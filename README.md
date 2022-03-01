# gradleRIO_CompilationDatabase

This will generate a `compile_commands.json` file based on a gradleRIO project.

## Usage
```bash
$ chmod +x ./rioCDGen.py # do this once
$ ./rioCDGen.py --help

usage: rioCDGen.py [-h] [--compiler COMPILER] [--build-type {Debug,Release}] [--year YEAR] [--source SOURCE] [--pretty]

Generate a compile_commands.json for an frc gradle project

optional arguments:
  -h, --help            show this help message and exit
  --compiler COMPILER   path to the cross-compiler that gradleRIO uses. If not specified, the script will search for it
  --build-type {Debug,Release}, -bt {Debug,Release}
                        The type of build. Can be Debug or Release. Defaults to Debug
  --year YEAR, -y YEAR  The year of the toolchain/project. Defaults to the current year
  --source SOURCE, -S SOURCE, -s SOURCE
                        The root directory of the project(should be the directory with your build.gradle file. Defaults to cwd
  --pretty              pretty prints the ouput
```

**note**: run this in the project directory or use the -S option


## Requirements
* python3

## Platforms
* Linux
* MaxOS (hopefully)
* Windows (in theory)

## TODO:
* ~~more customizability~~ implemented in [f05923c](https://github.com/theVerySharpFlat/gradleRIO_CompilationDatabase/commit/f9a073cb6d5377552a043b9681e57d9ad644b616) 
* make it a pip package?
* make it cross platform
