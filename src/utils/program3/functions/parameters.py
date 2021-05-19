from ..node import Node

class Parameters(Node):


    def __init__(self):
        self._parameters = []


    def add_parameter(self, identifier):
        self._parameters.append(identifier)


    def __repr__(self):
        return ", ".join(self._parameters)
