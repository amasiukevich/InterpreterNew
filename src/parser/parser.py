from src.exceptions.parsing_exception import ParsingException
from src.scanner.scanner import Scanner
from src.utils.program3.values.basic_value_getter import BasicValueGetter
from src.utils.program3.values.this_value_getter import ThisValueGetter

from src.utils.token_type import TokenType

from src.utils.program3.program import Program
from src.utils.program3.block import Block

from src.utils.program3.functions.function import Function
from src.utils.program3.functions.parameters import Parameters
from src.utils.program3.functions.arguments import Arguments
from src.utils.program3.functions.argument import Argument

from src.utils.program3.classes._class import Class
from src.utils.program3.classes.class_block import ClassBlock

from src.utils.program3.statements.assign import Assign
from src.utils.program3.statements.comment import Comment
from src.utils.program3.statements.conditional import Conditional
from src.utils.program3.statements.foreach_loop import ForeachLoop
from src.utils.program3.statements.reflect import Reflect
from src.utils.program3.statements.rest_function_call import RestFunctionCall
from src.utils.program3.statements._return import Return
from src.utils.program3.statements.while_loop import WhileLoop

from src.utils.program3.expressions.math.add_expression import AddExpression
from src.utils.program3.expressions.math.and_expression import AndExpression
from src.utils.program3.expressions.math.equality_expression import EqualityExpression
from src.utils.program3.expressions.math.multiply_expression import MultiplyExpression
from src.utils.program3.expressions.math.or_expression import OrExpression
from src.utils.program3.expressions.math.relation_expression import RelationExpression
from src.utils.program3.expressions.math.unary_expression import UnaryExpression
from src.utils.program3.expressions.math.negative_unary_expression import NegativeUnaryExpression
from src.utils.program3.expressions.math.not_unary_expression import NotUnaryExpression

from src.utils.program3.expressions.operators.oper_mapper import OperatorMapper

from src.utils.program3.values.list_value import ListValue
from src.utils.program3.values.value_getter import ValueGetter
from src.utils.program3.values.literals.int_literal import IntLiteral
from src.utils.program3.values.literals.float_literal import FloatLiteral
from src.utils.program3.values.literals.bool_literal import BoolLiteral
from src.utils.program3.values.literals.string_literal import StringLiteral


import numpy as np


