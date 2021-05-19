from src.exceptions.parser_exceptions.parser_exception import ParserException
from src.scanner.scanner import Scanner
from src.utils.program3.values.basic_value_getter import BasicValueGetter
from src.utils.program3.values.collection_element import CollectionElement

from src.utils.token_type import TokenType
from src.utils.program3.program import Program
from src.utils.program3.block import Block
from src.utils.program3.complex_identifier import ComplexIdentifier

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
from src.utils.program3.statements.function_call import FunctionCall
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

        if not program.functions_unique():
            raise ParserException(self.scanner.token_position, "There are duplicates in functions names")
        if not program.classes_unique():
            raise ParserException(self.scanner.token_position, "There are duplicates in classes names")
        if not program.function_exists("main"):
            raise ParserException(self.scanner.token_position, "There is no function main")

        return program


    def parse_function(self):

        function_clause = None
        if self.compare_token_types(TokenType.DEFINE):
            self.scanner.next_token()

            self.check_current_token(TokenType.IDENTIFIER)
            identifier = self.scanner.get_token_and_move()

            self.check_current_token(TokenType.OPEN_PARENTHESIS)
            self.scanner.next_token()


            parameters = self.parse_params()

            self.check_current_token(TokenType.CLOSING_PARENTHESIS)
            self.scanner.next_token()


            block = self.parse_block()


            function_clause = Function(identifier.value, parameters, block)
            self.scanner.next_token()


        return function_clause


    def parse_class(self):

        class_clause = None
        if self.compare_token_types(TokenType.CLASS):

            self.scanner.next_token()
            self.compare_token_types(TokenType.IDENTIFIER)
            identifier = self.scanner.get_token_and_move()

            # class block
            block = self.parse_class_block()

            class_clause = Class(identifier.value, block)

        return class_clause



    def parse_params(self):

        params = Parameters()
        self.check_current_token(TokenType.IDENTIFIER)
        identifier = self.scanner.get_token_and_move()

        params.add_parameter(identifier.value)


        while self.compare_token_types(TokenType.COMMA):

            self.scanner.next_token()
            self.check_current_token(TokenType.IDENTIFIER)
            identifier = self.scanner.get_token_and_move()

            params.add_parameter(identifier.value)

        return params



    def parse_block(self):

        self.compare_token_types(TokenType.OPEN_CURLY_BRACKET)
        # token = self.scanner.get_token_and_move()

        self.scanner.next_token()

        block = Block()

        # parse statements
        statement = self.parse_statement()

        while statement:
            block.add_statement(statement)
            statement = self.parse_statement()

        self.check_current_token(TokenType.CLOSING_CURLY_BRACKET)
        self.scanner.next_token()

        return block



    def parse_class_block(self):

        self.compare_token_types(TokenType.OPEN_CURLY_BRACKET)
        self.scanner.next_token()

        class_block = ClassBlock()

        # parsing methods
        method = self.parse_function()
        while method:
            class_block.add_method(method)

        self.check_current_token(TokenType.CLOSING_CURLY_BRACKET)
        self.scanner.next_token()

        return class_block



    def parse_statement(self):

        # TODO: write it better
        statement = None

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

        # parse function_call
        statement = self.parse_function_call()
        if statement:
            return statement

        # parse assign
        statement = self.parse_assign_statement()
        if statement:
            return statement

        # parse built-in functions

        statement = self.parse_built_in_function()
        if statement:
            return statement

        return statement


    def parse_conditional_statement(self):

        conditional = None
        if (self.compare_token_types(TokenType.IF)):

            conditions = []
            blocks = []

            self.scanner.next_token()
            or_expression = self.parse_or_expression()
            self.scanner.next_token()

            if_block = self.parse_block()
            conditions.append(or_expression)
            blocks.append(if_block)

            # contains ELSE clause
            if self.compare_token_types(TokenType.ELSE):

                self.scanner.next_token()
                while self.compare_token_types(TokenType.IF):

                    # else if stuff
                    self.scanner.next_token()
                    or_expression = self.parse_or_expression()
                    self.scanner.next_token()
                    else_if_block = self.parse_block()

                    conditions.append(or_expression)
                    blocks.append(else_if_block)


                # else stuff
                else_block = self.parse_block()
                blocks.append(else_block)

            conditional = Conditional(conditions, blocks)

        return conditional



    def parse_foreach_loop_statement(self):

        foreach_loop = None
        if self.compare_token_types(TokenType.FOREACH):

            self.scanner.next_token()
            # Identifier
            self.check_current_token(TokenType.IDENTIFIER)
            identifier = self.scanner.get_token_and_move()

            # In
            self.check_current_token(TokenType.IN)
            self.scanner.next_token()


            # or_expression
            or_expression = self.parse_or_expression()

            # block
            block = self.parse_block()

            foreach = ForeachLoop(identifier, or_expression, block)

        return foreach_loop


    def parse_while_loop_statement(self):

        while_loop = None
        if self.compare_token_types(TokenType.WHILE):
            self.scanner.next_token()

            # Expression
            or_expression = self.parse_or_expression()

            # block
            block = self.parse_block()

            while_loop = WhileLoop(or_expression, block)

        return while_loop


    def parse_return(self):

        return_statement = None
        if (self.compare_token_types(TokenType.RETURN)):
            token = self.scanner.get_token_and_move()
            or_expression = self.parse_or_expression()

            if not or_expression:
                raise ParserException(self.scanner.token, "Missing value to return")

            self.check_current_token(TokenType.SEMICOLON)

            return_statement = Return(or_expression)
            self.scanner.next_token()

        return return_statement

    def parse_reflect_statement(self):

        reflect = None
        if self.compare_token_types(TokenType.REFLECT):
            self.scanner.next_token()
            is_recursive = False

            # maybe recursive
            if self.compare_token_types(TokenType.RECURSIVE):
                is_recursive = True

            # or_expression
            or_expression = self.parse_or_expression()

            # semicolon
            self.ckeck_current_token(TokenType.SEMICOLON)
            self.scanner.next_token()

            reflect = Reflect(or_expression, is_recursive)

        return reflect



    def parse_comment_statement(self):

        comment = None
        if self.compare_token_types(TokenType.COMMENT):
            token = self.scanner.get_token_and_move()
            comment = Comment(token.value)

        return comment



    def parse_function_call(self):


        has_this = False
        identifier = None
        function_call = None


        if self.compare_token_types(TokenType.THIS):
            has_this = True
            self.scanner.next_token()
            self.check_current_token(TokenType.ACCESS)
            self.scanner.next_token()


        # value_getter
        value_getter = self.parse_value_getter()

        # restoring last identifier
        if value_getter and value_getter.get_num_base_getters() >= 1:

            last_base_getter = value_getter.base_getters[-1]
            value_getter.base_getters.pop()

            if last_base_getter.rest_function_call and not last_base_getter.slising_expr:

                identifier = last_base_getter.identifier
                rest_call = last_base_getter.rest_function_call

                function_call = FunctionCall(
                    has_this,
                    value_getter,
                    identifier,
                    rest_call
                )

            else:
                raise Exception("Last element in parsing function call cannot be slices")

        return function_call



    def parse_assign_statement(self):

        assign_statement = None
        # complex_identifier
        complex_identifier = self.parse_complex_identifier()

        if self.compare_token_types(TokenType.ASSIGN):
            # =
            self.scanner.next_token()

            # or_expression
            or_expression = self.parse_or_expression()

            assign_statement = Assign(complex_identifier, or_expression)

        return assign_statement



    def parse_complex_identifier(self):

        has_this = False
        identifier = None

        if self.compare_token_types(TokenType.THIS):
            has_this = True
            self.scanner.next_token()
            self.check_current_token(TokenType.ACCESS)
            self.scanner.next_token()

        value_getter = self.parse_value_getter()

        # restoring identifier

        if value_getter and value_getter.get_num_base_getters() > 0:

            last_base_getter = value_getter.base_getters[-1]
            value_getter.base_getters.pop()

            if not last_base_getter.rest_function_call:
                # move this getter to identifier
                id_name = last_base_getter.identifier
                if last_base_getter.slising_expr:
                    id_slicing_expr = last_base_getter.slising_expr
                    identifier = CollectionElement(id_name, id_slicing_expr)
                else:
                    identifier = id_name

        complex_identifier = ComplexIdentifier(has_this, value_getter, identifier)

        return complex_identifier


    def parse_value_getter(self):

        value_getter = None
        base_getters = self.parse_base_getters()

        value_getter = ValueGetter(base_getters)

        return value_getter


    def parse_base_getters(self):

        base_getters = []

        # Access operators
        base_getter = self.parse_basic_value_getter()

        # TODO: careful with errors here (next tokens)

        while self.compare_token_types(TokenType.ACCESS):

            base_getters.append(base_getter)
            base_getter = self.parse_basic_value_getter()

        return base_getters



    def parse_basic_value_getter(self):

        base_getter = None
        slicing_expr = None
        if self.compare_token_types(TokenType.IDENTIFIER):

            id_token = self.scanner.get_token_and_move()

            rest_call = self.parse_rest_function_call()

            # brackets here
            if self.compare_token_types(TokenType.OPEN_BRACKET):
                self.scanner.next_token()
                slicing_expr = self.parse_add_expression()
                self.check_current_token(TokenType.CLOSING_BRACKET)

            base_getter = BasicValueGetter(id_token.value, rest_call, slicing_expr)
            self.scanner.next_token()

        return base_getter



    def parse_rest_function_call(self):

        rest_function_call = None
        if self.compare_token_types(TokenType.OPEN_PARENTHESIS):

            self.scanner.next_token()
            arguments = self.parse_arguments()

            self.check_current_token(TokenType.CLOSING_PARENTHESIS)

            rest_function_call = RestFunctionCall(arguments)
            self.scanner.next_token()

        return rest_function_call


    def parse_built_in_function(self):
        pass



    def parse_arguments(self):

        list_of_args = []

        argument = self.parse_argument()

        while self.compare_token_types(TokenType.COMMA):

            list_of_args.append(argument)
            argument = self.parse_argument()

        arguments = Arguments(list_of_args)

        return arguments



    def parse_argument(self):

        argument = None
        is_by_ref = False
        # by ref
        if self.compare_token_types(TokenType.BY_REF):
            is_by_ref = True
            self.scanner.next_token()

        # argument (or_expression)
        or_expression = self.parse_or_expression()

        argument = Argument(or_expression, is_by_ref)

        return argument



    def parse_or_expression(self):

        or_expression = OrExpression()
        and_expression = self.parse_and_expression()

        if and_expression:

            or_expression.expressions.append(and_expression)

            while self.compare_token_types(TokenType.OR):

                self.scanner.next_token()
                and_expression = self.parse_and_expression()

                if not and_expression:
                    raise Exception("Wrong expression")

                or_expression.expressions.append(and_expression)


        if or_expression.num_operands() < 1:
            or_expression = None

        return or_expression

    def parse_and_expression(self):

        and_expression = AndExpression()

        eq_expression = self.parse_eq_expression()

        if eq_expression:

            and_expression.expressions.append(eq_expression)

            while self.compare_token_types(TokenType.AND):

                self.scanner.next_token()
                eq_expression = self.parse_eq_expression()

                if not eq_expression:
                    raise Exception("Wrong expression")

                and_expression.expressions.append(eq_expression)

        if and_expression.num_operands() < 1:
            and_expression = None

        return and_expression

    def parse_eq_expression(self):

        eq_expression = EqualityExpression()

        rel_expression = self.parse_rel_expression()

        if rel_expression:
            eq_expression.expressions.append(rel_expression)

            while self.is_equality_token(self.scanner.token.token_type):

                # TODO: resolve problem with the order of the operators

                eq_expression.operators.append(self.parse_operator(self.scanner.token))

                rel_expression = self.parse_rel_expression()

                if not rel_expression:
                    raise Exception("Wrong expression")

                eq_expression.expressions.append(eq_expression)
        if eq_expression.num_operands() < 1:
            eq_expression = None

        return eq_expression


    def is_equality_token(self, token_type):
        return  token_type == TokenType.EQUAL or \
                token_type == TokenType.NOT_EQUAL

    def parse_rel_expression(self):

        rel_expression = RelationExpression()
        add_expression = self.parse_add_expression()

        if add_expression:

            rel_expression.expressions.append(add_expression)

            while self.is_add_token(self.scanner.token.token_type):

                # TODO: resolve problem with the order of the operators
                operator = self.parse_operator()
                rel_expression.operators.append(operator)

                add_expression = self.parse_rel_expression()

                if not rel_expression:
                    raise Exception("Wrong expression")

                rel_expression.expressions.append(add_expression)

        if rel_expression.num_operands() < 1:
            rel_expression = None

        return rel_expression


    def is_relation_token(self, token_type):
        return  token_type == TokenType.GREATER or \
                token_type == TokenType.GREATER_EQUAL or \
                token_type == TokenType.LESS_EQUAL or \
                token_type == TokenType.LESS


    def parse_add_expression(self):

        add_expression = AddExpression()

        mult_expression = self.parse_mul_expression()

        if mult_expression:

            add_expression.expressions.append(mult_expression)

            while self.is_add_token(self.scanner.token.token_type):

                operator = self.parse_operator()
                add_expression.operators.append(operator)

                mult_expression = self.parse_mul_expression()

                if not mult_expression:
                    raise Exception("Wrong expression")

                add_expression.expressions.append(mult_expression)

        if add_expression.num_operands() < 1:
            add_expression = None

        return add_expression


    def is_add_token(self, token_type):
        return  token_type == TokenType.PLUS or \
                token_type == TokenType.MINUS


    def parse_mul_expression(self):

        mul_expression = MultiplyExpression()

        unary_expression = self.parse_unary_expression()

        if unary_expression:

            mul_expression.expressions.append(unary_expression)

            while self.is_add_token(self.scanner.token.token_type):

                operator = self.parse_operator()
                mul_expression.operators.append(operator)

                unary_expression = self.parse_unary_expression()

                if not unary_expression:
                    raise Exception("Wrong expression")

                mul_expression.expressions.append(unary_expression)

        if mul_expression.num_operands() < 1:
            mul_expression = None

        return mul_expression


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
        else:
            return None



    def parse_not_unary_expression(self):

        not_unary_expression = None
        if self.compare_token_types(TokenType.NOT):
            self.scanner.next_token()
            unary_expression = self.parse_unary_expression()
            not_unary_expression = NotUnaryExpression(unary_expression)

        return not_unary_expression


    def parse_negative_unary_expression(self):

        neg_unary_expression = None
        if self.compare_token_types(TokenType.MINUS):
            self.scanner.next_token()
            unary_expression = self.parse_unary_expression()
            neg_unary_expression = NegativeUnaryExpression(unary_expression)

        return neg_unary_expression



    def parse_general_value(self):

        if self.compare_token_types(TokenType.OPEN_PARENTHESIS):
            self.scanner.next_token()

            or_expression = self.parse_or_expression()
            self.check_current_token(TokenType.CLOSING_PARENTHESIS)

            self.scanner.next_token()

            return or_expression
        else:
            return self.parse_value()



    def parse_operator(self):

        token_type = self.scanner.token.token_type

        operator = self.oper_mapper.TOKEN_TYPE_TO_OPER.get(token_type)
        self.scanner.next_token()
        if operator:
            return operator
        else:
            raise Exception("Unknown operator")


    def parse_value(self):

        token = self.scanner.token

        value = None
        # literal value
        if self.is_literal(token.token_type):
            self.scanner.next_token()
            value = self.token_to_literal(token.token_type, token.value)
        # list_value
        elif self.compare_token_types(TokenType.OPEN_BRACKET):

            self.scanner.next_token()
            list_value = self.parse_list_value()

            self.check_current_token(TokenType.CLOSING_BRACKET)
            self.scanner.next_token()

            value = list_value

        # value_getter
        elif self.compare_token_types(TokenType.IDENTIFIER) or self.compare_token_types(TokenType.THIS):
            value_getter = self.parse_value_getter()
            value = value_getter

        self.scanner.next_token()

        return value



    def parse_list_value(self):

        list_value = ListValue()
        or_expression = self.parse_or_expression()

        if or_expression:
            list_value.add_elem(or_expression)

        while self.compare_token_types(TokenType.COMMA):

            self.scanner.next_token()
            or_expression = self.parse_or_expression()

            if or_expression:
                or_expression.add_elem(or_expression)

        return list_value


    def token_to_literal(self, token_type, value):

        literal = None
        if token_type == TokenType.NUMERIC_LITERAL:
            if isinstance(value, int):
                literal = IntLiteral(value)
            elif isinstance(value, float):
                literal = FloatLiteral(value)
        elif token_type == TokenType.STRING_LITERAL:
            literal = StringLiteral(value[1:-1])
        elif token_type == TokenType.BOOL_LITERAL:
            literal = BoolLiteral(value)
        else:
            raise Exception(f"Unknown type of literal\n{self.scanner.token}\n{token_type}")

        self.scanner.next_token()
        return literal


    def is_literal(self, token_type):
        return token_type == TokenType.NUMERIC_LITERAL or \
               token_type == TokenType.STRING_LITERAL or \
               token_type == TokenType.BOOL_LITERAL


    def check_current_token(self, token_type: TokenType):

        token = self.scanner.token
        if not self.compare_token_types(token_type):
            raise ParserException(self.scanner.token_position, f"{token},{token_type}")



    def compare_token_types(self, token_type: TokenType):
        return self.scanner.token.token_type == token_type