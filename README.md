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

## Learning (Part - 8):

* Concept of unary operators and it's precedence.
* Extending the grammar to handle unary plus and minus operators.
* Extending the parser to generate an AST with `UnaryOp` node and the interpreter with a new `visit_UnaryOp` method to interpret unary operators.
* Calling the function `factor(self)` from inside it in [#L168](https://github.com/aniruddha2000/fusion/blob/master/part8/spi.py#L168) and [#L172](https://github.com/aniruddha2000/fusion/blob/master/part8/spi.py#L172) so that it can get the unary operator token.

## Learning (Part - 9):

* Made changes to the grammar.
    ```
    program : compound_statement DOT

    compound_statement : BEGIN statement_list END

    statement_list : statement
                   | statement SEMI statement_list

    statement : compound_statement
              | assignment_statement
              | empty

    assignment_statement : variable ASSIGN expr

    empty :

    expr: term ((PLUS | MINUS) term)*

    term: factor ((MUL | DIV) factor)*

    factor : PLUS factor
           | MINUS factor
           | INTEGER
           | LPAREN expr RPAREN
           | variable

    variable: ID
    ```
* Made changes in the lexer like adding new tokens and added a `peak` and `_id` method and also edited the `get_next_token` method for new tokens.
* Added new AST nodes(Compound, Assign, Var, NoOp) to the parser for new language constructs.
* Added [new methods](https://github.com/aniruddha2000/fusion/blob/master/part9/spi.py#L228-L301) corresponding to the new grammar rules to our recursive-descent parser and updated the existing methods like `factor` and `term`.
* Added [new visitor methods](https://github.com/aniruddha2000/fusion/blob/master/part9/spi.py#L442-L459) to the interpreter.
* Added a dictionary for storing variables.
