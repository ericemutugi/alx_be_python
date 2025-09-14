# Script to calculate user's finance

# Request user to give monthly income and total monthly expenses and save inputs to variables
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

# Calculate monthly savings and save to variable
monthly_savings = monthly_income - monthly_expenses

# Calculate projected annual savings with 5% interest and save to variable
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Print user's monthly savings and projected annual savings after interest
print("Your monthly savings are:", monthly_savings, ".")
print("Projected savings after one year, with interest, is:", projected_savings, ".")