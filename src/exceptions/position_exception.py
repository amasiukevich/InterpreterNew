class PositionException(Exception):

    def __init__(self, msg: str):
        self.message = msg
        super().__init__(self.message)