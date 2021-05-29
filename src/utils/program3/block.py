from src.interpreter.visitor import Visitor

from src.utils.program3.node import Node
from src.utils.program3.statements.statement import Statement


class Block(Node):

    def __init__(self, statements=[]):

        # if len(statements) != 0 and not all([isinstance(statement, Statement) for statement in statements]):
        #     raise ParserException("All elements must be of Statement datatype")

        self.statements = statements


    def add_statement(self, statement: Statement):
        self.statements.append(statement)


    def accept(self, visitor: Visitor):
        pass


    def __str__(self):

        block_string = "{"
        for statement in self.statements:
            block_string += f"\n{statement}"
        block_string += "\n}"

        return block_string


    def __repr__(self):
        return self.__str__()