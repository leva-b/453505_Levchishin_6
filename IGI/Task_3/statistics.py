"""
Statistical calculations (mean, median, mode, variance, std) as mixin and standalone.
Lab 4, Task 3.
Developer: Ivan Leuchyshyn
Date: 2026-04-26
"""

from collections import Counter
import math
from typing import List, Union, Tuple

class StatisticsMixin:
    """Mixin adding statistical methods to a class that has a sequence attribute."""
    
    def _get_sequence(self) -> List[float]:
        """Override this to return the list of values."""
        raise NotImplementedError
    
    def arithmetic_mean(self) -> float:
        seq = self._get_sequence()
        if not seq:
            return 0.0
        return sum(seq) / len(seq)
    
    def median(self) -> float:
        seq = sorted(self._get_sequence())
        n = len(seq)
        if n == 0:
            return 0.0
        if n % 2 == 1:
            return seq[n // 2]
        else:
            return (seq[n // 2 - 1] + seq[n // 2]) / 2.0
    
    def mode(self) -> List[float]:
        """Return list of modes (most frequent values)."""
        seq = self._get_sequence()
        if not seq:
            return []
        counter = Counter(seq)
        max_freq = max(counter.values())
        return [val for val, freq in counter.items() if freq == max_freq]
    
    def variance(self, sample: bool = True) -> float:
        """Variance: if sample=True (default) use n-1, else population variance."""
        seq = self._get_sequence()
        n = len(seq)
        if n == 0:
            return 0.0
        mean = self.arithmetic_mean()
        sq_diff = sum((x - mean) ** 2 for x in seq)
        divisor = n - 1 if sample else n
        return sq_diff / divisor if divisor != 0 else 0.0
    
    def std_dev(self, sample: bool = True) -> float:
        """Standard deviation."""
        return math.sqrt(self.variance(sample))


class SequenceStats(StatisticsMixin):
    """Wrapper class that holds a sequence and provides statistical methods."""
    
    def __init__(self, data: List[float]):
        self._data = data
    
    def _get_sequence(self) -> List[float]:
        return self._data
    
    def __len__(self) -> int:
        return len(self._data)
    
    def __str__(self) -> str:
        return f"SequenceStats(n={len(self._data)}, mean={self.arithmetic_mean():.4f})"