# Write a function 'safe_divide(a, b)' that returns the result.
# Handle:
# - ZeroDivisionError -> return float('inf')
# - TypeError (if a or b is not number) -> return None
# - Any other exception -> raise a custom exception 'ComputationError'

class ComputationError(Exception):
    """Custom exception raised for unexpected errors during calculation."""
    pass

def safe_divide(a: any, b: any) -> float | None:
    try:
        return a / b
    except ZeroDivisionError:
        return float('inf')
    except TypeError:
        return None
    except Exception as e:
        # Wrap any other unexpected exceptions into our custom ComputationError
        raise ComputationError(f"An unexpected error occurred: {e}") from e