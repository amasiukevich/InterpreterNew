from .parameters import Parameters
from src.utils.program3.block import Block
from src.utils.program3.node import Node


class Function(Node):


    def __init__(self, identifier, parameters: Parameters, body: Block):

        self.identifier = identifier
        self.parameters = parameters
        self.body = body

        # TODO: what's with the returning value?


    def __repr__(self):
        return f"define {self.identifier} ({self.parameters})\n{self.body}"