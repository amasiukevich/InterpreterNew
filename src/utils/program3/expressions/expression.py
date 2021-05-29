from src.interpreter.visitor import Visitor

from src.utils.program3.node import Node


class Expression(Node):

    def num_operands(self):
        return 1