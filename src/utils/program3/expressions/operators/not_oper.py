from .operator import Operator


class NotOperator(Operator):

    def __init__(self):
        self.oper = "!"