from .operator import Operator


class NegativeOperator(Operator):

    def __init__(self):
        self.oper = "-"