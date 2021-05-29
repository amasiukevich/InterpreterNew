from src.interpreter.visitor import Visitor

from src.utils.program3.expressions.expression import Expression


class NotUnaryExpression(Expression):

    def __init__(self, expression: Expression):
        self.expression = expression

    def accept(self, visitor: Visitor):
        pass

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"!({self.expression})"