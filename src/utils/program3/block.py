from src.utils.program3.node import Node
from src.utils.program3.statements.statement import Statement

from src.exceptions.parser_exceptions.parser_exception import ParserException

class Block(Node):

    def __init__(self, statements=[]):

        # if len(statements) != 0 and not all([isinstance(statement, Statement) for statement in statements]):
        #     raise ParserException("All elements must be of Statement datatype")

        self.statements = statements


    def add_statement(self, statement: Statement):
        self.statements.append(statement)


    def __repr__(self):

        block_string = "{"
        for statement in self.statements:
            block_string += f"{statement}\n"
        block_string += "}"

        return block_string