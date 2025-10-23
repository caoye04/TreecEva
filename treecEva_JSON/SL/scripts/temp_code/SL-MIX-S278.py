from functools import reduce

item_prices = {'bread': 2.50, 'croissant': 3.75, 'muffin': 4.25}
items_sold = [12, 8, 15]  # bread, croissant, muffin counts

# Calculate revenue per item type
revenue_per_item = list(map(lambda count, price: count * price, items_sold, item_prices.values()))

# Sum up all revenues
total_revenue = reduce(lambda x, y: x + y, revenue_per_item)

print(f"Result: {total_revenue}")