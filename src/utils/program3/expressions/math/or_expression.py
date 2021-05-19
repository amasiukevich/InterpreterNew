from src.utils.program3.expressions.expression import Expression
from src.exceptions.parser_exceptions.parser_exception import ParserException


class OrExpression(Expression):


    def __init__(self, expressions=[]):

        # TODO: to the main class
        # if len(expressions) > 0 and not all([isinstance(expr, Expression) for expr in expressions]):
        #     raise ParserException("All elements should be of Expression datatype")

        self.expressions = expressions



    def num_operands(self):
        return len(self.expressions)



    def __repr__(self):

        or_expr_str = "_"

        if self.num_operands() > 0:

            or_expr_str = f"{self.expressions[0]}"
            for i in range(1, self.num_operands):
                or_expr_str.append(" || ")
                or_expr_str.append(self.expressions[i])

        return or_expr_str
