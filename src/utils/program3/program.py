from src.utils.program3.functions.function import Function
from src.utils.program3.classes._class import Class
from .node import Node



def check_unique_names(list_of_names):
    return len(set(list_of_names)) == len(list_of_names)


class Program(Node):

    def __init__(self, functions: dict, classes: dict):

        # functions unique
        if not check_unique_names([function_name for function_name in functions.keys()]):


            raise Exception("Names of the functions are not unique")

        # classes unique
        if not check_unique_names([class_name for class_name in classes.keys()]):
            raise Exception("Names of the classes are not unique")

        # has main function
        if not 'main' in [function_name for function_name in functions.keys()]:
            raise Exception("Function `main` not detected")

        # main function has no parameters

        self._functions = functions
        self._classes = classes


    def add_function(self, function: Function):

        if check_unique_names(
                [function_name for function_name in self.functions.keys()] + [function.identifier]
        ):
            self._functions[function.identifier] = function

    def add_class(self, _class: Class):
        if check_unique_names(
            [class_name for class_name in self._classes.keys()] + [_class.identifier]
        ):
            self._classes[_class.identifier] = _class

    def has_functions(self):
        return len(self.functions) > 0

    def function_exists(self, function_identifier):
        return bool(self._functions.get(function_identifier))



    def __str__(self):

        # TODO: specify the order of functions
        program_string = ""

        for function in self._functions:
            program_string += f"\n{function}"

        program_string += "\n"
        for _class in self._classes:
            program_string += f"\n{_class}"

        program_string += "\n"

        return program_string


    def __repr__(self):
        return self.__str__()