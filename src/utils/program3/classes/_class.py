from src.utils.program3.node import Node
from .class_block import ClassBlock

class Class(Node):

    def __init__(self, identifier, body: ClassBlock):

        self.identifier = identifier
        self.body = body