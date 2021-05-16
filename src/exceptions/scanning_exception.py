from ..utils.position import Position
from .scanner_exception import ScannerException


class ScanningException(ScannerException):

    def __init__(self, position: Position, msg: str):
        self.position = position
        self.message = msg
        super().__init__(f"Scanning exception at position {self.position}:\n{self.message}")
