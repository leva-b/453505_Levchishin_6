"""
Series classes for function approximation.
Lab 4, Task 3, Variant 6 (sin x).
Developer: Ivan Leuchyshyn
Date: 2026-04-26
"""

import math
from abc import ABC, abstractmethod

class SeriesBase(ABC):
    """Abstract base class for series expansion."""
    
    def __init__(self, eps: float = 1e-6, max_iter: int = 100):
        self._eps = eps
        self._max_iter = max_iter
    
    @property
    def eps(self) -> float:
        return self._eps
    
    @eps.setter
    def eps(self, value: float):
        if value <= 0:
            raise ValueError("Precision must be positive")
        self._eps = value
    
    @property
    def max_iter(self) -> int:
        return self._max_iter
    
    @max_iter.setter
    def max_iter(self, value: int):
        if value < 1:
            raise ValueError("max_iter must be >= 1")
        self._max_iter = value
    
    @abstractmethod
    def term(self, x: float, n: int) -> float:
        """Calculate n-th term of the series (n starting from 0)."""
        pass
    
    def partial_sum(self, x: float, n_max: int) -> float:
        """Sum of terms from n=0 to n_max."""
        s = 0.0
        for n in range(n_max + 1):
            s += self.term(x, n)
        return s
    
    def compute_until_eps(self, x: float) -> tuple:
        """
        Compute series until |term| < eps or max_iter reached.
        Returns (sum, number_of_terms_used, list_of_partial_sums).
        """
        s = 0.0
        history = []
        for n in range(self._max_iter + 1):
            t = self.term(x, n)
            s += t
            history.append(s)
            if abs(t) < self._eps:
                return s, n + 1, history
        return s, self._max_iter + 1, history
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__}(eps={self._eps}, max_iter={self._max_iter})"


class SinSeries(SeriesBase):
    """Sin(x) = sum_{n=0}∞ (-1)^n * x^(2n+1) / (2n+1)!."""
    
    def term(self, x: float, n: int) -> float:
        """Term for given n (0‑based)."""
        power = 2 * n + 1
        sign = -1 if n % 2 else 1
        # compute factorial iteratively to avoid huge numbers
        fact = math.factorial(power)
        return sign * (x ** power) / fact
    
    def compute_table(self, x_values: list) -> list:
        """
        For each x in x_values, compute approximated value and exact.
        Returns list of dicts: {'x': x, 'approx': approx, 'exact': exact, 'terms': n_used}
        """
        table = []
        for x in x_values:
            approx, terms_used, _ = self.compute_until_eps(x)
            exact = math.sin(x)
            table.append({
                'x': x,
                'approx': approx,
                'exact': exact,
                'terms': terms_used,
                'abs_error': abs(approx - exact)
            })
        return table