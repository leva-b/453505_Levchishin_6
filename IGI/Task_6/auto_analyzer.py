"""
Classes for analyzing Automobile dataset.
Lab 4, Task 6, Variant 6.
Developer: Ivan Leuchyshyn
Date: 2026-04-27
"""

import pandas as pd
import numpy as np
from abc import ABC, abstractmethod

class StatisticsMixin:
    """Mixin providing statistical helpers."""
    
    @staticmethod
    def safe_mean(series: pd.Series) -> float:
        """Return mean of non-null values, or 0 if empty."""
        if series.dropna().empty:
            return 0.0
        return series.mean()


class DataAnalyzer(ABC):
    """Abstract base class for data analyzers."""
    
    @abstractmethod
    def load_data(self):
        pass


class CarDataAnalyzer(DataAnalyzer, StatisticsMixin):
    """Analyzer for Automobile dataset."""
    
    _instance_count = 0   
    
    def __init__(self, dataframe: pd.DataFrame = None):
        if dataframe is not None:
            self._df = dataframe
        else:
            self._df = None
        self._id = CarDataAnalyzer._instance_count + 1
        CarDataAnalyzer._instance_count += 1
    
    @property
    def data(self) -> pd.DataFrame:
        return self._df
    
    @data.setter
    def data(self, value: pd.DataFrame):
        if not isinstance(value, pd.DataFrame):
            raise TypeError("Data must be a pandas DataFrame")
        self._df = value
    
    @property
    def id(self) -> int:
        return self._id
    
    def load_data(self, filepath: str = None):
        from .data_loader import load_automobile_dataset
        self._df = load_automobile_dataset(filepath)
        if self._df is not None:
            # Preprocess: convert price, cylinders, etc. to numeric
            self._df['price'] = pd.to_numeric(self._df['price'], errors='coerce')
            cylinder_map = {'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'eight':8, 'twelve':12}
            self._df['cylinders_num'] = self._df['num-of-cylinders'].map(cylinder_map)
        return self._df
    
    def create_car_features_df(self) -> pd.DataFrame:
        """
        Create a DataFrame from a list of lists, set columns, and change indices.
        This is the specific task for variant 6.
        """
        data_list = [
            ['Toyota', 'Camry', 24000],
            ['Honda', 'Accord', 22000],
            ['Ford', 'Mustang', 35000]
        ]
        columns = ['Make', 'Model', 'Price']
        df = pd.DataFrame(data_list, columns=columns)
        df.index = ['car_A', 'car_B', 'car_C']
        return df
    
    def average_price_max_cylinders(self) -> float:
        """Average price of cars with maximum number of cylinders (numeric)."""
        if self._df is None:
            return 0.0
        max_cyl = self._df['cylinders_num'].max()
        subset = self._df[self._df['cylinders_num'] == max_cyl]
        mean_price = subset['price'].mean()
        return round(mean_price, 2) if not pd.isna(mean_price) else 0.0
    
    def mpg_ratio_expensive_to_cheap(self) -> float:
        """
        Ratio of average city-mpg of cars in top price quartile to bottom price quartile.
        """
        if self._df is None:
            return 0.0
        clean = self._df.dropna(subset=['price', 'city-mpg'])
        if clean.empty:
            return 0.0
        
        lower_quartile = clean['price'].quantile(0.25)
        upper_quartile = clean['price'].quantile(0.75)
        cheap = clean[clean['price'] <= lower_quartile]
        expensive = clean[clean['price'] >= upper_quartile]
        if cheap.empty or expensive.empty:
            return 0.0
        mean_mpg_cheap = cheap['city-mpg'].mean()
        mean_mpg_expensive = expensive['city-mpg'].mean()
        if mean_mpg_cheap == 0:
            return 0.0
        ratio = mean_mpg_expensive / mean_mpg_cheap
        return round(ratio, 2)
    
    def demo_series_and_dataframe(self):
        """Show creation of Series, access via .loc/.iloc, etc."""
        print("\n--- Pandas Series demo ---")
        
        gender_series = pd.Series(['male','female','male','female','female'], 
                                  index=['P1','P2','P3','P4','P5'])
        print("gender_series:\n", gender_series)
        print("Access via .iloc[2]:", gender_series.iloc[2])
        print("Access via .loc['P4']:", gender_series.loc['P4'])
        
        crime_stats = pd.DataFrame({
            'district': [1,2,3],
            'crime_rate': [0.2, 0.5, 0.3],
            'avg_rooms': [6, 7, 5]
        })
        print("\nDataFrame from dict:\n", crime_stats)
        
        numpy_array = np.array([[1,2],[3,4]])
        df_from_numpy = pd.DataFrame(numpy_array, columns=['A','B'], index=['row1','row2'])
        print("\nDataFrame from NumPy:\n", df_from_numpy)
    
    def __str__(self):
        return f"CarDataAnalyzer(id={self._id}, data_shape={self._df.shape if self._df is not None else None})"
    
    def __repr__(self):
        return f"CarDataAnalyzer(dataframe={self._df is not None})"