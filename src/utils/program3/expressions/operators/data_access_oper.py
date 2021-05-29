from src.interpreter.visitor import Visitor

from .operator import Operator


class DataAccessOperator(Operator):

    def __init__(self):
        self.oper = "."

    def accept(self, visitor: Visitor):
        pass