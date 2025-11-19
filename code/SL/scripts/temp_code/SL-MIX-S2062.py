from functools import reduce

prices = [2.50, 1.75, 3.00]
quantities = [40, 25, 30]

# Calculate revenue per item
revenues = list(map(lambda p, q: p * q, prices, quantities))

# Total revenue
initial_revenue = reduce(lambda x, y: x + y, revenues)

# Apply discount using ternary operator
final_revenue = initial_revenue * 0.9 if initial_revenue > 150 else initial_revenue

print(f'Result: {final_revenue}')