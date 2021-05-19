from src.utils.program3.expressions.expression import Expression


class NotUnaryExpression(Expression):

    def __init__(self, expression: Expression):
        self.expression = expression

    def __repr__(self):
        return f"!({self.expression})"