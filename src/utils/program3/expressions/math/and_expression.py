from src.utils.program3.expressions.expression import Expression



class AndExpression(Expression):


    def __init__(self, expressions=[]):


        # TODO: to the main class
        # if len(expressions) > 0 and not all([isinstance(expr, Expression) for expr in expressions]):
        #     raise ParserException("All elements should be of Expression datatype")

        self.expressions = expressions


    def __repr__(self):
        return self.__str__()


    def __str__(self):

        and_expr_str = "_"

        if len(self.expressions) > 0:

            and_expr_str = f"{self.expressions[0]}"
            for i in range(1, len(self.expressions)):
                and_expr_str += " && "
                and_expr_str += f"{self.expressions[i]}"

        return and_expr_str
