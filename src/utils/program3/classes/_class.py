from src.utils.program3.node import Node
from .class_block import ClassBlock

class Class(Node):

    def __init__(self, identifier, body: ClassBlock):
        try:
            if not body.is_valid_class_block(identifier):
                raise Exception("A class block should contain the constructor of the same name as class")
        except:
            breakpoint()

        self.identifier = identifier
        self.body = body

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"class {self.identifier}{self.body}"