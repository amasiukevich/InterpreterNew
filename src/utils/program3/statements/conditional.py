from src.utils.program3.block import Block
from src.utils.program3.statements.statement import Statement
from src.utils.program3.expressions.expression import Expression




class Conditional(Statement):


    def __init__(self, conditions: list, blocks: list):


        # if len(conditions) <= 0:
        #     raise ParserException("At least one condition should be provided")
        # elif not all([isinstance(condition, Expression) for condition in conditions]):
        #     raise ParserException("Parser Exception: all of the conditions must be of Expresssion datatype")
        #
        # if len(blocks) <= 1:
        #     raise ParserException("Parser Exception: At least 2 blocks should be provided")
        # elif not all([isinstance(block, Block)] for block in blocks):
        #     raise ParserException("Parser Exception: all of the block must be of Block datatype")
        #
        # if len(blocks) - len(conditions) != 1:
        #     raise ParserException("Parser Exception: number of blocks"
        #                           "must be greater of number of conditions by exaclty 1")

        self.logical_conditions = conditions
        self.blocks = blocks


    def __repr__(self):
        return self.__str__()

    def __str__(self):


        conditional_string = ""
        if_string = "if "
        else_if_string = "else if "
        else_string = "else "

        if len(self.logical_conditions) == 1 and len(self.blocks) == 1:
            # single if case
            conditional_string = f"{if_string}{self.conditions[0]}\n{self.blocks[0]}"

        elif len(self.logical_conditions) == 1 and len(self.blocks) == 2:
            conditional_string = f"{if_string}{self.conditions[0]}\n{self.blocks[0]}\n{else_string}\n{self.blocks[1]}"

        else:

            for i in range(len(self.logical_conditions)):

                if i == 0:
                    conditional_string += if_string
                else:
                    conditional_string += else_if_string

                conditional_string += self.logical_conditions[i]
                conditional_string += f"\n{self.blocks[i]}\n"

            conditional_string += else_string
            conditional_string += f"\n{self.blocks[-1]}\n"


        return conditional_string