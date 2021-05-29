from src.interpreter.visitor import Visitor

from src.utils.program3.expressions.expression import Expression
from src.utils.program3.block import Block
from .statement import Statement

class WhileLoop(Statement):

    def __init__(self, expression: Expression, body: Block):
        self.logical_expr = expression
        self.body = body

    def accept(self, visitor: Visitor):
        pass

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"while {self.logical_expr}\n{self.body}"