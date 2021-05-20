from .value import Value
from src.utils.program3.expressions.math.add_expression import AddExpression

class CollectionElement(Value):


    def __init__(self, identifier: str, index: AddExpression):

        self.identifier = identifier
        self.index = index


    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"{self.identifier}[{self.index}]"