from src.interpreter.visitor import Visitor

from src.utils.program3.node import Node


class Operator(Node):

    def __init__(self):
        self.oper = ""

    def accept(self, visitor: Visitor):
        pass

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.oper
