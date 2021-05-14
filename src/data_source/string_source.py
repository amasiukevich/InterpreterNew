from ..utils.position import Position
from .base_source import BaseSource


class StringSource(BaseSource):


    def __init__(self, string_stream):

        self.string_stream = string_stream
        self.position = Position(line=1, column=0)
        self.read_char()

    def read_char(self):

        char = self.string_stream.read(1)

        # TODO: move advance_position method to the BaseSource class
        if char:
            self.advance_position(char)
            self.character = char

        else:
            self.character = -1



    def advance_position(self, char):

        if char == "\n":
            self.position.advance_line()
        else:
            self.position.advance_column()

    def close(self):
        self.string_stream.close()

    def get_curr_char(self):
        pass

    def next(self):
        pass


    def peek(self):
        pass