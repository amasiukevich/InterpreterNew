from .statement import Statement
from src.utils.program3.expressions.expression import Expression
from src.utils.program3.complex_identifier import ComplexIdentifier

class Assign(Statement):

    def __init__(self, complex_id: ComplexIdentifier, expression: Expression):

        self.complex_identifier = complex_id
        self.expression = expression


    def __repr__(self):

        return f"{self.complex_identifier} = {self.expression}"