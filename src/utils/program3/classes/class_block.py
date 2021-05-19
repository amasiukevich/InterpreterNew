from src.utils.program3.functions.function import Function
from src.utils.program3.node import Node

class ClassBlock(Node):

    def __init__(self, methods=[]):
        self.methods = methods

    def add_method(self, method: Function):
        self.methods.append(method)

    def __repr__(self):
        pass