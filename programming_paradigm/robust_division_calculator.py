# Python script containing division logic with error handling for division by zero and non-numeric inputs.
def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        if denominator == 0:
            return ZeroDivisionError("Error: Cannot divide by zero.")
        print("The result of the division is", numerator / denominator)
    except ValueError:
        return "Error: Please enter numeric values only."