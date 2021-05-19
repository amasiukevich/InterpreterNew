from src.utils.program3.expressions.expression import Expression
from src.utils.program3.expressions.operators.operator import Operator


class RelationExpression(Expression):


    # GREATER, GREATER_EQUAL, LESS, LESS_EQUAL

    def __init__(self, expressions=[], operators=[]):

        # TODO: expressions check (instances)
        # TODO: operators check (instances)
        # TODO: expressions - operators == 1 check

        self.expressions = expressions
        self.operators = operators



    def num_operands(self):
        return len(self.expressions)



    def __repr__(self):

        rel_oper_string = ""

        if self.num_operands() == 0:
            rel_oper_string = "_"
        else:
            if self.num_operands() > 1:
                rel_oper_string += "["
            rel_oper_string += self.expressions[0]

            for i in range(1, self.num_operands()):
                rel_oper_string += f"{self.operators[i - 1]}"
                rel_oper_string += self.expressions[i]

            if self.num_operands() > 1:
                rel_oper_string += "]"

        return rel_oper_string