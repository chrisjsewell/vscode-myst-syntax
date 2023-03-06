# Development

## What's in the folder

* `package.json` - this is the manifest file in which language support is declared and the grammar file location defined.
* `src/` - this folder contains the source code to build the grammar.
* `syntaxes/myst.tmLanguage` - this is the generated Text mate grammar file that is used for tokenization.

## Building the grammar

Run the `src/build_grammar.py` script to generate the `syntaxes/myst.tmLanguage` file.
Also [pre-commit](https://pre-commit.com/) is used to run this script before each commit.

## Get up and running straight away

* Press `F5` to open a new window with the extension loaded.
* Create a new file with a file name suffix matching `.md`.
* Verify that syntax highlighting works and that the language configuration settings are working.

## Make changes

* You can relaunch the extension from the debug toolbar after making changes to the files listed above.
* You can also reload (`Ctrl+R` or `Cmd+R` on Mac) the VS Code window with your extension to load your changes.

## Install your extension

* To start using your extension with Visual Studio Code copy it into the `<user home>/.vscode/extensions` folder and restart Code.
* To share your extension with the world, read on <https://code.visualstudio.com/docs> about publishing an extension.
