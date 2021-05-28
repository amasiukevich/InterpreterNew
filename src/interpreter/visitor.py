from __future__ import annotations
from abc import ABC, abstractmethod


class Visitor(ABC):


    @abstractmethod
    def visit_program(self):
        pass

    @abstractmethod
    def visit_function(self):
        pass


    @abstractmethod
    def visit_class(self):
        pass


    @abstractmethod
    def visit_params(self):
        pass


    @abstractmethod
    def visit_block(self):
        pass


    @abstractmethod
    def visit_class_block(self):
        pass


    @abstractmethod
    def visit_statement(self):
        pass


    @abstractmethod
    def visit_if(self):
        pass


    @abstractmethod
    def visit_foreach(self):
        pass


    @abstractmethod
    def visit_while(self):
        pass


    @abstractmethod
    def visit_return(self):
        pass


    @abstractmethod
    def visit_reflect(self):
        pass


    @abstractmethod
    def visit_comment(self):
        pass


    @abstractmethod
    def visit_assign(self):
        pass


    @abstractmethod
    def visit_function_call(self):
        pass



    @abstractmethod
    def visit_value_getter(self):
        pass


    @abstractmethod
    def visit_this_value_getter(self):
        pass



    @abstractmethod
    def visit_base_value_getter(self):
        pass


    @abstractmethod
    def visit_rest_function_call(self):
        pass


    @abstractmethod
    def visit_arguments(self):
        pass


    @abstractmethod
    def visit_argument(self):
        pass


    @abstractmethod
    def visit_or_expression(self):
        pass


    @abstractmethod
    def visit_and_expression(self):
        pass


    @abstractmethod
    def visit_eq_expression(self):
        pass


    @abstractmethod
    def visit_rel_expression(self):
        pass


    @abstractmethod
    def visit_add_expression(self):
        pass


    @abstractmethod
    def visit_mul_expression(self):
        pass


    @abstractmethod
    def visit_unary_expression(self):
        pass


    @abstractmethod
    def visit_not_unary_expression(self):
        pass


    @abstractmethod
    def visit_negative_unary_expression(self):
        pass


    # values

    @abstractmethod
    def visit_list_value(self):
        pass


    @abstractmethod
    def visit_bool_literal(self):
        pass


    @abstractmethod
    def visit_float_literal(self):
        pass


    @abstractmethod
    def visit_int_literal(self):
        pass


    @abstractmethod
    def visit_string_literal(self):
        pass


    # operators

    @abstractmethod
    def visit_and_oper(self):
        pass


    @abstractmethod
    def visit_data_access_oper(self):
        pass



    @abstractmethod
    def visit_divide_oper(self):
        pass



    @abstractmethod
    def visit_equal_oper(self):
        pass


    @abstractmethod
    def visit_greater_equal_oper(self):
        pass


    @abstractmethod
    def visit_greater_oper(self):
        pass


    @abstractmethod
    def visit_less_equal_oper(self):
        pass


    @abstractmethod
    def visit_less_oper(self):
        pass


    @abstractmethod
    def visit_minus_oper(self):
        pass


    @abstractmethod
    def visit_multiply_oper(self):
        pass


    @abstractmethod
    def visit_negative_oper(self):
        pass


    @abstractmethod
    def visit_not_equal_oper(self):
        pass


    @abstractmethod
    def visit_or_oper(self):
        pass


    @abstractmethod
    def visit_plus_oper(self):
        pass



    @abstractmethod
    def visit_plus_oper(self):
        pass