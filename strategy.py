from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def get_route(self, x, y):
        raise NotImplementedError("Требуется переопределить этот метод в классе потомке!")
