# Create a dictionary called 'operations' that maps strings '+', '-', '*', '/'
# to their respective functions from the 'operator' module.
#
import operator


operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '**': operator.pow  # BONUS: Add a '**' operation for power.
}

# Then, write a function `calculate(a, b, op)` that looks up the function
# and applies it.

def calculate(a, b, op):
    if op in operations:
        return operations[op](a, b)
    else:
        raise ValueError("Invalid operation")
    
print(calculate(2, 3, '+'))  # Output: 5
print(calculate(5, 2, '-'))  # Output: 3
print(calculate(4, 3, '*'))  # Output: 12
print(calculate(10, 2, '/'))  # Output: 5.0
print(calculate(2, 3, '**'))  # Output: 8
# BONUS: Add a '**' operation for power.