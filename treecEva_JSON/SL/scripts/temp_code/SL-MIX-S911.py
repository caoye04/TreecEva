from functools import reduce

item_prices = {'croissant': 3.50, 'muffin': 2.75, 'scone': 2.25}
quantities_sold = [24, 15, 9]
item_names = ['croissant', 'muffin', 'scone']

# Calculate individual revenues using map
individual_revenues = list(map(lambda name, qty: item_prices[name] * qty, item_names, quantities_sold))

# Sum all revenues using reduce
total_revenue = reduce(lambda x, y: x + y, individual_revenues)

print(f'Result: {total_revenue}')