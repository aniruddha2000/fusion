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


if __name__ == '__main__':
    unittest.main()
