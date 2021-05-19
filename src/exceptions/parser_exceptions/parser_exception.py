from src.utils.position import Position


class ParserException(Exception):

    def __init__(self, position: Position, msg: str):

        self.message = msg
        self.position = position
        super().__init__(f"Parsing Exception at position {self.position}\n: {self.message}")