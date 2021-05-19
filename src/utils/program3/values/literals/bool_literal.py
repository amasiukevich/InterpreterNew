from .literal import Literal

class BoolLiteral(Literal):

    def __init__(self, value: bool):
        self.value = value
        super(value)

    def __repr__(self):
        return str(self.value)
