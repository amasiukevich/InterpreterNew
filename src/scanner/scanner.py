from .keyword_mapper import KeywordMapper
from ..data_source.base_source import BaseSource
from ..exceptions.scanning_exception import ScanningException
from ..utils.token import Token
from ..utils.token_type import TokenType

from ..exceptions.scanner_exception import ScannerException


class Scanner():



    def __init__(self, source):

        if not isinstance(source, BaseSource):
            raise ScannerException(msg="The given source is not an instance of BaseSource")

        self.source = source
        self.kw_mapper = KeywordMapper()
        self.token = Token(TokenType.UNKNOWN)

        # for keywords and identifiers
        self.tmp_kw_id = ""
        self.tmp_kw_len = 0



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
            return
        elif self.construct_comment():
            return
        elif self.construct_keyword():
            return

        else:
            self.token = Token(TokenType.UNKNOWN, position=self.token_position)
            raise ScanningException(self.token_position, "Unknown symbol")

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
                raise ScanningException(
                    position=self.token_position,
                    msg="Non-zero number can't contain anything after zero"
                )
            else:
                is_zero = True

        return is_zero



    def construct_non_zero_num(self):

        value = 0
        while self.source.character.isdigit() and value < Token.MAX_NUMBER:

            value = value * 10 + (ord(self.source.character) - ord('0'))

            # value += 10 * value * (ord(self.source.character) - ord('0'))
            self.source.read_char()

        # Exceeded MAX_NUMBER
        if self.source.character.isdigit():
            raise ScanningException(self.token_position, f"Max allowed number value is {Token.MAX_NUMBER}")

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
                raise ScanningException(self.token_position, "Missing closing \"")

            str_literal_value += str(self.source.character)
            self.source.read_char()

        self.token = Token(TokenType.STRING_LITERAL, position=self.token_position, value=str_literal_value)
        self.source.read_char()

        return True




    def construct_identifier(self):

        self.tmp_kw_id = ""
        self.tmp_kw_len = 0

        if self.is_begin_valid():

            while self.is_valid_part() and self.tmp_kw_len < Token.MAX_IDENTIFIER_LENGHT:

                self.tmp_kw_id += self.source.character
                self.tmp_kw_len += 1
                self.source.read_char()

            if self.is_valid_part():
                raise ScanningException(
                    self.token_position,
                    "Exceeded length of the identifier"
                )

            if self.construct_keyword():
                return True

            self.token = Token(TokenType.IDENTIFIER, position=self.token_position, value=str(self.tmp_kw_id))
            return True

        else:
            return False


    def is_begin_valid(self):

        # for keywords and identifiers

        if self.source.character.isalpha():

            self.tmp_kw_id += self.source.character
            self.tmp_kw_len += 1
            self.source.read_char()

            return True

        # for identifiers only
        elif self.source.character in ["$", "_"]:

            self.tmp_kw_id += self.source.character
            self.source.read_char()

            if self.is_valid_part():

                self.tmp_kw_id += self.source.character
                self.source.read_char()
                self.tmp_len += 2

                return True
            else:
                raise ScanningException(self.token_position, msg="Invalid identifier")
        else:
            return False



    def is_valid_part(self):
        return isinstance(self.source.character, str) and (self.source.character.isalnum() or self.source.character == "_")



    def construct_keyword(self):

        tmp_keyword_name = self.kw_mapper.KEYWORD_MAP.get(self.tmp_kw_id)
        if tmp_keyword_name:
            self.token = Token(token_type=tmp_keyword_name, position=self.token_position, value=str(self.tmp_kw_id))

        return bool(tmp_keyword_name)



    def construct_comment(self):

        is_recognized = self.source.character == "#"

        if is_recognized:
            comment_value = ""
            # all of the character until the end of the line or EOF skipping and adding to the commented
            while self.source.character not in ["\n", -1]:
                comment_value += self.source.character
                self.source.read_char()
            self.token = Token(TokenType.COMMENT, position=self.token_position, value=comment_value)
        return is_recognized