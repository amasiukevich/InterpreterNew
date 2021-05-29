from src.interpreter.visitor import Visitor

from src.utils.program3.expressions.expression import Expression
from src.utils.program3.expressions.operators.operator import Operator

class EqualityExpression(Expression):

    # EQUAL and NOT_EQUAL

    def __init__(self, expressions=[], operators=[]):

        if len(expressions) > 0 and not all([isinstance(expr, Expression) for expr in expressions]):
            raise Exception("All of the components must be of Expression datatype")

        if len(operators) > 0 and not all([isinstance(oper, Operator) for oper in operators]):
            raise Exception("All of the elements among operators must be of Operator datatype")

        if len(expressions) - len(operators) != 1:
            raise Exception("Number of exception components must be greater than number of operators by 1")

        self.expressions = expressions
        self.operators = operators


    def accept(self, visitor: Visitor):
        pass

    def __repr__(self):
        return self.__str__()


    def __str__(self):

        eq_oper_string = ""
        if len(self.expressions) == 0:
            eq_oper_string = "_"
        else:
            if len(self.expressions) > 1:
                eq_oper_string += "("
            eq_oper_string += f"{self.expressions[0]}"

            for i in range(1, len(self.expressions)):

                eq_oper_string += f" {self.operators[i - 1]} "
                eq_oper_string += self.expressions[i]
            if len(self.expressions) > 1:
                eq_oper_string += ")"

        return eq_oper_string
