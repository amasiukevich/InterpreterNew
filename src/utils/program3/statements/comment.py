from .statement import Statement


class Comment(Statement):


    def __init__(self, comment_body):
        self.comment_body = comment_body


    def __repr__(self):
        return self.comment_body