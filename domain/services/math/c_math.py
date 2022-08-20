from domain.services.math import Math
from domain.services.math import libmath

class CMath(Math):
    def fibonacci(self, n: int) -> int:
        return libmath.fibonacci(n)
