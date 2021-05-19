from .literal import Literal


class FloatLiteral(Literal):

    def __init__(self, value: float):
        self.value = value
        super(value)

    def __repr__(self):
        return str(self.value)
