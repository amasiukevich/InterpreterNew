from src.parser.parser import Parser
from src.scanner.scanner import Scanner

from src.data_source.file_source import FileSource
from src.data_source.string_source import StringSource

import io
import os

import unittest

class TestParser(unittest.TestCase):


    def test_function_creation(self):

        string_stream = io.StringIO("define main(a, b) {}")

        string_source = StringSource(string_stream)
        scanner = Scanner(string_source)

        parser = Parser(scanner=scanner)
        parser.parse_program()


    def test_class_creation(self):

        string_stream = io.StringIO(
            "class Person {} define main() { return a + b;}"
        )

        string_source = StringSource(string_stream)
        scanner = Scanner(string_source)
        parser = Parser(scanner=scanner)

        parser.parse_program()