from abc import ABC, abstractmethod
from src.interpreter.visitor import Visitor

class Node(ABC):

    @abstractmethod
    def accept(self, visitor: Visitor):
        pass