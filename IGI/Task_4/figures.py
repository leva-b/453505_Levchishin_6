"""
Geometric figures: abstract base class, Color, Rhombus.
Lab 4, Task 4, Variant 6.
Developer: Ivan Leuchyshyn
Date: 2026-04-25
"""

import math
from abc import ABC, abstractmethod

class Color:
    """Class representing a fill color for a figure."""
    
    def __init__(self, name: str):
        """name: color name recognized by matplotlib (e.g., 'blue', 'red', '#FF00FF')."""
        self._name = name
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str):
        if not value or not isinstance(value, str):
            raise ValueError("Color name must be a non-empty string")
        self._name = value
    
    def __str__(self) -> str:
        return self._name


class GeometricFigure(ABC):
    """Abstract base class for all geometric figures."""
    
    @abstractmethod
    def area(self) -> float:
        """Calculate area of the figure."""
        pass
    
    @classmethod
    @abstractmethod
    def get_figure_name(cls) -> str:
        """Return the name of the figure (class-level)."""
        pass


class Rhombus(GeometricFigure):
    """Rhombus defined by side length and acute angle (in degrees)."""
    
    _figure_name = "Rhombus"   
    
    def __init__(self, side: float, acute_angle_deg: float, color: Color):
        self._side = side
        self._acute_angle_deg = acute_angle_deg
        self._color = color
        self._acute_angle_rad = math.radians(acute_angle_deg)
    
    @property
    def side(self) -> float:
        return self._side
    
    @side.setter
    def side(self, value: float):
        if value <= 0:
            raise ValueError("Side length must be positive")
        self._side = value
    
    @property
    def acute_angle_deg(self) -> float:
        return self._acute_angle_deg
    
    @acute_angle_deg.setter
    def acute_angle_deg(self, value: float):
        if not (0 < value < 90):
            raise ValueError("Acute angle must be between 0 and 90 degrees")
        self._acute_angle_deg = value
        self._acute_angle_rad = math.radians(value)
    
    @property
    def color(self) -> Color:
        return self._color
    
    @color.setter
    def color(self, value: Color):
        self._color = value
    
    def area(self) -> float:
        """Area = side^2 * sin(acute_angle)."""
        return self._side * self._side * math.sin(self._acute_angle_rad)
    
    @classmethod
    def get_figure_name(cls) -> str:
        return cls._figure_name
    
    def get_info(self) -> str:
        """Return formatted string with parameters, color, and area."""
        info = (f"Figure: {self.get_figure_name()}\n"
                f"Side: {self._side:.2f}\n"
                f"Acute angle: {self._acute_angle_deg:.2f}°\n"
                f"Color: {self._color}\n"
                f"Area: {self.area():.2f} sq. units")
        return info
    
    def __str__(self) -> str:
        return f"Rhombus(side={self._side}, angle={self._acute_angle_deg}°, color={self._color})"
    
    def get_vertices(self) -> list:
        """
        Return list of (x, y) tuples for the rhombus vertices.
        The rhombus is centered at (0,0) with horizontal and vertical diagonals.
        Acute angle at left and right vertices.
        """
        # half-diagonals
        half_d1 = self._side * math.cos(self._acute_angle_rad / 2)
        half_d2 = self._side * math.sin(self._acute_angle_rad / 2)
        vertices = [
            ( half_d1,  0.0     ),   # right vertex
            ( 0.0,       half_d2),   # top vertex
            (-half_d1,  0.0     ),   # left vertex
            ( 0.0,      -half_d2)    # bottom vertex
        ]
        return vertices