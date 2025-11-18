from functools import reduce

# Prices per unit for ingredients (flour, sugar, butter, eggs)
ingredient_prices = [0.5, 0.3, 1.2, 0.2]

# Quantities needed for one batch of croissants
quantities = [2, 1, 3, 4]

# Lambda function to calculate cost of each ingredient
cost_calculator = lambda price, qty: price * qty

# Calculate individual costs using map
individual_costs = list(map(cost_calculator, ingredient_prices, quantities))

# Sum up all costs using reduce
total_cost = reduce(lambda x, y: x + y, individual_costs)

print(f'Result: {total_cost}')