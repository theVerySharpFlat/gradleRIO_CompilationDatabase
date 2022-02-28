#!/usr/bin/env python3
import os, sys
import datetime
import json

year = datetime.date.today().year
buildType = "Debug"

# finds the roboRIO g++ cross compiler
def findCompiler() -> str:
    name = os.path.sep + os.path.join(f"{year}", "roborio", "bin", f"arm-frc{year}-linux-gnueabi-g++")
    path = os.path.expanduser('~')
    for root, dirs, files in os.walk(path):
        for file in files:
            if name in os.path.join(root, file):
                return os.path.join(root, file)

# find the options file
def findOptionsTXT() -> str():
    name = os.path.join(f"compileFrcUserProgram{buildType}ExecutableFrcUserProgramCpp", "options.txt")
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if name in os.path.join(root, file):
                return os.path.join(root, file)

# get the options from the file (replace newlines with spaces)
def getOptionString(filePath: str) -> str:
    optionString = None
    with open(filePath) as file:
        dat = file.read()
        optionsString = dat.replace("\n", " ")

    return optionsString

# find all cpp files
def getAllCppFiles():
    foundFiles = []
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith(".cpp"):
                foundFiles.append(os.path.join(root, file))

    return foundFiles

def findFile(filename: str, filepath: str) -> str:
    for root, dirs, files in os.walk(filepath):
        if filename in files:
            return os.path.join(root, filename)

def generateCompileCommands(compilerPath: str, optionString: str):
    model = []
    for file in getAllCppFiles():
        objectFile = os.path.basename(file).replace(".cpp", ".o")
        objectFile = findFile(objectFile, os.path.join(os.getcwd(), "build"))

        if objectFile == None:
            print(f"  failed to find object file for cpp file \"{file}\". Skipping...")
            continue
        else:
            print(f"  generating definition for {file}")

        fileObj = {
            "directory": os.path.join(os.getcwd(), "build"),
            "command": f"{compilerPath} {optionString} -o {objectFile} {file}",
            "file": f"{file}"
        }

        model.append(fileObj)

    print(f"dumping to {os.path.join(os.getcwd(), 'compile_commands.json')}")
    with open("compile_commands.json", mode='w') as compilationDatabaseFile:
        json.dump(model, compilationDatabaseFile)

def main():

    # find compiler
    print("searching for compiler... ", end="")
    compilerPath = findCompiler()
    if compilerPath == None:
        print("Failed to find compiler!")
        exit(1)
    print(f"using {compilerPath}")

    # find the options.txt file which lists the compile options
    print("searching for options.txt...", end="")
    optionsFilePath = findOptionsTXT()
    if optionsFilePath == None:
        print("Could not find options.txt. Perhaps you need to build?")
        exit(1)
    print(f"using {optionsFilePath}")

    # get the options
    print("getting compiler options... ", end="")
    compilerOptions = getOptionString(optionsFilePath)
    if compilerOptions == None:
        print("could not get compiler options for some reason!")
        exit(1)
    print("success")

    #generate the file
    print("generating compile_commands.json... ")
    generateCompileCommands(compilerPath, compilerOptions)

if __name__ == "__main__":
    main()
