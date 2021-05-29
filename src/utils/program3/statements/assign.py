from src.interpreter.visitor import Visitor

from .statement import Statement
from src.utils.program3.expressions.expression import Expression

class Assign(Statement):

    def __init__(self, value_getter, expression: Expression):

        self.value_getter = value_getter
        self.expression = expression

    def accept(self, visitor: Visitor):
        pass

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"{self.value_getter} = {self.expression};"