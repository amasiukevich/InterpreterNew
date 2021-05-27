from src.utils.program3.expressions.expression import Expression
from src.utils.program3.expressions.operators.operator import Operator


class MultiplyExpression(Expression):

    # HERE CAN BE ALSO DIVIDERS AND MODULO

    def __init__(self, expressions=[], operators=[]):

        if len(expressions) > 0 and not all([isinstance(expr, Expression) for expr in expressions]):
            raise Exception("All of the components must be of Expression datatype")

        if len(operators) > 0 and not all([isinstance(oper, Operator) for oper in operators]):
            raise Exception("All of the elements among operators must be of Operator datatype")

        if len(expressions) - len(operators) != 1:
            raise Exception("Number of exception components must be greater than number of operators by 1")


        self.expressions = expressions
        self.operators = operators


    def __repr__(self):
        return self.__str__()


    def __str__(self):
        mult_oper_string = ""
        if len(self.expressions) == 0:
            mult_oper_string = "_"
        else:
            if len(self.expressions) > 1:
                mult_oper_string += "("
            mult_oper_string += f"{self.expressions[0]}"
            for i in range(1, len(self.expressions)):
                mult_oper_string += f" {self.operators[i - 1]} "
                mult_oper_string += f"{self.expressions[i]}"
            if len(self.expressions) > 1:
                mult_oper_string += ")"

        return mult_oper_string