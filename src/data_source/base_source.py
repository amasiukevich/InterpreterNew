import abc

class BaseSource(metaclass=abc.ABCMeta):

    def __init__(self, position):
        self.position = position

    @abc.abstractmethod
    def get_curr_char(self):
        pass

    @abc.abstractmethod
    def peek(self):
        pass

    @abc.abstractmethod
    def next(self):
        pass