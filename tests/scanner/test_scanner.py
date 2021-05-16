from src.data_source.string_source import StringSource
from src.data_source.file_source import FileSource
from src.exceptions.scanning_exception import ScanningException
from src.scanner.scanner import Scanner
from src.utils.token_type import TokenType
from src.utils.token import Token
from src.utils.position import Position

from src.exceptions.scanner_exception import ScannerException

import io
import os

import unittest

class TestScanner(unittest.TestCase):


    def test_invalid_source(self):

        with self.assertRaises(ScannerException) as cm:
            Scanner(source="string_source")

        the_exception = cm.exception

        self.assertEqual(
            the_exception.message,
            "The given source is not an instance of BaseSource"
        )


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



    def test_leading_zero(self):

        string_source = StringSource(
            io.StringIO("010")
        )

        scanner = Scanner(source=string_source)

        with self.assertRaises(ScanningException) as cm:
            scanner.next_token()

        the_exception = cm.exception

        self.assertEqual(
            the_exception.message,
            f"Scanning exception at position {scanner.token_position}:\n"
            f"Non-zero number can't contain anything after zero"
        )


    def test_max_number(self):

        string_source = StringSource(
            io.StringIO("1000000000000000000000000000000000;")
        )

        scanner = Scanner(string_source)


        with self.assertRaises(ScanningException) as cm:
            scanner.next_token()

        the_exception = cm.exception

        self.assertEqual(
            the_exception.message,
            f"Scanning exception at position {scanner.token_position}:\n"
            f"Max allowed number value is {Token.MAX_NUMBER}"
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
            io.StringIO('= "To be or not to be.";')
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
                Token(TokenType.ASSIGN, Position(line=1, column=1), value="="),
                Token(TokenType.STRING_LITERAL, Position(line=1, column=3), value="To be or not to be"),
                Token(TokenType.SEMICOLON, Position(line=1, column=24), value=";")
            ],
            "Something went wrong during the string literal tokenization"
        )



    def test_not_closed_exception(self):


        # test if raised exception for missing "
        string_source = StringSource(
            io.StringIO('"To be or not to be.;')
        )

        scanner = Scanner(source=string_source)

        with self.assertRaises(ScanningException) as cm:
            scanner.next_token()


        exception_message = cm.exception.message

        self.assertEqual(
            exception_message,
            f"Scanning exception at position {scanner.token_position}:\n"
            f"Missing closing \""
        )



    def test_identifier(self):

        string_source = StringSource(
            io.StringIO("is_prime = true;")
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
                Token(TokenType.IDENTIFIER, Position(line=1, column=1), value="is_prime"),
                Token(TokenType.ASSIGN, Position(line=1, column=10), value="="),
                Token(TokenType.BOOL_LITERAL, Position(line=1, column=12), value="true"),
                Token(TokenType.SEMICOLON, Position(line=1, column=16), value=";")
            ],
            "Something went wrong during identifier and boolean tokenization"
        )



    def test_id_length(self):

        string_source = StringSource(
            io.StringIO("is_prime_second_third_fourth_louis_armstrongs_anything_else_that_comes_to_your_mind_when_creating_a_too_long_identifier_name = true;")
        )

        scanner = Scanner(string_source)

        with self.assertRaises(ScanningException) as cm:
            scanner.next_token()

        exception_message = cm.exception.message

        self.assertEqual(
            exception_message,
            f"Scanning exception at position {scanner.token_position}:\n"
            f"Exceeded length of the identifier"
        )


    def test_id_valid(self):

        string_source = StringSource(
            io.StringIO("$/")
        )

        scanner = Scanner(string_source)

        with self.assertRaises(ScanningException) as cm:
            scanner.next_token()

        self.assertEqual(
            cm.exception.message,
            f"Scanning exception at position {scanner.token_position}:\n"
            f"Invalid identifier"
        )



    def test_comment(self):

        file_source = FileSource(
            io.open("../../lang_codes/real_codes/comment.txt")
        )

        scanner = Scanner(file_source)

        scanner.next_token()
        current_token = scanner.token
        tokens = []

        while current_token.token_type != TokenType.EOF:
            tokens.append(current_token)
            scanner.next_token()
            current_token = scanner.token

        file_source.close()

        self.assertListEqual(
            tokens,
            [
                Token(TokenType.COMMENT, Position(line=1, column=1), value="# this is the comment"),
                Token(TokenType.COMMENT, Position(line=2, column=1), value="# 234134 th1s 1$ also # a comment"),
                Token(TokenType.COMMENT, Position(line=3, column=1), value="# and :sd...a91.4/3 is comment either")
            ],
            "Something went wrong while detecting comment tokens"
        )



    def test_keyword1(self):

        string_source = StringSource(
            io.StringIO("if (true) {} else if {} else {}")
        )

        scanner = Scanner(string_source)
        scanner.next_token()
        current_token = scanner.token
        tokens = []

        while current_token.token_type != TokenType.EOF:
            tokens.append(current_token)
            scanner.next_token()
            current_token = scanner.token

        string_source.string_stream.close()

        self.assertListEqual(
            tokens,
            [
                Token(TokenType.IF, Position(line=1, column=1), value="if"),
                Token(TokenType.OPEN_PARENTHESIS, Position(line=1, column=4), value="("),
                Token(TokenType.BOOL_LITERAL, Position(line=1, column=5), value="true"),
                Token(TokenType.CLOSING_PARENTHESIS, Position(line=1, column=9), value=")"),
                Token(TokenType.OPEN_CURLY_BRACKET, Position(line=1, column=11), value="{"),
                Token(TokenType.CLOSING_CURLY_BRACKET, Position(line=1, column=12), value="}"),
                Token(TokenType.ELSE, Position(line=1, column=14), value="else"),
                Token(TokenType.IF, Position(line=1, column=19), value="if"),
                Token(TokenType.OPEN_CURLY_BRACKET, Position(line=1, column=22), value="{"),
                Token(TokenType.CLOSING_CURLY_BRACKET, Position(line=1, column=23), value="}"),
                Token(TokenType.ELSE, Position(line=1, column=25), value="else"),
                Token(TokenType.OPEN_CURLY_BRACKET, Position(line=1, column=30), value="{"),
                Token(TokenType.CLOSING_CURLY_BRACKET, Position(line=1, column=31), value="}"),
            ]
        )



    def test_keywords2(self):

        string_source = StringSource(
            io.StringIO("while foreach return define this reflect by_ref class reflect recursive")
        )

        scanner = Scanner(string_source)
        scanner.next_token()
        current_token = scanner.token
        tokens = []

        while current_token.token_type != TokenType.EOF:
            tokens.append(current_token)
            scanner.next_token()
            current_token = scanner.token

        string_source.string_stream.close()

        self.assertListEqual(
            tokens,
            [
                Token(TokenType.WHILE, Position(line=1, column=1), value="while"),
                Token(TokenType.FOREACH, Position(line=1, column=7), value="foreach"),
                Token(TokenType.RETURN, Position(line=1, column=15), value="return"),
                Token(TokenType.DEFINE, Position(line=1, column=22), value="define"),
                Token(TokenType.THIS, Position(line=1, column=29), value="this"),
                Token(TokenType.REFLECT, Position(line=1, column=34), value="reflect"),
                Token(TokenType.BY_REF, Position(line=1, column=42), value="by_ref"),
                Token(TokenType.CLASS, Position(line=1, column=49), value="class"),
                Token(TokenType.REFLECT, Position(line=1, column=55), value="reflect"),
                Token(TokenType.RECURSIVE, Position(line=1, column=63), value="recursive")
            ]
        )



    def test_unknown_symbol(self):

        string_source = StringSource(
            io.StringIO("?self;")
        )

        scanner = Scanner(string_source)


        with self.assertRaises(ScanningException) as cm:
            scanner.next_token()

        the_exception = cm.exception

        self.assertEqual(
            the_exception.message,
            f"Scanning exception at position {scanner.token_position}:\nUnknown symbol"
        )