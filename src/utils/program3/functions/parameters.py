from src.interpreter.visitor import Visitor

from ..node import Node


# TODO: move check uniqueness to helpers file
def check_unique(list_of_names):
    return len(set(list_of_names)) == len(list_of_names)


class Parameters(Node):


    def __init__(self, param_names):

        # checking uniqueness
        if not check_unique(param_names):
            raise Exception("Param names are not unique")

        self._parameters = param_names

    def accept(self, visitor: Visitor):
        pass

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return ", ".join(self._parameters)
