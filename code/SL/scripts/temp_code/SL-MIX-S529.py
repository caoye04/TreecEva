from collections import Counter

# Daily sales quantities
sales_quantities = Counter({'croissants': 40, 'muffins': 30, 'scones': 20})

# Item prices
prices = {'croissants': 2.50, 'muffins': 1.75, 'scones': 3.00}

# Calculate total revenue using a lambda and ternary operator for discount application
is_weekend = True
discount_rate = 0.1 if is_weekend else 0

revenue_calc = lambda item, qty: qty * prices[item] * (1 - discount_rate)
total_revenue = sum(revenue_calc(item, qty) for item, qty in sales_quantities.items())

print(f'Result: {total_revenue}')