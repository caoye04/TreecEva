import itertools

# Process inventory data to find items with sufficient stock
stock_levels = [12, 8, 15, 3, 20, 5, 18, 6]
min_threshold = 10

# Identify items above minimum stock threshold
adequate_stock = [level for level in stock_levels if level >= min_threshold]

# Calculate combinations of items that can be bundled
bundling_options = []
for r in range(1, len(adequate_stock) + 1):
    combinations = itertools.combinations(adequate_stock, r)
    for combo in combinations:
        if len(combo) >= 2:
            bundling_options.append(combo)

# Process the first valid bundling option
if bundling_options:
    first_bundle = bundling_options[0]
    result_set = set(first_bundle)
    filtered_sum = sum(result_set)
    print(f"Result: {filtered_sum}")
else:
    print("Result: 0")