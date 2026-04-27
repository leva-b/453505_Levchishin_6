"""
Serialization/deserialization to CSV and pickle formats.
Lab 4, Task 1, Variant 6.
Version: 1.0
Developer: Ivan Leuchyshyn
Date: 2026-04-23
"""
import csv
import pickle
from abc import ABC, abstractmethod
from typing import List, Dict, Any

class Serializer(ABC):
    """Abstract base class for serializers (polymorphism)."""

    @staticmethod
    @abstractmethod
    def save(data: List[Dict[str, Any]], filepath: str) -> None:
        pass

    @staticmethod
    @abstractmethod
    def load(filepath: str) -> List[Dict[str, Any]]:
        pass

class CSVSerializer(Serializer):
    """CSV format serializer."""

    @staticmethod
    def save(data: List[Dict[str, Any]], filepath: str) -> None:
        if not data:
            return
        with open(filepath, 'w', newline ='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
    
    @staticmethod
    def load(filepath: str) -> List[Dict[str, Any]]:
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                return [row for row in reader]
        except FileNotFoundError:
            return []

class PickleSerializer(Serializer):
    """;Pickle format serializer"""

    @staticmethod
    def save(data: List[Dict[str, Any]], filepath: str) -> None:
        with open(filepath, 'wb') as file:
            pickle.dump(data, file)
    
    @staticmethod
    def load(filepath:str)-> List[Dict[str, Any]]:
        try:
            with open(filepath, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.PickleError):
            return []