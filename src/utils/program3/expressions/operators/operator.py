from src.utils.program3.node import Node


class Operator(Node):

    def __init__(self):
        self.oper = ""

    def __repr__(self):
        return self.oper
