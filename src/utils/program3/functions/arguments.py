from ..node import Node
from .argument import Argument


class Arguments(Node):

    def __init__(self, arguments=[]):

        # a list of Argument objects
        self.arguments = arguments



    def add_argument(self, argument: Argument):
        self._arguments.add(argument)


    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return ", ".join(f"{self.arguments}")