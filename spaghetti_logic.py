from typing import List, Optional

# Constants
MARKUP_COEFFICIENT = 1.15


def calculate_with_markup(
    values: List[float], coefficient: float = MARKUP_COEFFICIENT
) -> List[float]:
    """
    Apply a markup coefficient to each value in the list.
    
    Pure function with no side effects - suitable for unit testing.
    
    Args:
        values: List of numeric values to process
        coefficient: Multiplication factor (default: 1.15)
    
    Returns:
        List of values multiplied by the coefficient
    
    Raises:
        TypeError: If values is not a list or contains non-numeric items
        ValueError: If coefficient is negative or zero
    """
    if not isinstance(values, list):
        raise TypeError(f"Expected list, got {type(values).__name__}")
    
    if not values:
        return []
    
    if coefficient <= 0:
        raise ValueError(f"Coefficient must be positive, got {coefficient}")
    
    try:
        return [float(v) * coefficient for v in values]
    except (TypeError, ValueError) as e:
        raise TypeError(f"Cannot process non-numeric value in list: {e}")


def log_to_file(data: List[float], filepath: str) -> None:
    """
    Write processed data to a log file.
    
    Args:
        data: List of processed values to log
        filepath: Path to the log file
    
    Raises:
        IOError: If file cannot be written
    """
    try:
        with open(filepath, "a") as f:
            f.write(str(data) + "\n")
    except IOError as e:
        raise IOError(f"Failed to write to {filepath}: {e}")


def format_and_display(value: float, format_spec: str = ".2f") -> str:
    """
    Format a numeric value as a string for display.
    
    Args:
        value: Numeric value to format
        format_spec: Python format specification (default: ".2f")
    
    Returns:
        Formatted string
    """
    return f"Total: {value:{format_spec}}"


def process_data(
    data: List[float],
    log_filepath: Optional[str] = None,
    enable_logging: bool = False
) -> List[float]:
    """
    Process data by applying markup coefficient and optional logging.
    
    Orchestrates the workflow: calculation → display → optional file logging.
    
    Args:
        data: List of numeric values to process
        log_filepath: Path to log file (required if enable_logging=True)
        enable_logging: If True, log results to file and print to console
    
    Returns:
        List of processed values (multiplied by MARKUP_COEFFICIENT)
    
    Raises:
        TypeError: If data contains non-numeric items
        ValueError: If data format is invalid
        IOError: If logging fails
    """
    # Step 1: Calculate with markup (pure function)
    processed_values = calculate_with_markup(data)
    
    # Step 2: Display and log (if enabled)
    if enable_logging:
        for value in processed_values:
            formatted = format_and_display(value)
            print(formatted)
        
        # Write to file only if path is provided
        if log_filepath:
            log_to_file(processed_values, log_filepath)
    
    return processed_values
