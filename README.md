# DelGen.Check

Checks Deli manifests to make sure they follow correct formatting.

This includes that all fields are present, and that:

- "guid"
  - Makes sure that there are no capitals or spaces
- "version" and "require"
  - Follow correct versioning
- "dependencies"
  - Is a dict
- "authors"
  - Is a list
- "assets"
  - Is a dict
  - Has a loading phase

## Installation/Usage

1. Download `DelGen.Check.exe` from the [Releases](https://github.com/nayr31/DelGen.Check/releases) page.
2. Place it in a folder next to your files you wish to check. Make sure that the file is not zipped. If you do not have read permissions inside the folder, move the files somewhere else, or run `DelGen.Check.exe` as administrator.
3. Run the program and follow the terminal prompts.
