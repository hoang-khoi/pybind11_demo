from abc import abstractmethod, ABC


class Math(ABC):
    @abstractmethod
    def fibonacci(self, n: int) -> int:
        pass
