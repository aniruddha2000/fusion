# Fusion
---------

## Learning (Part - 1):

* Concept of interpreter.
* Concept of compiler.
* Difference between compilr and interpreter.
* Concept of token.
* How lexical analysis works.
* How **scanner** or **tokenizer** as the part of the intrpreter or compiler that does the lexical analysis.

## Learning (Part - 2):

* Concept of lexeme.
* How interpreter does parsing.
* How parser works.

## Learning (Part - 3):

* Concept of syntax diagram.
* How syntax analysis works.
* How syntax analyzer works.
* How the interpreter is returning the only number if I don't pass any arithmatic operator.
* How the interpreter is performing while I pass arbitary number of additions and subtractions.
* How the interpreter is performing while I pass arbitary number of multiplication and division.

## Learning (Part - 4):

* The concept of grammer.
* The idea of rules / productions in the grammer.
* Concept and identification of terminals(expt, factor) and non-terminals(PLUS, MINUS, etc).
* **Head** and **Body** of a rule.
* **start symbol -** It is the non-terminal symbol of the left side of the first rule.
* [Here](https://github.com/aniruddha2000/fusion/blob/master/part4/calc4.py#L92) we can set the current token to the first token taken from the input. Because whenever the object of `Interpreter()` class will be created then the `__init__()` method will be called. So we don't have to explicitly set the token to the first token like [here](https://github.com/aniruddha2000/fusion/blob/master/part3/calc3.py#L116).

## Learning (Part - 5):

* concept of **associativity** and **precedence** for operator.
* How we calculate arithmetic expressions containing any number of +, -, *, or / operators.
* Learned how to write unit tests.

## Learning (Part - 6):

* I have learned How to calculate an arithmatic expression containing parentheses.
* Leraned how to divide parentheses into tokens.

## Learning (Part - 7):

* Concept about the tree data structure.
* Idea of **root**, **node**, **interior node**, **leaf node**, **parent**, **child(left, right)**.
* Concept of concrete syntax tree.
* **AST(abstract-syntax-tree)** - An abstract syntax tree (AST) is a tree that represents the abstract syntactic structure of a language construct where each interior node and the root node represents an operator, and the children of the node represent the operands of that operator.
* Difference between AST and the parse tree.
* Various traversal method(preorder, inorder, postorder).
* Modified the parser and interpreter and split them apart. Now the parser is getting a token from lexer and returning generating the AST for the interpreter to traverse and interpret the input.
