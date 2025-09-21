# Get number for multiplication table from user
number = int(input("Enter a number to see its multiplication table: "))

# Loop to get multiplication from 1 to 10
for multiplier in range(1, 11):
    product = number * multiplier
    print(f"{number} * {multiplier} = {product}")
    multiplier + 1
