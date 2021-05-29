from src.interpreter.visitor import Visitor

from src.utils.program3.expressions.expression import Expression


class Value(Expression):

    def accept(self, visitor: Visitor):
        pass