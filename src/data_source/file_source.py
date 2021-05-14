from .base_source import BaseSource
from src.utils.position import Position

import io

class FileSource(BaseSource):

    def __init__(self, file_stream):

        # 'cause someone should close it
        self.reader = file_stream
        self.position = Position(line=1, column=0)
        self.read_char()


    def read_char(self):
        char = self.reader.read(1)
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


    def get_curr_char(self):
        return self.character

    def close(self):
        self.reader.close()


    def next(self):
        pass


    def peek(self):
        pass