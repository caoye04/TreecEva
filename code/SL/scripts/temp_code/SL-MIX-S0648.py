from functools import reduce

# Base price per pastry
base_price = 2.50

# Lambda function to calculate discount based on quantity
apply_discount = lambda quantity: (quantity // 5) * 1.00

# Number of pastries purchased
pastries_bought = 17

# Calculate gross cost before discount
gross_cost = pastries_bought * base_price

# Calculate total discount
total_discount = apply_discount(pastries_bought)

# Calculate final total cost
total_cost = gross_cost - total_discount

print(f"Result: {total_cost}")