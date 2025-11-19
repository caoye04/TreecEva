from functools import reduce

# Price and quantity data for each pastry type
pastry_sales = [
    {'name': 'croissant', 'price': 2.5, 'quantity': 40},
    {'name': 'muffin', 'price': 3.0, 'quantity': 30},
    {'name': 'danish', 'price': 3.5, 'quantity': 20}
]

# Calculate revenue per item using map and lambda
revenues = list(map(lambda item: item['price'] * item['quantity'], pastry_sales))

# Sum all revenues using reduce
total_revenue = reduce(lambda x, y: x + y, revenues)

print(f"Total revenue: {total_revenue}")