from .value import Value


class ListValue(Value):



    def __init__(self, expressions=[]):
        self.items = expressions


    def add_elem(self, expression):
        self.items.append(expression)



    def __str__(self):
        return f"[{', '.join([elem for elem in self.items])}]"


    def __repr__(self):
        return self.__str__()