# Script to convert temperature between Celsius and Fahrenheit with global variables for conversion factors.

# Global variables to store temperature conversion factors.
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Function to convert Fahrenheit to Celsius.
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# Function to convert Celsius to Fahrenheit.
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# Get user input and output with error for invalid temperature inputs.
def main():
    temp = float(input("Enter the temperature to convert: "))
    scale = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if scale == "C":
        new_temp = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {new_temp}°F")
    elif scale == "F":
        new_temp = convert_to_celsius(temp)
        print(f"{temp}°F is {new_temp}°C")
    else:
        print("Invalid temperature. Please enter a numeric value.")

# Call the function
if __name__ == "__main__":
    main()