from collections import namedtuple

# Define item prices
BREAD_PRICE = 5.50
CROISSANT_PRICE = 3.75

# Monday's sales
monday_bread = 24
monday_croissants = 42

# Calculate Tuesday's sales with increase
bread_increase = 0.20
pastry_increase = 0.15
tuesday_bread = int(monday_bread * (1 + bread_increase))
tuesday_croissants = int(monday_croissants * (1 + pastry_increase))

# Create a lambda to compute daily revenue
revenue_calculator = lambda bread_count, croissant_count: (bread_count * BREAD_PRICE) + (croissant_count * CROISSANT_PRICE)

# Calculate revenues
monday_revenue = revenue_calculator(monday_bread, monday_croissants)
tuesday_revenue = revenue_calculator(tuesday_bread, tuesday_croissants)

# Total combined revenue
combined_revenue = monday_revenue + tuesday_revenue

print(f"Result: {combined_revenue}")