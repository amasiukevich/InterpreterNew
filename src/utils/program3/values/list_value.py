from .value import Value


class ListValue(Value):



    def __init__(self, expressions=[]):
        self.items = expressions


    def add_elem(self, expression):
        self.items.append(expression)

    def __repr__(self):
        return f"[{', '.join([elem for elem in self.items])}]"
