from src.interpreter.visitor import Visitor

from src.utils.program3.functions.function import Function
from src.utils.program3.node import Node



class ClassBlock(Node):

    def __init__(self, methods=[]):
        self.methods = methods


    def accept(self, visitor: Visitor):
        pass


    def is_valid_class_block(self, class_name):

        if len(self.methods) > 0:
            return class_name in [method.identifier for method in self.methods]
        else:
            return True

    def __repr__(self):
        return self.__str__()

    def __str__(self):

        class_block_string = "{"
        for method in self.methods:
            class_block_string += f"\n{method}"

        class_block_string += "\n}"

        return class_block_string

