# modules/common/__init__.py
"""
Common utilities module initialization.
Exports commonly used functions for all tasks.
"""

from .input_utils import (
    get_float_input,
    get_int_input,
    get_string_input,
    get_continue_choice
)

from .validation import (
    validate_number_range,
    validate_positive,
    validate_non_negative,
    validate_list_not_empty,
    validate_list_size,
    is_binary_string,
    is_hex_string,
    is_octal_string
)

from .decorators import (
    log_execution,
    timer,
    validate_input,
    retry
)

from .init_methods import (
    generator_sequence_generator,
    manual_sequence_input,
    random_sequence_generator,
    get_initialization_method,
    initialize_sequence,
    get_float_sequence_from_user,
    get_int_sequence_from_user
)

__all__ = [
    # Input utilities
    'get_float_input',
    'get_int_input',
    'get_string_input',
    'get_continue_choice',
    # Validation
    'validate_number_range',
    'validate_positive',
    'validate_non_negative',
    'validate_list_not_empty',
    'validate_list_size',
    'is_binary_string',
    'is_hex_string',
    'is_octal_string',
    # Decorators
    'log_execution',
    'timer',
    'validate_input',
    'retry',
    # Init methods
    'generator_sequence_generator',
    'manual_sequence_input',
    'random_sequence_generator',
    'get_initialization_method',
    'initialize_sequence',
    'get_float_sequence_from_user',
    'get_int_sequence_from_user'
]