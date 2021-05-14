from .token_type import TokenType
from .position import Position

class Token:

    SPECIAL_CHARS = [';', '"', '\'', '-', '.', ',', '/', '\\', '_', '$', ' ']
    MAX_IDENTIFIER_LENGHT = 120
    MAX_NUMBER = 2**32

    def __init__(self, token_type, position=None, value=None):

        self.token_type = token_type
        self.position = position
        self.value = value


    def __eq__(self, other):
        if not isinstance(other, Token):
            return False
        else:
            return self.token_type == other.token_type and self.position == other.position


    def __repr__(self):
        return f"Type: {self.token_type}\n" \
               f"Position: {self.position}\n" \
               f"Value: {self.value}\n"