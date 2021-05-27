from src.utils.program3.values.value import Value


class Literal(Value):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.value}"


    def __repr__(self):
        return self.__str__()