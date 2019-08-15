import unittest
from calc5 import *


class LexerTestCase(unittest.TestCase):
    def makeLexer(self, text):
        lexer = Lexer(text)
        return lexer

    def test_lexer_integer(self):
        lexer = self.makeLexer('10')
        token = lexer.get_next_token()
        self.assertEqual(token.type, INTEGER)
        self.assertEqual(token.value, 10)

    def test_lexer_plus(self):
        lexer = self.makeLexer('+')
        token = lexer.get_next_token()
        self.assertEqual(token.type, PLUS)
        self.assertEqual(token.value, '+')

    def test_lexer_minus(self):
        lexer = self.makeLexer('-')
        token = lexer.get_next_token()
        self.assertEqual(token.type, MINUS)
        self.assertEqual(token.value, '-')

    def test_lexer_mul(self):
        lexer = self.makeLexer('*')
        token = lexer.get_next_token()
        self.assertEqual(token.type, MUL)
        self.assertEqual(token.value, '*')

    def test_lexer_div(self):
        lexer = self.makeLexer('/')
        token = lexer.get_next_token()
        self.assertEqual(token.type, DIV)
        self.assertEqual(token.value, '/')


class TestInterpreter(unittest.TestCase):

    def makeInterpreter(self, text):
        lexer = Lexer(text)
        interpreter = Interpreter(lexer)
        return interpreter

    def test_only_int(self):
        interpreter = self.makeInterpreter('3')
        result = interpreter.expr()
        self.assertEqual(result, 3)

    def test_plus_mul(self):
        interpreter = self.makeInterpreter('4 + 8 * 2')
        result = interpreter.expr()
        self.assertEqual(result, 20)

    def test_minus_div(self):
        interpreter = self.makeInterpreter('10 - 6 / 3')
        result = interpreter.expr()
        self.assertEqual(result, 8)

    def test_all_operators(self):
        interpreter = self.makeInterpreter('7 * 4 / 2 + 5 / 3 - 6')
        result = interpreter.expr()
        self.assertEqual(result, 9)

    def test_invalid_expression(self):
        interpreter = self.makeInterpreter('3 *')
        with self.assertRaises(Exception):
            interpreter.expr()


if __name__ == '__main__':
    unittest.main()
