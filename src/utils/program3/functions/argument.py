from src.interpreter.visitor import Visitor

from src.utils.program3.node import Node
from src.utils.program3.expressions.expression import Expression

class Argument(Node):

    def __init__(self, expression: Expression, is_by_ref: bool):

        self.expression = expression
        self.is_by_ref = is_by_ref

    def accept(self, visitor: Visitor):
        pass

    def __repr__(self):
        return self.__str__()

    def __str__(self):

        argument_str = ""
        if self.is_by_ref:
            argument_str += "by_ref "
        argument_str += f"{self.expression}"

        return argument_str
