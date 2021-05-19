from src.utils.program3.functions.function import Function
from src.utils.program3.classes._class import Class
from .node import Node


class Program(Node):

    def __init__(self, functions: dict, classes: dict):

        self._functions = functions
        self._classes = classes

    def functions_unique(self):
        return self.check_names_unique([function_name for function_name in self._functions.keys()])

    def classes_unique(self):
        return self.check_names_unique([_class_name for _class_name in self._classes.keys()])

    def check_names_unique(self, names_list):
        return len(list(set(names_list))) == len(names_list)

    def add_function(self, function: Function):
        if self.functions_unique(self._functions + [function.identifier]):
            self._functions[function.identifier] = function

    def add_class(self, _class: Class):
        if self.classes_unique(self._classes + [_class.identifier]):
            self._classes[_class.identifier] = _class

    def has_functions(self):
        return len(self.functions) > 0

    def function_exists(self, function_identifier):
        return bool(self._functions.get(function_identifier))