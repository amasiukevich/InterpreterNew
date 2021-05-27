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


    def __repr__(self):
        return self.__str__()

    def __str__(self):

        rel_oper_string = ""
        if len(self.expressions) == 0:
            rel_oper_string = "_"
        else:
            if len(self.expressions) > 1:
                rel_oper_string += "("
            rel_oper_string += f"{self.expressions[0]}"
            for i in range(1, len(self.expressions)):

                if self.operators == []:
                    breakpoint()
                rel_oper_string += f"{self.operators[i - 1]}"
                rel_oper_string += self.expressions[i]

            if len(self.expressions) > 1:
                rel_oper_string += ")"

        return rel_oper_string