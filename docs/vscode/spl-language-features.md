# Language server features

When an SPL file is open, the language server provides several features to improve reading and writing SPL code.

## Syntax highlighting and errors

Syntax highlighting for SPL files is provided to help differentiate keywords, types, functions, stream names, attributes, and more.

<img src="../../assets/vscode-syntax-highlight.png"
    alt="Screenshot showing contents of an SPL file containing differently colored words depending on their usage and meaning in the code"
    style="max-width: 100%; height: auto;">

Additionally, if an SPL file does not have correct syntax, an error is reported in the editor and viewable in the PROBLEMS panel.

<img src="../../assets/vscode-syntax-error.png"
    alt="Screenshot showing contents of an SPL file with a missing semi-colon. The output clause has a red squigly line underneath meaning an error is present. The PROBLEMS panel is also displayed with the file name and error."
    style="max-width: 100%; height: auto;">

## Folding

Fold portions of code using folding icons of the left side of the editor.

<img src="../../assets/vscode-code-folding.png"
    alt="Screenshot showing contents of an SPL file with partially collapsed blocks of code and arrows indicating what blocks can be expanded or collapsed."
    style="max-width: 100%; height: auto;">

## Find references

To find out where a stream or operator is used within a file or workspace, right-click on it and select `Go to References` or `Find All References`.

## IntelliSense

IntelliSense provides code hints, assistance, completions, and operator templates depending where your cursor is in the code. To trigger IntelliSense, 
enter ++ctrl+space++ (Windows/Linux) or ++cmd+space++ (macOS).

<img src="../../assets/vscode-intellisense-comp.png"
    alt="Screenshot showing IntelliSense suggestions in an SPL file."
    style="max-width: 50%; height: auto;">
<img src="../../assets/vscode-intellisense-op.png"
    alt="Screenshot showing IntelliSense operator template suggestions in an SPL file."
    style="max-width: 50%; height: auto;">

The language server is aware of types, functions, and operators provided by toolkits in the [configured Streams install and toolkit paths](../vscode/configuring-paths.md).

### View documentation

IntelliSense also provides quick info and documentation for parameters, functions, streams, and operators if available. Hover over an item to view its info or documentation.

<img src="../../assets/vscode-hover-doc.png"
    alt="Screenshot showing Custom operator documentation appears as a tooltip when user hovers over the Custom operator in their SPL application."
    style="max-width: 100%; height: auto;">

## Formatting

Format a selection of code or a whole document by using the built-in **Format Document** or **Format Selection** commands. See the [VS Code Formatting documentation](https://code.visualstudio.com/docs/editing/codebasics#_formatting) for more info.