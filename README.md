# Fusion
---------

## Learning (Part - 1):

* Concept of interpreter.
* Concept of compiler.
* Difference between compilr and interpreter.
* Concept of token.
* Lexical analysis - The process of breaking sentences in to token is called lexical analysis.
* How **scanner** or **tokenizer** as the part of the intrpreter or compiler that does the lexical analysis.

## Learning (Part - 2):

* Concept of lexeme.
* Parsing - The process of recognizing a phrase in the stream of tokens or, to put it differently, the process of finding structure in the stream of tokens is called parsing.
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

## Learning (Part - 10):

* Added few grammar rules like block, declaration, variable_declaration, type_spec and updated some grammar like term and factor. Here below our new grammar -
  ```
  program : PROGRAM variable SEMI block DOT

    block : declarations compound_statement

    declarations : VAR (variable_declaration SEMI)+
                 | empty

    variable_declaration : ID (COMMA ID)* COLON type_spec

    type_spec : INTEGER | REAL

    compound_statement : BEGIN statement_list END

    statement_list : statement
                   | statement SEMI statement_list

    statement : compound_statement
              | assignment_statement
              | empty

    assignment_statement : variable ASSIGN expr

    empty :

    expr : term ((PLUS | MINUS) term)*

    term : factor ((MUL | INTEGER_DIV | FLOAT_DIV) factor)*

    factor : PLUS factor
           | MINUS factor
           | INTEGER_CONST
           | REAL_CONST
           | LPAREN expr RPAREN
           | variable

    variable: ID
  ```
* Made changes in the lexer like -
  * Adding new tokens.
  * Adding new reserved keywords and updating some previous one.
  * Adding new `skip_comment` method to handle pascal comment and updated the `integer` and `get_next_token` method.
* Added [new AST nodes](https://github.com/aniruddha2000/fusion/blob/master/part10/spi.py#L265-L286) like `Program`, `Block`, `VarDecl`, `Type`.
* Added [new methods](https://github.com/aniruddha2000/fusion/blob/master/part10/spi.py#L319-L369) and updated the existing parser methods like `program`, `term`, `factor`.
* Added [new visitor methods](https://github.com/aniruddha2000/fusion/blob/master/part10/spi.py#L570-L584) and updated the `visit_BinOp` method.

## Learning (Part - 11):

* **Symbol** - It is an identifier of some program entity like a variable, subroutine, or built-in type. Added two classes called `BuiltinTypeSymbol` , `VarSymbol` and both are inheriting the class `Symbol`.
* **Symbol table** - A symbol table is an abstract data type (ADT) for tracking various symbols in source code. Added `SymbolTable` class to handle this operation.
* Edited the `visit_Assign` and `visit_Var` method so that it can check weather a variable is declared or not before they are used in assignments and expressions.

## Learning (Part - 12):

* **Procedure declaration** - it is a language construct that defines an identifier (a procedure name) and associates it with a block of Pascal code.
* Updated the grammar(declarations) -
  ```
  declarations : VAR (variable_declaration SEMI)+
                     | (PROCEDURE ID SEMI block SEMI)*
                     | empty
  ```
* Updated the lexer by adding `PROCEDURE` in new token and reserved keywords.
* Updated the parser by adding the `ProcedureDecl` AST nodes and modified the [declarations method](https://github.com/aniruddha2000/fusion/blob/master/part12/spi.py#L332-L356) to support procedure declaration.
* Updated the interpreter by adding a `visit_ProcedureDecl` in the `Interpreter` class.

## Learning (Part - 13):

* **Semantic analysis** - it is just a process to help us determine whether a program makes sense, and that it has meaning, according to a language definition.
* Added an algorithm by which we store all information about variable declarations in a stash and when you see a variable reference, such as in the assignment statement `x := x + y`, search the stash by the variable’s name to see if the stash has any information about the variable. If yes then the variable has been declared and if not then there is a semantic error.
* Concept how to code a semantic analyzer that walks an AST, builds the symbol table, and does basic semantic checks.

## Learning (Part - 14):

* Concept of scope(global scope, nested scope) in a programming language and how it helps.
  * Every scope creates an isolated name space, which means that variables declared in a scope cannot be accessed    from outside of it.
  * You can re-use the same name in different scopes and know exactly, just by looking at the program source code,   what declaration the name refers to at every point in the program.
  * In a nested scope you can re-declare a variable with the same name as in the outer scope, thus effectively       hiding the outer declaration, which gives you control over access to different variables from the outer scope.
* Enhanced our `SymbolTable` class to `ScopedSymbolTable` class by updating some stuffs, So that it can handle scope feature in our new spi.
* Changed the grammar and updated the parser so that it can handle the procedure parameters.
* Concept of procedure symbol and introduced a new class called `ProcedureSymbol` class.
* Concept of scope symbol table. Added `visit_ProcedureDecl` and updated our `visit_Program` method to create the scoped symbol tables. Updated the semantic analyzer visitor methods `visit_VarDecl`, `visit_Var` for inserting and looking up the symbols.
* Updated the `ScopedSymbolTable` class and add a variable `enclosing_scope` that will hold a pointer to the scope’s enclosing scope and this will be link between scopes. Updated the `visit_Program` and `visit_ProcedureDecl` methods to create an actual link to the scope’s enclosing scope.
* We updated the `lookup` method in `ScopedSymbolTable` class to seach for variable declaration in the scopes.
* **source-to-source compiler** - It is a compiler that translates a program in some source language into a program in the same (or almost the same) source language.
