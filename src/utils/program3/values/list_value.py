from src.interpreter.visitor import Visitor
from .value import Value

class ListValue(Value):

    def __init__(self, expressions=[]):
        self.items = expressions

    def accept(self, visitor: Visitor):
        pass

    def __str__(self):
        return f"[{', '.join([elem for elem in self.items])}]"


    def __repr__(self):
        return self.__str__()