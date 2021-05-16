from ..utils.position import Position

class SourceException(Exception):

    def __init__(self, position: Position, msg: str):
        super().__init__(f"Source exception at position {position}:\n{msg}")