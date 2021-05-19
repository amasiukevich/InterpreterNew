from src.utils.program3.statements.statement import Statement
from src.utils.program3.statements.rest_function_call import RestFunctionCall
from src.utils.program3.values.value_getter import ValueGetter


class FunctionCall(Statement):


    def __init__(self,
                 has_this: bool,
                 value_getter: ValueGetter,
                 identifier: str,
                 rest_call: RestFunctionCall):

        self.has_this = has_this
        self.value_getter = value_getter
        self.identifier = identifier
        self.rest_call = rest_call



    def __repr__(self):

        function_call_string = ""
        if self.has_this:
            function_call_string += "this."
        if self.value_getter:
            function_call_string += f"{self.value_getter}"

        function_call_string += f"{self.identifier}{self.rest_call}"
        return function_call_string