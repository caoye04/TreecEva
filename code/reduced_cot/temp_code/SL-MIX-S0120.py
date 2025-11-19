from functools import reduce

def get_item_price(item_name):
    prices = {'croissant': 2.50, 'bagel': 1.75, 'muffin': 2.00}
    return prices.get(item_name, 0)

sold_items = [('croissant', 12), ('bagel', 8), ('muffin', 15)]

# Calculate revenue per item type
revenues = list(map(lambda x: get_item_price(x[0]) * x[1], sold_items))

# Sum all revenues to get total
total_revenue = reduce(lambda a, b: a + b, revenues)

print(f"Result: {total_revenue}")