# Developing custom operators

!!! tip "Before you begin"
    Check out the [Types of operators](https://doc.streams.teracloud.com/com.ibm.streams.dev.doc/doc/str_optype.html) page in the product documentation to evaluate options before proceeding.

If existing operators, including the `Custom` operator, are insufficent to implement application logic, you can create your own primitive operators using a lower-level programming language like C++, Java, or Python.

Additionally, if you have duplicate sets of operators within one or more applications, you may want to create a composite operator.

## Primitive operators

The extension provides convenient commands to create primitive operators within your workspace.

### Creating a C++ operator

1. Right-click in an editor or File Explorer
1. Hover over `SPL Project`
1. Click `Create C++ Primitive Operator` to open a wizard form
1. Fill in the namespace, name, and whether to make the operator generic or not
1. Click the `Create Operator` button

A namespace and operator directory will be created containing an operator model XML file and C++ code generation templates for your operator.

Proceed to implement the code and modify the operator model using these references:

* [Implementing generic operators](https://doc.streams.teracloud.com/com.ibm.streams.dev.doc/doc/implementinggenericoperators.html)
* [Implementing operators](https://doc.streams.teracloud.com/com.ibm.streams.dev.doc/doc/implementingoperators.html)
* [C++ operator model](https://doc.streams.teracloud.com/com.ibm.streams.ref.doc/doc/operatormodel.html)
* [C++ operator API](https://doc.streams.teracloud.com/external-reference/spl/operator/api/c++/index.html)

### Creating a Java operator

1. Right-click in an editor or File Explorer
1. Hover over `SPL Project`
1. Click `Create Java Primitive Operator` to open a wizard form
1. Fill in the namespace, name, and processing pattern
1. Click the `Create Operator` button

An implementation directory will be created containing the operator Java file.

Proceed to implement the code using these references:

* [Developing Java primitive operators](https://doc.streams.teracloud.com/com.ibm.streams.dev.doc/doc/javaprimitiveoperators.html)
* [Java Operator API](https://doc.streams.teracloud.com/external-reference/spl/operator/api/java/api/index.html)

!!! info "Important"
    Unlike C++ and Python, Java primitive operators must be compiled before they can be used by the SPL compiler. The extension creates a `Makefile` with a `javac` command to demonstrate this, but any build system can be used.

### Creating a Python operator

1. Right-click in an editor or File Explorer
1. Hover over `SPL Project`
1. Click `Create Python Primitive Operator` to open a wizard form
1. Fill in the name and processing pattern
1. Click the `Create Operator` button

An implementation directory will be created containing the operator Python file.

Proceed to implement the code using these references:

* [Developing Python primitive operators](https://doc.streams.teracloud.com/com.ibm.streams.dev.doc/doc/dev-python-prim-oper.html)
* [Python Operator API](https://doc.streams.teracloud.com/external-reference/spl/operator/api/python/)


### Using custom operators in your application

=== "C++ operators"
    After implementing your operator logic, invoke the operator directly in your SPL application. For an example, see the [C++ primitive operator at work](https://github.com/teracloud-streams/samples/blob/main/Examples-for-beginners/035_c%2B%2B_primitive_operator_at_work/my.sample/Main.spl) application.

=== "Java operators"
    1. After implementing your operator logic, compile the Java operator source code
    1. Invoke the operator directly in your SPL application

=== "Python operators"
    After implementing your operator logic, it is easiest to use a [PythonOp operator](https://doc.streams.teracloud.com/com.ibm.streams.toolkits.doc/spldoc/dita/tk\$spl/op\$spl.utility$PythonOp.html) in your SPL application to call the module. For an example, see the [PythonOpScoring](https://github.com/teracloud-streams/samples/blob/main/PythonOpScoring/sample/PythonOpScoring.spl) application.

## Composite operators

Composite operators are defined in SPL files and can utilize the SPL language server.

### Creating a composite operator

1. Create or open an SPL file you want the composite operator in
1. Activate IntelliSense: enter ++ctrl+space++ (Windows/Linux) or ++cmd+space++ (macOS)
1. Type `Add new composite with ports`
1. Hit ++enter++

!!! tip "Tip"
    Composite operators can have parameters similar to primitive operators. See the [Composite operators tutorial](https://doc.streams.teracloud.com/com.ibm.streams.tutorials.doc/doc/compositeoperators.html) in the product documentation and the [Multiple composites at work sample](https://github.com/teracloud-streams/samples/blob/main/Examples-for-beginners/028_multiple_composites_at_work/my.sample2/StockMatch.spl) for examples.

### Using a composite operator in your application

After implementing your composite operator, invoke the operator directly in your SPL application. For an example, see the [Multiple composites at work](https://github.com/teracloud-streams/samples/blob/main/Examples-for-beginners/028_multiple_composites_at_work/my.sample1/Main.spl) application.