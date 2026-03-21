"""
Module: decorators.py
Description: Common decorators for all tasks
Lab: Laboratory Work No. 3
Version: 1.0
Author: Ivan Leuchyshyn
Date: 2026-03-21
"""

import time
import functools
from typing import Any, Callable


def log_execution(func: Callable) -> Callable:
    """
    Decorator that logs function execution details.
    
    Args:
        func: Function to decorate
    
    Returns:
        Wrapped function with logging
    
    Example:
        >>> @log_execution
        ... def calculate(x, y):
        ...     return x + y
        >>> calculate(5, 3)
        ==================================================
        [LOG] Executing: calculate
        [LOG] Arguments: (5, 3), {}
        [LOG] Execution time: 0.001 ms
        [LOG] Result: 8
        ==================================================
        8
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\n{'='*50}")
        print(f"[LOG] Executing: {func.__name__}")
        print(f"[LOG] Arguments: {args}, {kwargs}")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"[LOG] Execution time: {(end_time - start_time)*1000:.3f} ms")
        print(f"[LOG] Result: {result}")
        print(f"{'='*50}")
        return result
    return wrapper


def timer(func: Callable) -> Callable:
    """
    Decorator that measures execution time.
    
    Args:
        func: Function to decorate
    
    Returns:
        Wrapped function with timing
    
    Example:
        >>> @timer
        ... def slow_function():
        ...     time.sleep(1)
        ...     return "Done"
        >>> slow_function()
        [INFO] slow_function took 1000.234 ms
        'Done'
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"\n[INFO] {func.__name__} took {(end_time - start_time)*1000:.3f} ms")
        return result
    return wrapper


def validate_input(validator: Callable) -> Callable:
    """
    Decorator that validates input before function execution.
    
    Args:
        validator: Function that takes args and kwargs and returns bool
    
    Returns:
        Wrapped function with validation
    
    Example:
        >>> def positive_args(*args, **kwargs):
        ...     return all(a > 0 for a in args)
        >>> @validate_input(positive_args)
        ... def divide(a, b):
        ...     return a / b
        >>> divide(10, 2)
        5.0
        >>> divide(10, -2)
        ValueError: Input validation failed
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if validator(*args, **kwargs):
                return func(*args, **kwargs)
            else:
                raise ValueError("Input validation failed")
        return wrapper
    return decorator


def retry(max_attempts: int = 3, error_msg: str = "Operation failed"):
    """
    Decorator that retries function execution on exception.
    
    Args:
        max_attempts: Maximum number of retry attempts
        error_msg: Error message to display on failure
    
    Returns:
        Decorated function with retry logic
    
    Example:
        >>> @retry(max_attempts=3)
        ... def unstable_operation():
        ...     import random
        ...     if random.random() < 0.7:
        ...         raise ValueError("Random failure")
        ...     return "Success"
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt + 1}/{max_attempts} failed: {e}")
                    if attempt == max_attempts - 1:
                        raise Exception(f"{error_msg} after {max_attempts} attempts")
            return None
        return wrapper
    return decorator