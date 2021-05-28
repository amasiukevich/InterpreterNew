from .visitor import Visitor
from ..utils.program3.program import Program


class Interpreter(Visitor):


    def __init__(self, program: Program):

        self.program = program
        # TODO: enviroment here
        # TODO: I/O streams here


    def visit_program(self):
        pass

    def visit_function(self):
        pass

    def visit_class(self):
        pass

    def visit_params(self):
        pass

    def visit_block(self):
        pass

    def visit_class_block(self):
        pass

    def visit_statement(self):
        pass

    def visit_if(self):
        pass

    def visit_foreach(self):
        pass

    def visit_while(self):
        pass

    def visit_return(self):
        pass

    def visit_reflect(self):
        pass

    def visit_comment(self):
        pass

    def visit_assign(self):
        pass

    def visit_function_call(self):
        pass

    def visit_value_getter(self):
        pass

    def visit_this_value_getter(self):
        pass

    def visit_base_value_getter(self):
        pass

    def visit_rest_function_call(self):
        pass

    def visit_arguments(self):
        pass

    def visit_argument(self):
        pass

    def visit_or_expression(self):
        pass

    def visit_and_expression(self):
        pass

    def visit_eq_expression(self):
        pass

    def visit_rel_expression(self):
        pass

    def visit_add_expression(self):
        pass

    def visit_mul_expression(self):
        pass

    def visit_unary_expression(self):
        pass

    def visit_not_unary_expression(self):
        pass

    def visit_negative_unary_expression(self):
        pass

    def visit_list_value(self):
        pass

    def visit_bool_literal(self):
        pass

    def visit_float_literal(self):
        pass

    def visit_int_literal(self):
        pass

    def visit_string_literal(self):
        pass

    def visit_and_oper(self):
        pass

    def visit_data_access_oper(self):
        pass

    def visit_divide_oper(self):
        pass

    def visit_equal_oper(self):
        pass

    def visit_greater_equal_oper(self):
        pass

    def visit_greater_oper(self):
        pass

    def visit_less_equal_oper(self):
        pass

    def visit_less_oper(self):
        pass

    def visit_minus_oper(self):
        pass

    def visit_multiply_oper(self):
        pass

    def visit_negative_oper(self):
        pass

    def visit_not_equal_oper(self):
        pass

    def visit_or_oper(self):
        pass

    def visit_plus_oper(self):
        pass