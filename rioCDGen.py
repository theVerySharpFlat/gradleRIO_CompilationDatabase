#!/bin/python3
import os, sys
import datetime

year = datetime.date.today().year
buildType = "Debug"

# finds the roboRIO g++ cross compiler
def findCompiler() -> str:
    name = f"/{year}/roborio/bin/arm-frc{year}-linux-gnueabi-g++"
    path = os.path.expanduser('~')
    for root, dirs, files in os.walk(path):
        for file in files:
            if name in os.path.join(root, file):
                return os.path.join(root, file)

# find the options file
def findOptionsTXT() -> str():
    name = f"compileFrcUserProgram{buildType}ExecutableFrcUserProgramCpp/options.txt"
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
    print("getting compiler options... ")
    compilerOptions = getOptionString(optionsFilePath)

if __name__ == "__main__":
    main()