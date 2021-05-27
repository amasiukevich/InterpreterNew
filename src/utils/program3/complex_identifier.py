from .node import Node
from src.utils.program3.values.value_getter import ValueGetter
from src.utils.program3.values.collection_element import CollectionElement

# TODO: remove the class
class ComplexIdentifier(Node):

    def __init__(self, has_this: bool, value_getter: ValueGetter, identifier):

        self.has_this = has_this
        self.value_getter = value_getter

        # self.identifier = identifier


    def last_id_type(self):

        if isinstance(self.identifier, str):
            return "str"
        elif isinstance(self.identifier, CollectionElement):
            return "collection_element"


    def __str__(self):

        complex_id_str = ""
        if self.has_this:
            complex_id_str += "this."

        if self.value_getter:
            complex_id_str += f"{self.value_getter}"

        complex_id_str += f"{self.identifier}"

        return complex_id_str

    def __repr__(self):
        return self.__str__()