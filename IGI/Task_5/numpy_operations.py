"""
NumPy matrix operations for Task 5, Variant 6.
Lab 4, Task 5.
Developer: Ivan Leuchyshyn
Date: 2026-04-27
"""

import numpy as np
import math

class MatrixAnalyzer:
    """Class to hold a random integer matrix and perform required operations."""
    
    _instance_count = 0   
    
    def __init__(self, rows: int, cols: int, low: int = -100, high: int = 100):
        """
        Create a random integer matrix of shape (rows, cols) with values in [low, high).
        """
        self._rows = rows
        self._cols = cols
        self._low = low
        self._high = high
        self._matrix = np.random.randint(low, high, size=(rows, cols))
        MatrixAnalyzer._instance_count += 1
        self._id = MatrixAnalyzer._instance_count   
    
    @property
    def matrix(self) -> np.ndarray:
        return self._matrix
    
    @property
    def shape(self) -> tuple:
        return self._matrix.shape
    
    def get_negative_odd_elements(self) -> np.ndarray:
        """Return 1D array of elements that are negative and odd."""
        
        mask = (self._matrix < 0) & (self._matrix % 2 != 0)
        return self._matrix[mask]
    
    def sum_of_abs_negative_odd(self) -> int:
        """Sum of absolute values of negative odd elements."""
        elements = self.get_negative_odd_elements()
        if len(elements) == 0:
            return 0
        return np.sum(np.abs(elements))
    
    def std_numpy(self, elements: np.ndarray) -> float:
        """Standard deviation using numpy.std (ddof=1 for sample std)."""
        if len(elements) <= 1:   
            return 0.0
        return np.std(elements, ddof=1)
    
    def std_formula(self, elements: np.ndarray) -> float:
        """Standard deviation calculated manually: sqrt(sum((x - mean)^2)/(n-1))."""
        n = len(elements)
        if n <= 1:   
            return 0.0
        mean = np.mean(elements)
        variance = np.sum((elements - mean) ** 2) / (n - 1)
        return math.sqrt(variance)
    
    def compare_std(self) -> tuple:
        """Return (numpy_std, formula_std, are_close)."""
        elems = self.get_negative_odd_elements()
        if len(elems) <= 1:
            return (0.0, 0.0, True)
        np_std = self.std_numpy(elems)
        form_std = self.std_formula(elems)
        return (np_std, form_std, math.isclose(np_std, form_std, rel_tol=1e-9))
    
    def demonstrate_indexing_slicing(self) -> None:
        """Print examples of indexing and slicing."""
        print("\n--- NumPy Indexing & Slicing Demo ---")
        print(f"Matrix shape: {self.shape}")
        print("First row:", self._matrix[0, :])
        print("Last column:", self._matrix[:, -1])
        print("Submatrix (rows 1..3, cols 0..2):\n", self._matrix[1:4, 0:3])
        
        print("Setting a slice to 999 (temporary demo)...")
        temp = self._matrix.copy()
        temp[0, :2] = 999
        print("After setting first row, first two columns to 999:\n", temp[:2, :3])
    
    def demonstrate_ufuncs(self) -> None:
        """Show element-wise operations."""
        print("\n--- Universal Functions (ufuncs) Demo ---")
        flat = self._matrix.flatten()
        print("Absolute value (first 5 elements):", np.abs(flat[:5]))
        print("Square root of absolute values (first 5):", np.sqrt(np.abs(flat[:5])))
        print("Element-wise addition of 10 to first row:", self._matrix[0] + 10)
    
    def __str__(self) -> str:
        return f"MatrixAnalyzer(id={self._id}, shape={self.shape})"
    
    def __repr__(self) -> str:
        return f"MatrixAnalyzer(rows={self._rows}, cols={self._cols}, low={self._low}, high={self._high})"
    
    @classmethod
    def get_instance_count(cls) -> int:
        return cls._instance_count