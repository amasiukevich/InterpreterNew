from src.interpreter.visitor import Visitor

from src.utils.program3.node import Node

class ThisValueGetter(Node):


    def __init__(self):
        pass

    def accept(self, visitor: Visitor):
        pass

    def __str__(self):
        return "this"


    def __repr__(self):
        return self.__str__()