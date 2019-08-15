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
