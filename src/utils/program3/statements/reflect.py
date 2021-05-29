from src.interpreter.visitor import Visitor

from src.utils.program3.node import Node
from src.utils.program3.expressions.expression import Expression


class Reflect(Node):


    def __init__(self, expression: Expression, is_recursive: bool):

        self.expression = expression
        self.is_recursive = is_recursive

    def accept(self, visitor: Visitor):
        pass

    def __repr__(self):
        return self.__str__()

    def __str__(self):

        reflect_string = "reflect "
        if self.is_recursive:
            reflect_string += "recursive "
        reflect_string += f"{self.expression};"

        return reflect_string