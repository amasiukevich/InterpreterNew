from src.interpreter.visitor import Visitor

from .literal import Literal


class FloatLiteral(Literal):

    def __init__(self, value: float):
        self.value = value
        super().__init__(value)

    def accept(self, visitor: Visitor):
        pass


    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return super.__str__()
