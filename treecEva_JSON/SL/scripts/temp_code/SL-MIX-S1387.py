from collections import defaultdict

# Prices of items
bakery_prices = {'croissant': 2.5, 'muffin': 3.0, 'scone': 2.0}

# Quantities sold in a day
sales_quantities = [20, 15, 10]  # croissants, muffins, scones

# Calculate total revenue
revenue_components = map(lambda item, qty: bakery_prices[item] * qty, ['croissant', 'muffin', 'scone'], sales_quantities)
total_revenue = sum(revenue_components)

print(f"Total revenue: {total_revenue}")
