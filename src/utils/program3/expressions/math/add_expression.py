from src.utils.program3.expressions.expression import Expression


class AddExpression(Expression):

    # PLUS AND MINUS

    def __init__(self, expressions=[], operators=[]):

        # TODO: expressions check (instances)
        # TODO: operators check (instances)
        # TODO: expressions - operators == 1 check

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
