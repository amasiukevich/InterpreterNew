from src.utils.token import Token
from src.utils.token_type import TokenType
from src.utils.position import Position

"""
    Author: Anton Masiukevich
    Github: https://github.com/amasiukevich
"""


class ParsingException(Exception):

    def __init__(self, token: Token, token_type: TokenType, msg=""):

        if msg:
            self.msg = msg
        else:
            message = f"Token type {token.token_type} expected, got {token_type}"
            self.msg = f"At line: {token.position.line}: {message}"

        super().__init__(self.msg)