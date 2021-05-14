from .keyword_mapper import KeywordMapper
from ..data_source.base_source import BaseSource
from ..utils.token import Token
from ..utils.token_type import TokenType


class Scanner():



    def __init__(self, source):

        if not isinstance(source, BaseSource):
            # TODO: make custom exception here
            raise Exception("The given source is not an instance of BaseSource")

        self.source = source
        self.kw_mapper = KeywordMapper()
        self.token = Token(TokenType.UNKNOWN)



    def next_token(self):

        self.ignore_whitespaces()
        self.token_position = self.source.position.clone()
        if self.construct_eof():
            return
        elif self.construct_single_char_oper():
            return
        elif self.construct_double_char_oper():
            return
        elif self.construct_number():
            return
        elif self.construct_string_literal():
            return
        elif self.construct_identifier():
            pass
        elif self.construct_comment():
            pass
        elif self.construct_keyword():
            pass

        else:
            self.token = Token(TokenType.UNKNOWN, position=self.token_position)
            raise Exception(self.token_position, "Unknown symbol")

    def ignore_whitespaces(self):

        if self.source.character != -1:
            while self.source.character.isspace():
                self.source.read_char()



    def construct_eof(self):

        character_not_exist = (self.source.character == -1)
        if character_not_exist:
            self.token = Token(TokenType.EOF, position=self.token_position)
            self.source.read_char()

        return character_not_exist



    def construct_single_char_oper(self):

        try:
            tmp_token_type = self.kw_mapper.SINGLE_CHAR_MAP[self.source.character]
            self.token = Token(tmp_token_type, position=self.token_position, value=self.source.character)
            self.source.read_char()
            return True
        except:
            return False



    def construct_double_char_oper(self):

        first_char = self.source.character
        is_recognized = True

        if first_char == "<":
            self.source.read_char()
            second_char = self.source.character
            if second_char == "=":
                self.token = Token(TokenType.LESS_EQUAL, position=self.token_position, value="<=")
                self.source.read_char()
            else:
                self.token = Token(TokenType.LESS, position=self.token_position, value="<")
        elif first_char == ">":
            self.source.read_char()
            second_char = self.source.character
            if second_char == "=":
                self.token = Token(TokenType.GREATER_EQUAL, position=self.token_position, value=">=")
                self.source.read_char()
            else:
                self.token = Token(TokenType.GREATER, position=self.token_position, value=">")
        elif first_char == "!":
            self.source.read_char()
            second_char = self.source.character
            if second_char == "=":
                self.token = Token(TokenType.NOT_EQUAL, position=self.token_position, value="!=")
                self.source.read_char()
            else:
                self.token = Token(TokenType.NOT, position=self.token_position, value="!")
        elif first_char == "=":
            self.source.read_char()
            second_char = self.source.character
            if second_char == "=":
                self.token = Token(TokenType.EQUAL, position=self.token_position, value="==")
                self.source.read_char()
            else:
                self.token = Token(TokenType.ASSIGN, position=self.token_position, value="=")
        elif first_char == "&":
            self.source.read_char()
            second_char = self.source.character
            if second_char == "&":
                self.token = Token(TokenType.AND, position=self.token_position, value="&&")
                self.source.read_char()
            else:
                is_recognized = False
        elif first_char == "|":
            self.source.read_char()
            second_char = self.source.character
            if second_char == "|":
                self.token = Token(TokenType.OR, position=self.token_position, value="||")
                self.source.read_char()
            else:
                is_recognized = False
        else:
            is_recognized = False

        return is_recognized



    def construct_number(self):

        if not self.source.character.isdigit():
            return False

        value = self.construct_integer()

        # constructing fraction
        frac = 0
        if self.source.character == ".":
            self.source.read_char()
            frac = self.build_fraction()

        self.token = Token(TokenType.NUMERIC_LITERAL, position=self.token_position, value=(value + frac))

        return True



    def construct_integer(self):

        if self.is_zero_integer():
            return 0

        return self.construct_non_zero_num()



    def is_zero_integer(self):

        is_zero = False

        if self.source.character == '0':
            self.source.read_char()
            if self.source.character.isdigit():
                # TODO: custom exception here
                raise Exception("Non-zero number can't contain anything after zero")
            else:
                is_zero = True

        return is_zero



    def construct_non_zero_num(self):

        value = 0
        while self.source.character.isdigit() and value < Token.MAX_NUMBER:

            value += 10 * value * (ord(self.source.character) - ord('0'))
            self.source.read_char()

        # Exceeded MAX_NUMBER
        if self.source.character.isdigit():
            raise Exception(self.token_position, f"Max allowed number value is {Token.MAX_VALUE}")

        return value




    def build_fraction(self):

        value = 0
        exponent = self.ignore_zeros() + 1

        while self.source.character.isdigit():
            value += (ord(self.source.character) - ord('0')) * pow(10, -exponent)
            exponent += 1
            self.source.read_char()

        return value




    def ignore_zeros(self):

        num_ignored = 0
        while self.source.character == '0':
            num_ignored += 1
            self.source.read_char()

        return num_ignored



    def construct_string_literal(self):

        if self.source.character != "\"":
            return False

        str_literal_value = ""
        self.source.read_char()

        while self.source.character != "\"":

            if self.source.character in [-1, "\n"]:
                # TODO: custom exception here
                raise Exception("Missing closing \"")

            str_literal_value += str(self.source.character)
            self.source.read_char()

        self.token = Token(TokenType.STRING_LITERAL, position=self.token_position, value=str_literal_value)
        self.source.read_char()

        return True




    def construct_identifier(self):
        pass



    def construct_keyword(self):
        pass



    def construct_comment(self):
        pass