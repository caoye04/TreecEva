import itertools

# Analyzing digital product combinations
digits = [2, 3, 5, 7, 9]
colors = ['red', 'blue', 'green']

# Generate all possible 2-digit combinations
combinations = list(itertools.product(digits, repeat=2))

# Calculate product of each combination
product_values = []
for combo in combinations:
    product = combo[0] * combo[1]
    product_values.append(product)

# Filter combinations where product is divisible by 3
filtered_combinations = []
for value in product_values:
    if value % 3 == 0:
        filtered_combinations.append(value)

# Count unique products that meet our criteria
unique_combinations = len(set(filtered_combinations))

# Additional metrics (not used in final calculation)
total_possible = len(digits) ** 2
average_product = sum(product_values) / len(product_values)

print(f"Result: {unique_combinations}")