from src.parser.parser import Parser
from src.scanner.scanner import Scanner

from src.data_source.file_source import FileSource
from src.data_source.string_source import StringSource
from src.utils.program3.expressions.math.add_expression import AddExpression
from src.utils.program3.expressions.math.and_expression import AndExpression
from src.utils.program3.expressions.math.equality_expression import EqualityExpression
from src.utils.program3.expressions.math.multiply_expression import MultiplyExpression
from src.utils.program3.expressions.math.or_expression import OrExpression
from src.utils.program3.expressions.math.relation_expression import RelationExpression
from src.utils.program3.expressions.math.unary_expression import UnaryExpression

from src.utils.program3.functions.function import Function
from src.utils.program3.classes._class import Class

from src.utils.program3.statements.conditional import Conditional
from src.utils.program3.statements.foreach_loop import ForeachLoop
from src.utils.program3.statements.while_loop import WhileLoop
from src.utils.program3.statements._return import Return
from src.utils.program3.statements.comment import Comment
from src.utils.program3.statements.reflect import Reflect
from src.utils.program3.statements.assign import Assign


from src.utils.program3.values.value_getter import ValueGetter

import io

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
            "class Person { define Person(name, age) {this.son.name = name; this.age = age;}}",
            "class Person { define Person(name, age) {this.name = name; this.age = age;}}",
            "class Pet {}"
        ]

        parsed_classes = []
        for program in programs:
            string_source = StringSource(io.StringIO(program))
            scanner = Scanner(string_source)
            parser = Parser(scanner=scanner)

            _class = parser.parse_class()
            parsed_classes.append(_class)

        print(_class)
        self.assertTrue(
            all(
                [isinstance(_class, Class) for _class in parsed_classes]
            )
        )



    # statements
    def test_parse_conditional(self):

        programs = [
            "if a > b { c = a + b; }",
            'if a == b { return "Equal";} else { return "Not equal";}'
            "if a > b { return a; } else if a < b { return b;} else { return b;}"
        ]
        parsed_ifs = []

        for program in programs:
            string_source = StringSource(io.StringIO(program))
            scanner = Scanner(string_source)
            parser = Parser(scanner=scanner)

            conditional = parser.parse_conditional_statement()
            parsed_ifs.append(conditional)

        self.assertTrue(
            all(
                [isinstance(conditional, Conditional) for conditional in parsed_ifs]
            )
        )



    def test_parse_foreach_loop(self):

        programs = [
            "foreach a in lst { print(a);}",
            "foreach a in make_squares([1, 2, 3]) {sum = sum + a; }",
        ]

        parsed_foreaches = []

        for program in programs:

            string_source = StringSource(io.StringIO(program))
            scanner = Scanner(string_source)
            parser = Parser(scanner=scanner)

            foreach = parser.parse_foreach_loop_statement()

            parsed_foreaches.append(foreach)

        self.assertTrue(
            all(
                [isinstance(foreach, ForeachLoop) for foreach in parsed_foreaches]
            )
        )


    def test_parse_while_loop(self):

        programs = [
            "while a < 10 { a = a + 1;}",
            "while is_prime(a) { print(a); }"
        ]

        parsed_whiles = []
        for program in programs:

            string_source = StringSource(io.StringIO(program))
            scanner = Scanner(string_source)
            parser = Parser(scanner=scanner)

            while_loop = parser.parse_while_loop_statement()
            parsed_whiles.append(while_loop)

        self.assertTrue(
            all([
                isinstance(while_loop, WhileLoop) for while_loop in parsed_whiles
            ])
        )



    def test_parse_return(self):

        programs = [
            "return a;",
            "return 2;",
            "return -1000;",
            'return "String Literal";',
            'return this.function.compute(123);'
        ]

        parsed_returns = []
        for program in programs:

            string_source = StringSource(io.StringIO(program))
            scanner = Scanner(string_source)
            parser = Parser(scanner=scanner)

            _return = parser.parse_return()
            parsed_returns.append(_return)

        self.assertTrue(
            all([
                isinstance(_return, Return) for _return in parsed_returns
            ])
        )



    def test_parse_comment(self):

        programs = [
            "#this is the comment",
            "# this is a \n# multiline comment"
        ]

        parsed_comments = []

        for program in programs:
            string_source = StringSource(io.StringIO(program))
            scanner = Scanner(string_source)
            parser = Parser(scanner=scanner)

            comment = parser.parse_comment_statement()
            parsed_comments.append(comment)

        self.assertTrue(
            all([isinstance(comment, Comment) for comment in parsed_comments])
        )


    def test_parse_reflect(self):

        programs = [
            "reflect father;",
            "reflect recursive mother;"
        ]

        parsed_reflects = []

        for program in programs:
            string_source = StringSource(io.StringIO(program))
            scanner = Scanner(string_source)
            parser = Parser(scanner=scanner)

            reflect = parser.parse_reflect_statement()
            parsed_reflects.append(reflect)

        self.assertTrue(
            all([isinstance(reflect, Reflect) for reflect in parsed_reflects])
        )




    def test_parse_assign(self):

        programs = [
            "a = make_squares(10, 20, 40);",
            "this.b.maker = make_squares(get_prime([1, 2, 3, 4, 5]));",
            "this.b.child = get_children(by_ref mother);"
        ]

        parsed_assign_statements = []

        for program in programs:
            string_source = StringSource(io.StringIO(program))
            scanner = Scanner(string_source)
            parser = Parser(scanner=scanner)

            assign_statement = parser.parse_assign_or_function_call()
            parsed_assign_statements.append(assign_statement)

        self.assertTrue(
            all([isinstance(assign, Assign) for assign in parsed_assign_statements])
        )

    def parse_function_call(self):

        programs = [
            "make_squares(10, 20, 40);",
            "make_squares(get_prime([1, 2, 3, 4, 5]));",
            "print_children(by_ref mother);"
        ]

        parsed_function_calls = []

        for program in programs:
            string_source = StringSource(io.StringIO(program))
            scanner = Scanner(string_source)
            parser = Parser(scanner=scanner)

            function_call = parser.parse_assign_or_function_call()
            parsed_function_calls.append(function_call)

        self.assertTrue(
            all([isinstance(function_call, ValueGetter) for function_call in parsed_function_calls])
        )


    def test_parse_or_expression(self):

        programs = [
            "true || false;",
            "1 || 2;",
        ]

        parsed_or_expressions = []

        for program in programs:
            string_source = StringSource(io.StringIO(program))
            scanner = Scanner(string_source)
            parser = Parser(scanner=scanner)

            or_expression = parser.parse_or_expression()
            parsed_or_expressions.append(or_expression)


        self.assertTrue(
            all([isinstance(or_expression, OrExpression) for or_expression in parsed_or_expressions])
        )




    def test_parse_and_expression(self):

        programs = [
            "true && false;",
            "is_good(a) && !is_bad(a);",
        ]

        parsed_and_expressions = []

        for program in programs:
            string_source = StringSource(io.StringIO(program))
            scanner = Scanner(string_source)
            parser = Parser(scanner=scanner)

            and_expression = parser.parse_and_expression()
            parsed_and_expressions.append(and_expression)

        self.assertTrue(
            all([isinstance(and_expression, AndExpression) for and_expression in parsed_and_expressions])
        )




    def test_parse_eq_expression(self):

        programs = [
            "true == false;",
            "1 * 10 == 20 / 2;",
        ]

        parsed_eq_expressions = []

        for program in programs:
            string_source = StringSource(io.StringIO(program))
            scanner = Scanner(string_source)
            parser = Parser(scanner=scanner)

            eq_expression = parser.parse_eq_expression()
            parsed_eq_expressions.append(eq_expression)

        self.assertTrue(
            all([isinstance(eq_expression, EqualityExpression) for eq_expression in parsed_eq_expressions])
        )



    def test_parse_rel_expression(self):

        programs = [
            "10 > 20;",
            "10 * 2 + 12 <= 20001;",
        ]

        parsed_rel_expressions = []

        for program in programs:
            string_source = StringSource(io.StringIO(program))
            scanner = Scanner(string_source)
            parser = Parser(scanner=scanner)

            rel_expression = parser.parse_rel_expression()
            parsed_rel_expressions.append(rel_expression)


        self.assertTrue(
            all([isinstance(rel_expression, RelationExpression) for rel_expression in parsed_rel_expressions])
        )



    def test_parse_add_expression(self):

        programs = [
            "12 + 13;",
            "12 * 3 + 14 + 15 * 3;",
        ]

        parsed_add_expressions = []

        for program in programs:
            string_source = StringSource(io.StringIO(program))
            scanner = Scanner(string_source)
            parser = Parser(scanner=scanner)

            add_expression = parser.parse_add_expression()
            parsed_add_expressions.append(add_expression)

        self.assertTrue(
            all([isinstance(add_expression, AddExpression) for add_expression in parsed_add_expressions])
        )



    def test_parse_mul_expression(self):

        programs = [
            "factorial(9) * 10;",
            "fibonacci(5) * (-13) * 15;",
        ]

        parsed_mul_expressions = []

        for program in programs:
            string_source = StringSource(io.StringIO(program))
            scanner = Scanner(string_source)
            parser = Parser(scanner=scanner)

            mul_expression = parser.parse_mul_expression()
            parsed_mul_expressions.append(mul_expression)

        self.assertTrue(
            all([isinstance(mul_expression, MultiplyExpression) for mul_expression in parsed_mul_expressions])
        )


    def test_parse_unary_expression(self):

        # negative unary expression
        # not unary expression
        # general value

        programs = [
            "-15;",
            "!(is_prime(a));",
            "(true && false)"
        ]

        parsed_unary_expressions = []

        for program in programs:

            string_source = StringSource(io.StringIO(program))
            scanner = Scanner(string_source)
            parser = Parser(scanner=scanner)

            unary_expression = parser.parse_unary_expression()
            parsed_unary_expressions.append(unary_expression)

        self.assertTrue(
            all([isinstance(unary_expr, UnaryExpression) for unary_expr in parsed_unary_expressions])
        )