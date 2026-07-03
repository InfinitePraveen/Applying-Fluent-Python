# Write a decorator @timer that prints how long a function took to run.
# Example:
# @timer
# def slow_function():
#     time.sleep(2)

import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()      # Record the starting time
        result = func(*args, **kwargs)        # Execute the original function
        end_time = time.perf_counter()        # Record the ending time
        
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' took {execution_time:.6f} seconds to run.")
        
        return result                         # Return the original function's output
    return wrapper

# --- Usage ---

@timer
def process_data(n):
    """Simulates a data processing loop."""
    total = 0
    for i in range(n):
        total += i
    return total

# Call the decorated function
result = process_data(10_000_000)
print(f"Result: {result}")


# Output: "slow_function took 2.0001 seconds"