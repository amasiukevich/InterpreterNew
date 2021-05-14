from src.data_source.string_source import StringSource
from src.data_source.file_source import FileSource
from src.scanner.scanner import Scanner
from src.utils.token_type import TokenType
from src.utils.token import Token
from src.utils.position import Position

import io
import os

import unittest

class TestScanner(unittest.TestCase):

    def test_ignoring_whitespaces(self):

        file_stream = io.open(
            os.path.abspath("../../lang_codes/testing/test_arithmetic")
        )

        file_source = FileSource(file_stream)
        scanner = Scanner(source=file_source)

        chars = []
        while scanner.source.character != -1:
            scanner.ignore_whitespaces()
            chars.append(file_source.get_curr_char())
            file_source.read_char()

        file_stream.close()

        real_chars = [c for c in "a+bc-d"]
        self.assertListEqual(chars, real_chars, "Doesn't ignore whitespaces")


    def test_eof_creation(self):

        string_stream_eof = io.StringIO("")
        string_source = StringSource(string_stream_eof)

        scanner = Scanner(source=string_source)
        scanner.next_token()

        string_stream_eof.close()

        self.assertEqual(scanner.token.token_type, TokenType.EOF, "Token must be of type EOF")

    def test_single_param_creation(self):

        string_source = StringSource(
            io.StringIO("+    - /     {{ } )( * % ][,.;")
        )

        scanner = Scanner(source=string_source)

        scanner.next_token()
        current_token = scanner.token
        tokens = []
        while current_token.token_type != TokenType.EOF:
            tokens.append(current_token)
            scanner.next_token()
            current_token = scanner.token

        string_source.close()

        self.assertListEqual(
            tokens,
            [
                Token(TokenType.PLUS, Position(line=1, column=1), value="+"),
                Token(TokenType.MINUS, Position(line=1, column=6), value="-"),
                Token(TokenType.DIVIDE, Position(line=1, column=8), value="/"),
                Token(TokenType.OPEN_CURLY_BRACKET, Position(line=1, column=14), value="{"),
                Token(TokenType.OPEN_CURLY_BRACKET, Position(line=1, column=15), value=""),
                Token(TokenType.CLOSING_CURLY_BRACKET, Position(line=1, column=17), value="}"),
                Token(TokenType.CLOSING_PARENTHESIS, Position(line=1, column=19), value=""),
                Token(TokenType.OPEN_PARENTHESIS, Position(line=1, column=20), value="("),
                Token(TokenType.MULTIPLY, Position(line=1, column=22), value="*"),
                Token(TokenType.MODULO, Position(line=1, column=24), value="%"),
                Token(TokenType.CLOSING_BRACKET, Position(line=1, column=26), value="]"),
                Token(TokenType.OPEN_BRACKET, Position(line=1, column=27), value="["),
                Token(TokenType.COMMA, Position(line=1, column=28), value=","),
                Token(TokenType.ACCESS, Position(line=1, column=29), value="."),
                Token(TokenType.SEMICOLON, Position(line=1, column=30), value=';')
            ],
            "Something went wrong while detecting tokens"
        )



    def test_double_param_creation(self):

        string_source = StringSource(
            io.StringIO(">= <= !=  == && ||")
        )

        scanner = Scanner(source=string_source)

        scanner.next_token()
        current_token = scanner.token
        tokens = []

        while current_token.token_type != TokenType.EOF:
            tokens.append(current_token)
            scanner.next_token()
            current_token = scanner.token

        string_source.close()

        self.assertListEqual(
            tokens,
            [
                Token(TokenType.GREATER_EQUAL, Position(line=1, column=1), value=">="),
                Token(TokenType.LESS_EQUAL, Position(line=1, column=4), value="<="),
                Token(TokenType.NOT_EQUAL, Position(line=1, column=7), value="!="),
                Token(TokenType.EQUAL, Position(line=1, column=11), value="=="),
                Token(TokenType.AND, Position(line=1, column=14), value="&&"),
                Token(TokenType.OR, Position(line=1, column=17), value="||")
            ],
            "Something went wrong while detecting double-character tokens"
        )


    def test_number(self):

        string_source = StringSource(
            io.StringIO("[10, 12, 13, 0]")
        )

        scanner = Scanner(source=string_source)
        scanner.next_token()
        current_token = scanner.token
        tokens = []

        while current_token.token_type != TokenType.EOF:
            tokens.append(current_token)
            scanner.next_token()
            current_token = scanner.token

        string_source.close()

        self.assertListEqual(
            tokens,
            [
                Token(TokenType.OPEN_BRACKET, Position(line=1, column=1), value="["),
                Token(TokenType.NUMERIC_LITERAL, Position(line=1, column=2), value=10),
                Token(TokenType.COMMA, Position(line=1, column=4), value=","),
                Token(TokenType.NUMERIC_LITERAL, Position(line=1, column=6), value=12),
                Token(TokenType.COMMA, Position(line=1, column=8), value=","),
                Token(TokenType.NUMERIC_LITERAL, Position(line=1, column=10), value=13),
                Token(TokenType.COMMA, Position(line=1, column=12), value=","),
                Token(TokenType.NUMERIC_LITERAL, Position(line=1, column=14), value=0),
                Token(TokenType.CLOSING_BRACKET, Position(line=1, column=15), value="]"),

            ],
            "Something went wrong during the number tokenization"
        )



    def test_fraction_number(self):

        string_source = StringSource(
            io.StringIO("[7.806, 5.25]")
        )

        scanner = Scanner(source=string_source)

        scanner.next_token()
        current_token = scanner.token
        tokens = []

        while current_token.token_type != TokenType.EOF:
            tokens.append(current_token)
            scanner.next_token()
            current_token = scanner.token

        string_source.close()



        self.assertListEqual(
            tokens,
            [
                Token(TokenType.OPEN_BRACKET, Position(line=1, column=1), value="["),
                Token(TokenType.NUMERIC_LITERAL, Position(line=1, column=2), value=7.806),
                Token(TokenType.COMMA, Position(line=1, column=7), value=","),
                Token(TokenType.NUMERIC_LITERAL, Position(line=1, column=9), value=5.25),
                Token(TokenType.CLOSING_BRACKET, Position(line=1, column=13), value="]"),

            ],
            "Something went wrong during fraction number tokenization"
        )





    def test_string_literal(self):

        string_source = StringSource(
            io.StringIO('quote = "To be or not to be.";')
        )

        scanner = Scanner(source=string_source)
        current_token = scanner.token
        tokens = []

        while current_token.token_type != TokenType.EOF:
            tokens.append(current_token)
            scanner.next_token()
            current_token = scanner.token

        string_source.close()

        # TODO: beware of values of tokens
        self.assertListEqual(
            tokens,
            [
                Token(TokenType.IDENTIFIER, Position(line=1, column=0)),
                Token(TokenType.ASSIGN, Position(line=1, column=6)),
                Token(TokenType.STRING_LITERAL, Position(line=1, column=8)),
                Token(TokenType.SEMICOLON, Position(line=1, column=29))
            ],
            "Something went wrong during the string literal tokenization"
        )

    def test_identifier(self):

        string_source = StringSource(
            io.StringIO("is_prime_number = true;")
        )

        scanner = Scanner(source=string_source)
        current_token = scanner.token
        tokens = []

        while current_token.token_type != TokenType.EOF:
            tokens.append(current_token)
            scanner.next_token()
            current_token = scanner.token

        string_source.close()

        # TODO: beware of values of tokens
        self.assertListEqual(
            tokens,
            [
                Token(TokenType.IDENTIFIER, Position(line=1, column=0)),
                Token(TokenType.ASSIGN, Position(line=1, column=16)),
                Token(TokenType.BOOL_LITERAL, Position(line=1, column=18)),
                Token(TokenType.SEMICOLON, Position(line=1, column=22))
            ],
            "Something went wrong during identifier and boolean tokenization"
        )

    def test_comment(self):

        file_source = FileSource(
            io.open("../../lang_codes/real_codes/comment.txt")
        )

        scanner = Scanner(file_source)
        current_token = scanner.token

        tokens = []

        while current_token.token_type != TokenType.EOF:
            tokens.append(current_token)
            scanner.next_token()
            current_token = scanner.token

        file_source.close()

        # TODO: beware of values of tokens
        self.assertListEqual(
            tokens,
            [
                Token(TokenType.COMMENT, Position(line=1, column=0)),
                Token(TokenType.COMMENT, Position(line=2, column=0)),
                Token(TokenType.COMMENT, Position(line=3, column=0))
            ],
            "Something went wrong while detecting comment tokens"
        )



    def test_keyword(self):

        file_source = FileSource(
            io.open("../../lang_codes/real_codes/iterate_through_func_result.txt")
        )

        scanner = Scanner(file_source)
        current_token = scanner.token

        tokens = []

        while current_token.token_type != TokenType.EOF:
            tokens.append(current_token)
            scanner.next_token()
            current_token = scanner.token
        file_source.close()

        # TODO: beware of values of tokens
        self.assertListEqual(
            tokens,
            [
                Token(TokenType.DEFINE, Position(line=1, column=0)),
                Token(TokenType.IDENTIFIER, Position(line=1, column=7)),
                Token(TokenType.OPEN_PARENTHESIS, Position(line=1, column=19)),
                Token(TokenType.IDENTIFIER, Position(line=1, column=20)),
                Token(TokenType.CLOSING_PARENTHESIS, Position(line=1, column=23)),
                Token(TokenType.OPEN_CURLY_BRACKET, Position(line=1, column=25)),
                Token(TokenType.IDENTIFIER, Position(line=2, column=4)),
                Token(TokenType.ASSIGN, Position(line=2, column=13)),
                Token(TokenType.OPEN_BRACKET, Position(line=2, column=15)),
                Token(TokenType.CLOSING_BRACKET, Position(line=2, column=16)),
                Token(TokenType.SEMICOLON, Position(line=2, column=17)),
                Token(TokenType.IDENTIFIER, Position(line=3, column=4)),
                Token(TokenType.ASSIGN, Position(line=3, column=6)),
                Token(TokenType.NUMERIC_LITERAL, Position(line=3, column=8)),
                Token(TokenType.SEMICOLON, Position(line=3, column=9)),
                Token(TokenType.FOREACH, Position(line=4, column=4)),
                Token(TokenType.IDENTIFIER, Position(line=4, column=12)),
                Token(TokenType.IN, Position(line=4, column=14)),
                Token(TokenType.IDENTIFIER, Position(line=4, column=17)),
                Token(TokenType.OPEN_CURLY_BRACKET, Position(line=4, column=21)),
                Token(TokenType.IDENTIFIER, Position(line=5, column=8)),
                Token(TokenType.ACCESS, Position(line=5, column=16)),
                Token(TokenType.IDENTIFIER, Position(line=5, column=17)),
                Token(TokenType.OPEN_PARENTHESIS, Position(line=5, column=23)),
                Token(TokenType.IDENTIFIER, Position(line=5, column=24)),
                Token(TokenType.MULTIPLY, Position(line=5, column=26)),
                Token(TokenType.IDENTIFIER, Position(line=5, column=28)),
                Token(TokenType.CLOSING_PARENTHESIS, Position(line=5, column=29)),
                Token(TokenType.SEMICOLON, Position(line=5, column=30)),
                Token(TokenType.CLOSING_CURLY_BRACKET, Position(line=6, column=4)),
                Token(TokenType.RETURN, Position(line=7, column=4)),
                Token(TokenType.IDENTIFIER, Position(line=7, column=11)),
                Token(TokenType.SEMICOLON, Position(line=7, column=19)),
                Token(TokenType.CLOSING_CURLY_BRACKET, Position(line=8, column=0)),

                # main function
                Token(TokenType.DEFINE, Position(line=10, column=0)),
                Token(TokenType.IDENTIFIER, Position(line=10, column=7)),
                Token(TokenType.OPEN_PARENTHESIS, Position(line=10, column=11)),
                Token(TokenType.CLOSING_PARENTHESIS, Position(line=10, column=12)),
                Token(TokenType.OPEN_CURLY_BRACKET, Position(line=10, column=14)),
                Token(TokenType.FOREACH, Position(line=11, column=4)),
                Token(TokenType.IDENTIFIER, Position(line=11, column=12)),
                Token(TokenType.IN, Position(line=11, column=20)),
                Token(TokenType.IDENTIFIER, Position(line=11, column=23)),
                Token(TokenType.OPEN_PARENTHESIS, Position(line=11, column=35)),
                Token(TokenType.OPEN_BRACKET, Position(line=11, column=36)),
                Token(TokenType.NUMERIC_LITERAL, Position(line=11, column=37)),
                Token(TokenType.COMMA, Position(line=11, column=38)),
                Token(TokenType.NUMERIC_LITERAL, Position(line=11, column=40)),
                Token(TokenType.COMMA, Position(line=11, column=41)),
                Token(TokenType.NUMERIC_LITERAL, Position(line=11, column=43)),
                Token(TokenType.COMMA, Position(line=11, column=44)),
                Token(TokenType.CLOSING_BRACKET, Position(line=11, column=45)),
                Token(TokenType.CLOSING_PARENTHESIS, Position(line=11, column=46)),
                Token(TokenType.OPEN_CURLY_BRACKET, Position(line=11, column=48)),
                Token(TokenType.IDENTIFIER, Position(line=12, column=8)),
                Token(TokenType.OPEN_PARENTHESIS, Position(line=12, column=13)),
                Token(TokenType.IDENTIFIER, Position(line=12, column=14)),
                Token(TokenType.CLOSING_PARENTHESIS, Position(line=12, column=21)),
                Token(TokenType.SEMICOLON, Position(line=12, column=22)),
                Token(TokenType.CLOSING_CURLY_BRACKET, Position(line=13, column=4)),
                Token(TokenType.CLOSING_CURLY_BRACKET, Position(line=14, column=0)),
            ]
        )