from ..exceptions.position_exception import PositionException

class Position():

    def __init__(self, line=1, column=0):
        
        if line <= 0:
            raise PositionException("Line number cannot be less or equal to 0")

        if column < 0:
            raise PositionException("Column number cannot be less than 0")
        self.line = line
        self.column = column



    def advance_column(self):
        self.column += 1

    def advance_line(self):

        self.line += 1
        self.column = 0


    def __str__(self):
        return f"line: {self.line}, column: {self.column}"

    def __repr__(self):
        return self.__str__()


    def __eq__(self, other):
        if not isinstance(other, Position):
            return False
        else:
            return self.line == other.line and self.column == other.column


    def clone(self):
        return Position(line=self.line, column=self.column)