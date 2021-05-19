from src.utils.program3.node import Node
from src.utils.program3.functions.arguments import Arguments


class RestFunctionCall(Node):

    def __init__(self, arguments: Arguments):
        self.arguments = arguments


    def __repr__(self):
        return f"({self.arguments})"
