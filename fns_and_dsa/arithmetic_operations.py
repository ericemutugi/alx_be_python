# Python script to perform basic arithmetic operations.

# Function named perform_operation that takes parameters num1 (float), num2 (float), and operation (str).
# operation can be one of the following strings: 'add', 'subtract', 'multiply', 'divide'.
def perform_operation(num1: float, num2: float, operation: str) -> float:
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")
        return num1 / num2
    else:
        raise ValueError("Invalid operation. Supported operations: add, subtract, multiply, divide.")