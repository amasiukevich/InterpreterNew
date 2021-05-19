from .operator import Operator


class AndOperator(Operator):

    def __init__(self):
        self.oper = "&&"