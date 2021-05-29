from src.interpreter.visitor import Visitor

from .statement import Statement


class Comment(Statement):

    def __init__(self, comment_body):
        self.comment_body = comment_body

    def accept(self, visitor: Visitor):
        pass

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.comment_body