class Parser:

    def __init__(self, scanner: Scanner):

        self.scanner = scanner
        self.scanner.next_token()
        self.token = scanner.token

        self.oper_mapper = OperatorMapper()



    def parse_program(self):

        functions = {}
        classes = {}

        while self.scanner.token.token_type != TokenType.EOF:

            function = self.parse_function()
            _class = self.parse_class()

            if function:
                functions[function.identifier] = function

            if _class:
                classes[_class.identifier] = _class

        program = Program(functions, classes)

        return program




    def parse_function(self):

        if self.compare_and_consume(TokenType.DEFINE):
            self.check_current_token(TokenType.IDENTIFIER)
            identifier = self.scanner.get_token_and_move()

            self.must_be_token(TokenType.OPEN_PARENTHESIS)

            parameters = self.parse_params()

            self.must_be_token(TokenType.CLOSING_PARENTHESIS)

            block = self.parse_block()

            function_clause = Function(identifier.value, parameters, block)

            return function_clause


    def parse_class(self):

        if self.compare_and_consume(TokenType.CLASS):

            self.compare_token_types(TokenType.IDENTIFIER)
            identifier = self.scanner.get_token_and_move()

            # class block
            block = self.parse_class_block()

            class_clause = Class(identifier.value, block)

            return class_clause


    def parse_params(self):

        param_names = []
        if self.compare_token_types(TokenType.IDENTIFIER):

            identifier = self.scanner.get_token_and_move()

            param_names.append(identifier.value)

            while self.compare_and_consume(TokenType.COMMA):

                self.check_current_token(TokenType.IDENTIFIER)
                identifier = self.scanner.get_token_and_move()
                param_names.append(identifier.value)

            params = Parameters(param_names)

            return params



    def parse_block(self):

        if self.compare_and_consume(TokenType.OPEN_CURLY_BRACKET):

            statements = []

            # parse statements
            statement = self.parse_statement()

            while statement:
                statements.append(statement)
                statement = self.parse_statement()

            self.must_be_token(TokenType.CLOSING_CURLY_BRACKET)

            block = Block(statements=[])

            return block



    def parse_class_block(self):

        if self.compare_and_consume(TokenType.OPEN_CURLY_BRACKET):

            methods = []

            # parsing methods
            method = self.parse_function()

            while method:
                methods.append(method)
                method = self.parse_function()

            self.must_be_token(TokenType.CLOSING_CURLY_BRACKET)

            class_block = ClassBlock(methods)

            return class_block



    def parse_statement(self):

        # TODO: write it better
        # statement = None

        # parse conditional
        statement = self.parse_conditional_statement()
        if statement:
            return statement

        # parse while loop
        statement = self.parse_while_loop_statement()
        if statement:
            return statement

        # parse foreach loop
        statement = self.parse_foreach_loop_statement()
        if statement:
            return statement

        # parse return
        statement = self.parse_return()
        if statement:
            return statement

        # parse comment
        statement = self.parse_comment_statement()
        if statement:
            return statement


        # parse reflect
        statement = self.parse_reflect_statement()
        if statement:
            return statement


        # parse function_call or assign
        statement = self.parse_assign_or_function_call()
        if statement:
            return statement


    def parse_conditional_statement(self):

        if self.compare_and_consume(TokenType.IF):

            conditions = []
            blocks = []

            or_expression = self.parse_or_expression()

            if_block = self.parse_block()
            conditions.append(or_expression)
            blocks.append(if_block)

            # contains ELSE clause
            if self.compare_and_consume(TokenType.ELSE):

                while self.compare_and_consume(TokenType.IF):

                    # else if stuff
                    or_expression = self.parse_or_expression()

                    else_if_block = self.parse_block()

                    conditions.append(or_expression)
                    blocks.append(else_if_block)

                # else stuff
                else_block = self.parse_block()
                blocks.append(else_block)

            return Conditional(conditions, blocks)



    def parse_foreach_loop_statement(self):

        if self.compare_and_consume(TokenType.FOREACH):

            # Identifier
            self.check_current_token(TokenType.IDENTIFIER)
            identifier = self.scanner.get_token_and_move()

            # In
            self.must_be_token(TokenType.IN)

            # or_expression
            or_expression = self.parse_or_expression()

            # block
            block = self.parse_block()

            return ForeachLoop(identifier, or_expression, block)


    def parse_while_loop_statement(self):

        if self.compare_and_consume(TokenType.WHILE):
            # Expression
            or_expression = self.parse_or_expression()

            # block
            block = self.parse_block()

            while_loop = WhileLoop(or_expression, block)

            return while_loop


    def parse_return(self):

        if self.compare_and_consume(TokenType.RETURN):

            or_expression = self.parse_or_expression()

            if not or_expression:
                raise ParsingException(token=self.scanner.token, msg="Missing value to return")

            self.must_be_token(TokenType.SEMICOLON)

            return_statement = Return(or_expression)

            return return_statement



    def parse_reflect_statement(self):

        if self.compare_and_consume(TokenType.REFLECT):

            is_recursive = False

            # may be recursive
            if self.compare_and_consume(TokenType.RECURSIVE):
                is_recursive = True

            # or_expression
            or_expression = self.parse_or_expression()

            # semicolon
            self.must_be_token(TokenType.SEMICOLON)

            reflect = Reflect(or_expression, is_recursive)

            return reflect



    def parse_comment_statement(self):

        if self.compare_token_types(TokenType.COMMENT):

            token = self.scanner.get_token_and_move()
            comment = Comment(token.value)

            return comment



    def parse_assign_or_function_call(self):

        # left_part
        value_getter = self.parse_value_getter()


        # =
        if self.compare_and_consume(TokenType.ASSIGN):
            # assign statement

            # or_expression
            or_expression = self.parse_or_expression()
            self.must_be_token(TokenType.SEMICOLON)

            assign_statement = Assign(value_getter, or_expression)

            return assign_statement

        elif self.compare_and_consume(TokenType.SEMICOLON):
            # function call here
            return value_getter


    def parse_value_getter(self):

        full_base_getters = []
        if self.compare_and_consume(TokenType.THIS):

            full_base_getters.append(ThisValueGetter())
            self.must_be_token(TokenType.ACCESS)

        base_getters = self.parse_base_getters()

        if base_getters:
            full_base_getters += base_getters

        if full_base_getters:
            return ValueGetter(full_base_getters)


    def parse_base_getters(self):


        # Access operators
        base_getter = self.parse_basic_value_getter()

        if base_getter:

            base_getters = []

            base_getters.append(base_getter)

            while self.compare_and_consume(TokenType.ACCESS):

                base_getter = self.parse_basic_value_getter()
                base_getters.append(base_getter)


            return base_getters



    def parse_basic_value_getter(self):

        slicing_expr = None

        if self.compare_token_types(TokenType.IDENTIFIER):

            id_token = self.scanner.get_token_and_move()

            rest_call = self.parse_rest_function_call()


            # brackets here
            if self.compare_and_consume(TokenType.OPEN_BRACKET):
                slicing_expr = self.parse_add_expression()

                self.must_be_token(TokenType.CLOSING_BRACKET)

            base_getter = BasicValueGetter(id_token.value, rest_call, slicing_expr)

            return base_getter


    def parse_rest_function_call(self):

        prev_token = self.scanner.token

        if self.compare_and_consume(TokenType.OPEN_PARENTHESIS):

            a = self.scanner.token
            arguments = self.parse_arguments()

            self.must_be_token(TokenType.CLOSING_PARENTHESIS)
            rest_function_call = RestFunctionCall(arguments)

            return rest_function_call



    def parse_arguments(self):

        list_of_args = []

        argument = self.parse_argument()
        if argument:

            list_of_args.append(argument)

            while self.compare_and_consume(TokenType.COMMA):

                argument = self.parse_argument()
                list_of_args.append(argument)

        arguments = Arguments(list_of_args)

        return arguments



    def parse_argument(self):

        is_by_ref = False

        # by ref
        if self.compare_and_consume(TokenType.BY_REF):
            is_by_ref = True

        # argument
        or_expression = self.parse_or_expression()

        argument = Argument(or_expression, is_by_ref)

        return argument



    def parse_or_expression(self):

        component_expressions = []

        and_expression = self.parse_and_expression()
        if and_expression:

            component_expressions.append(and_expression)
            while self.compare_and_consume(TokenType.OR):
                and_expression = self.parse_and_expression()

                if not and_expression:
                    raise Exception("Error while parsing OR expression")
                component_expressions.append(and_expression)
        if len(component_expressions) == 1:
            return and_expression

        return OrExpression(component_expressions)



    def parse_and_expression(self):

        component_expressions = []

        eq_expression = self.parse_eq_expression()
        if eq_expression:
            component_expressions.append(eq_expression)

            while self.compare_and_consume(TokenType.AND):

                eq_expression = self.parse_eq_expression()
                if not eq_expression:
                    raise Exception("Error while parsing AND expression")

                component_expressions.append(eq_expression)
        if len(component_expressions) == 1:
            return eq_expression

        return AndExpression(component_expressions)



    def parse_eq_expression(self):

        component_expressions = []

        operators = []

        rel_expression = self.parse_rel_expression()
        if rel_expression:
            component_expressions.append(rel_expression)

            while self.is_equality_token(self.scanner.token.token_type):

                operators.append(self.parse_operator())
                rel_expression = self.parse_rel_expression()

                if not rel_expression:
                    raise Exception("Error while parsing EQUALITY expression")

                component_expressions.append(rel_expression)
        if len(component_expressions) == 1:
            return rel_expression

        return EqualityExpression(component_expressions, operators)


    def is_equality_token(self, token_type):
        return  token_type == TokenType.EQUAL or \
                token_type == TokenType.NOT_EQUAL



    def parse_rel_expression(self):

        component_expressions = []

        operators = []

        add_expression = self.parse_add_expression()

        if add_expression:
            component_expressions.append(add_expression)

            while self.is_relation_token(self.scanner.token.token_type):

                operator = self.parse_operator()
                operators.append(operator)

                add_expression = self.parse_rel_expression()

                if not add_expression:
                    raise Exception("Error while parsing RELATION expression")

                component_expressions.append(add_expression)

        if len(component_expressions) == 1:
            return add_expression

        return RelationExpression(component_expressions, operators)



    def is_relation_token(self, token_type):
        return  token_type == TokenType.GREATER or \
                token_type == TokenType.GREATER_EQUAL or \
                token_type == TokenType.LESS_EQUAL or \
                token_type == TokenType.LESS



    def parse_add_expression(self):

        component_expressions = []

        operators = []

        mult_expression = self.parse_mul_expression()

        if mult_expression:
            component_expressions.append(mult_expression)

        while self.is_add_token(self.scanner.token.token_type):


            operator = self.parse_operator()
            operators.append(operator)

            mult_expression = self.parse_mul_expression()

            if not mult_expression:
                raise Exception("Error while parsing ADD expression")


            component_expressions.append(mult_expression)

        if len(component_expressions) == 1:
            return mult_expression

        return AddExpression(component_expressions, operators)



    def is_add_token(self, token_type):
        return  token_type == TokenType.PLUS or \
                token_type == TokenType.MINUS



    def parse_mul_expression(self):

        component_expressions = []

        operators = []

        unary_expression = self.parse_unary_expression()

        if unary_expression:
            component_expressions.append(unary_expression)

        while self.is_mult_token(self.scanner.token.token_type):

            operator = self.parse_operator()
            operators.append(operator)

            unary_expression = self.parse_unary_expression()

            if not unary_expression:
                raise Exception("Error while parsing MULTIPLY expression")
            component_expressions.append(unary_expression)

        if len(component_expressions) == 1:
            return unary_expression

        return MultiplyExpression(component_expressions, operators)



    def is_mult_token(self, token_type):

        return  token_type == TokenType.MULTIPLY or \
                token_type == TokenType.DIVIDE  or \
                token_type == TokenType.MODULO



    def parse_unary_expression(self):


        not_unary_expression = self.parse_not_unary_expression()
        if not_unary_expression:
            return UnaryExpression(not_unary_expression)

        negative_unary_expression = self.parse_negative_unary_expression()
        if negative_unary_expression:
            return UnaryExpression(negative_unary_expression)

        general_value = self.parse_general_value()
        if general_value:
            return UnaryExpression(general_value)



    def parse_not_unary_expression(self):

        if self.compare_and_consume(TokenType.NOT):

            unary_expression = self.parse_unary_expression()
            not_unary_expression = NotUnaryExpression(unary_expression)

            return not_unary_expression



    def parse_negative_unary_expression(self):

        if self.compare_and_consume(TokenType.MINUS):

            unary_expression = self.parse_unary_expression()
            neg_unary_expression = NegativeUnaryExpression(unary_expression)

            return neg_unary_expression



    def parse_general_value(self):

        if self.compare_and_consume(TokenType.OPEN_PARENTHESIS):

            or_expression = self.parse_or_expression()

            self.must_be_token(TokenType.CLOSING_PARENTHESIS)

            return or_expression

        else:
            return self.parse_value()



    def parse_operator(self):

        token_type = self.scanner.token.token_type

        operator = self.oper_mapper.TOKEN_TYPE_TO_OPER.get(token_type)
        if operator:
            self.scanner.next_token()
            return operator
        else:
            raise Exception("Unknown operator")



    def parse_value(self):

        token = self.scanner.token
        value = None

        # literal value
        if self.is_literal(token.token_type):
            value = self.token_to_literal(token)
        # list_value
        elif self.compare_and_consume(TokenType.OPEN_BRACKET):

            list_value = self.parse_list_value()

            self.must_be_token(TokenType.CLOSING_BRACKET)

            value = list_value

        # value_getter
        elif self.compare_token_types(TokenType.IDENTIFIER) or self.compare_token_types(TokenType.THIS):

            value_getter = self.parse_value_getter()
            value = value_getter

        return value



    def parse_list_value(self):

        component_values = []
        or_expression = self.parse_or_expression()

        if or_expression:
            component_values.append(or_expression)

        while self.compare_and_consume(TokenType.COMMA):

            or_expression = self.parse_or_expression()

            if not or_expression:
                raise Exception("Wrong expression in the list")

            component_values.append(or_expression)

        return ListValue(component_values)



    def token_to_literal(self, token):

        literal = None
        if token.token_type == TokenType.NUMERIC_LITERAL:
            if isinstance(token.value, int):
                literal = IntLiteral(token.value)
            elif isinstance(token.value, float):
                literal = FloatLiteral(token.value)
        elif token.token_type == TokenType.STRING_LITERAL:
            literal = StringLiteral(token.value[1:-1])
        elif token.token_type == TokenType.BOOL_LITERAL:
            literal = BoolLiteral(token.value)
        else:
            raise Exception(f"Unknown type of literal\n{token}\n")

        self.scanner.next_token()
        return literal



    def is_literal(self, token_type):
        return token_type == TokenType.NUMERIC_LITERAL or \
               token_type == TokenType.STRING_LITERAL or \
               token_type == TokenType.BOOL_LITERAL



    def check_current_token(self, token_type: TokenType):

        token = self.scanner.token
        if not self.compare_token_types(token_type):
            raise ParsingException(token=token, token_type=token_type, msg=f"Expected {token.token_type}, got {token_type}")



    def compare_token_types(self, token_type: TokenType):
        return self.scanner.token.token_type == token_type



    def compare_and_consume(self, token_type: TokenType):

        result = self.compare_token_types(token_type)
        if result:
            self.scanner.next_token()

        return result



    # TODO: info in the exception: Missing 'something' to build 'something'
    def must_be_token(self, token_type: TokenType):
        self.check_current_token(token_type)
        self.scanner.next_token()