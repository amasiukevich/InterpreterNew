from src.utils.program3.node import Node
from src.utils.program3.statements.rest_function_call import RestFunctionCall
from src.utils.program3.expressions.math.add_expression import AddExpression

class BasicValueGetter(Node):

    def __init__(self, identifier: str, rest_call: RestFunctionCall, slicing_expr: AddExpression):

        self.identifier = identifier
        self.rest_call = rest_call
        self.slicing_expr = slicing_expr


    def __repr__(self):
        return self.__str__()

    def __str__(self):

        basic_value_getter_str = f"{self.identifier}"
        if bool(self.rest_call):
            basic_value_getter_str += f"{self.rest_call}"
        if bool(self.slicing_expr):
            basic_value_getter_str += f"[{self.slising_expr}]"

        return basic_value_getter_str
