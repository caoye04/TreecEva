from collections import defaultdict

# Prices of bakery items
item_prices = {'croissant': 2.5, 'muffin': 1.8, 'scone': 2.0}

# Quantities sold today
quantities_sold = {'croissant': 40, 'muffin': 30, 'scone': 25}

# Calculate total revenue using list comprehension
total_revenue = sum([item_prices[item] * quantities_sold[item] for item in item_prices])

print(f'Result: {total_revenue}')