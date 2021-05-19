from .operator import Operator


class NotEqualOperator(Operator):

    def __init__(self):
        self.oper = "!="