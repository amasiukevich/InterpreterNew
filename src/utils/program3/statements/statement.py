from src.interpreter.visitor import Visitor
from src.utils.program3.node import Node


class Statement(Node):

    def accept(self, visitor: Visitor):
        pass