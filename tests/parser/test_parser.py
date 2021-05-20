from src.parser.parser import Parser
from src.scanner.scanner import Scanner

from src.data_source.file_source import FileSource
from src.data_source.string_source import StringSource


from src.utils.program3.functions.function import Function
from src.utils.program3.classes._class import Class

import io
import os

import unittest

class TestParser(unittest.TestCase):


    def test_program1(self):

        string_stream = io.StringIO("define main(a, b) {}")

        string_source = StringSource(string_stream)
        scanner = Scanner(string_source)

        parser = Parser(scanner=scanner)
        parser.parse_program()



    def test_program2(self):

        string_stream = io.StringIO(
            "class Person {} define main() { return a + b;}"
        )

        string_source = StringSource(string_stream)
        scanner = Scanner(string_source)
        parser = Parser(scanner=scanner)

        parser.parse_program()



    def test_function_creation(self):

        programs = [
            "define main() {}",
            "define add(a, b) { return a + b;}"
        ]

        parsed_functions = []
        for program in programs:

            string_source = StringSource(io.StringIO(program))
            scanner = Scanner(string_source)
            parser = Parser(scanner=scanner)

            function = parser.parse_function()
            parsed_functions.append(function)

        print(parsed_functions[1])

        self.assertTrue(
            all(
                [isinstance(parsed_functions[i], Function) for i in range(len(parsed_functions))]
            ),
            "Not all functions parsed"
        )



    def test_class_creation(self):

        programs = [
            # "class Person { define Person(name, age) {this.son.name = name; this.age = age;}}",
            "class Person { define Person(name, age) {this.name = name; this.age = age;}}",
            #"class Pet {}"
        ]

        parsed_classes = []
        for program in programs:
            string_source = StringSource(io.StringIO(program))
            scanner = Scanner(string_source)
            parser = Parser(scanner=scanner)

            _class = parser.parse_class()

        print(_class)
        self.assertTrue(
            all(
                [isinstance(_class, Class) for _class in parsed_classes]
            )
        )



    # statements
    def test_parse_conditional(self):
        pass


    def test_parse_foreach_loop(self):
        pass


    def test_parse_while_loop(self):
        pass


    def test_parse_return(self):
        pass


    def test_parse_comment(self):
        pass


    def test_parse_reflect(self):
        # reflect and reflect_recursive here
        pass


    def test_parse_function_call(self):
        pass



    def test_parse_assign(self):
        pass



    def test_parse_or_expression(self):
        pass



    def test_parse_and_expression(self):
        pass


    def test_parse_eq_expression(self):
        pass



    def test_parse_rel_expression(self):
        pass



    def test_parse_add_expression(self):
        pass




    def test_parse_mul_expression(self):
        pass


    def test_parse_unary_expression(self):
        pass