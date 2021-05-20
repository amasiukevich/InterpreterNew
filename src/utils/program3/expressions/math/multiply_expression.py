from src.utils.program3.expressions.expression import Expression
from src.utils.program3.expressions.operators.operator import Operator


class MultiplyExpression(Expression):

    # HERE CAN BE ALSO DIVIDERS AND MODULO

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
        mult_oper_string = ""
        if self.num_operands == 0:
            mult_oper_string = "_"
        else:
            if self.num_operands() > 1:
                mult_oper_string += "("
            mult_oper_string += f"{self.expressions[0]}"
            for i in range(1, self.num_operands()):
                mult_oper_string += f" {self.operators[i - 1]} "
                mult_oper_string += f"{self.expressions[i]}"
            if self.num_operands() > 1:
                mult_oper_string += ")"

        return mult_oper_string