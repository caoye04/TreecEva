import itertools

# Product inventory data with prices and weights
products = {
    'apple': {'price': 1.20, 'weight': 0.15},
    'banana': {'price': 0.50, 'weight': 0.18},
    'orange': {'price': 0.80, 'weight': 0.22},
    'grape': {'price': 2.50, 'weight': 0.10},
    'kiwi': {'price': 0.90, 'weight': 0.08}
}

# Calculate price per kg for each product
for product, info in products.items():
    info['price_per_kg'] = info['price'] / info['weight']

# Extract price per kg values
price_per_kg_values = list(map(lambda x: x['price_per_kg'], products.values()))

# Filter values between thresholds
min_threshold = 5.0
max_threshold = 12.0
filtered_values = list(filter(lambda x: min_threshold <= x <= max_threshold, price_per_kg_values))

# Calculate average of filtered values
filtered_average = sum(filtered_values) / len(filtered_values)

print(f"Result: {filtered_average}")