from src.utils.program3.expressions.expression import Expression


class EqualityExpression(Expression):

    # EQUAL and NOT_EQUAL

    def __init__(self, expressions=[], operators=[]):

        # TODO: expressions check (instances)
        # TODO: operators check (instances)
        # TODO: expressions - operators == 1 check

        self.expressions = expressions
        self.operators = operators


    def num_operands(self):
        return len(self.expressions)


    def __repr__(self):
        return self.__str__()


    def __str__(self):

        eq_oper_string = ""
        if self.num_operands() == 0:
            eq_oper_string = "_"
        else:
            if self.num_operands() > 1:
                eq_oper_string += "("
            eq_oper_string += f"{self.expressions[0]}"

            for i in range(1, self.num_operands()):

                eq_oper_string += f" {self.operators[i - 1]} "
                eq_oper_string += self.expressions[i]
            if self.num_operands() > 1:
                eq_oper_string += ")"

        return eq_oper_string
