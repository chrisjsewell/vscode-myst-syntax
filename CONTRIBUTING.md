# Development

## What's in the folder

* `package.json` - this is the manifest file in which language support is declared and the grammar file location defined.
* `src/` - this folder contains the source code to build the grammar.
* `syntaxes/myst.tmLanguage` - this is the generated Text mate grammar file that is used for tokenization.

## Building the grammar

Run the `src/build_grammar.py` script to generate the `syntaxes/myst.tmLanguage` file.
Also [pre-commit](https://pre-commit.com/) is used to run this script before each commit.

## Running the tests

Tests are run using [vscode-tmgrammar-test
TypeScript icon, indicating that this package has built-in type declarations](https://www.npmjs.com/package/vscode-tmgrammar-test/v/0.0.2)
The easiest way is also with [pre-commit](https://pre-commit.com/).

## Get up and running straight away

* Press `F5` to open a new window with the extension loaded.
* Create a new file with a file name suffix matching `.md`.
* Verify that syntax highlighting works and that the language configuration settings are working.

You can also use [VS Code scope inspector](https://code.visualstudio.com/api/language-extensions/syntax-highlight-guide#scope-inspector) to dynamically view the applied highlighting scopes.

## Make changes

* You can relaunch the extension from the debug toolbar after making changes to the files listed above.
* You can also reload (`Ctrl+R` or `Cmd+R` on Mac) the VS Code window with your extension to load your changes.

## Install the extension

* To start using your extension with Visual Studio Code copy it into the `<user home>/.vscode/extensions` folder and restart Code.
* To share your extension with the world, read on <https://code.visualstudio.com/docs> about publishing an extension.
- Use `vsce publish` to publish the extension to the marketplace.
- Also see https://github.com/eclipse/openvsx/wiki/Publishing-Extensions
