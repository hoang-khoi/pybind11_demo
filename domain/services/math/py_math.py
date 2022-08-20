from domain.services.math import Math


class PyMath(Math):
    def fibonacci(self, n: int) -> int:
        """
        A stupidly implemented algorithm with O(2^n) time complexity
        """
        if n == 0 or n == 1:
            return n

        return self.fibonacci(n - 1) + self.fibonacci(n - 2)
