# Define a protocol 'Stringable' that requires a __str__ method.
# Write a function 'join_strings(objects)' that takes a list of Stringable
# and returns their string representations concatenated with '|'.

from typing import List, Protocol, runtime_checkable

@runtime_checkable
class Stringable(Protocol):
    def __str__(self) -> str:
        ...

def join_strings(objects: List[Stringable]) -> str:
    """Takes a list of Stringable objects and joins their __str__ representations with '|'."""
    return "|".join(str(obj) for obj in objects)

# --- Testing ---

class CustomUser:
    def __init__(self, name: str):
        self.name = name
        
    def __str__(self) -> str:
        return f"User({self.name})"

# Test with int, float, and a custom class.

# Create a mixed list containing int, float, and the custom class
# All of these implicitly or explicitly satisfy the Stringable protocol
test_objects: List[Stringable] = [
    42, 
    3.14, 
    CustomUser("Alice")
]

# Run the function
result = join_strings(test_objects)
print(result)
# Output: 42|3.14|User(Alice)