from src.data_source.file_source import FileSource
from src.utils.position import Position

from time import sleep

import io
import os

import unittest


class TestFileSource(unittest.TestCase):

    def test_position_advance(self):

        file_stream = io.open(
            os.path.abspath("../../lang_codes/testing/test_arithmetic")
        )

        file_source = FileSource(file_stream)

        while file_source.character != -1:
            file_source.read_char()

        file_stream.close()

        pos2 = Position(line=2, column=5)
        self.assertEqual(file_source.position, pos2, f"Positions are not equal\npos1: {repr(file_source.position)}\npos2: {repr(pos2)}")

    def test_some_text(self):

        file_stream = io.open(
            os.path.abspath("../../lang_codes/real_codes/tiny_arithmetic.txt")
        )

        file_source = FileSource(file_stream)
        file_source.read_char()

        chars = []
        while file_source.character != -1:
            chars.append(file_source.get_curr_char())
            file_source.read_char()

        file_stream.close()
        real_chars = [c for c in  "define add(a, b) {\n    return a + b;\n}"]
        self.assertListEqual(chars, real_chars, "Read chars aren't equal")

