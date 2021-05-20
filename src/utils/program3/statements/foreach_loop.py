from src.utils.program3.expressions.expression import Expression
from src.utils.program3.block import Block

from .loop import Loop


class ForeachLoop(Loop):


    def __init__(self, identifier: str, expression: Expression, block: Block):

        self.identifier = identifier
        self.expression = expression
        self.block = block


    def __repr__(self):
        return self.__str__()

    def __str__(self):

        return f"foreach {self.identifier} in {self.expression}\n" \
               f"{self.block}"