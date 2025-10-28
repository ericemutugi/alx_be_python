# Script performs various datetime operations and prints the results.
from datetime import datetime, timedelta

# Function to print current date and time in format YYYY-MM-DD HH:MM:SS and store it in variable current_date.
def display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", current_date)
    return current_date

# Function to calculate a future date by prompting user for number of days to add.
def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.now() + timedelta(days=number_of_days)
    print("Future date: ", future_date.strftime("%Y-%m-%d"))
    return future_date

# Call the functions
if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
