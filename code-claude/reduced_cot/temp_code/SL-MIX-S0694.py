import itertools

# Analyzing product inventory overlap between two stores
store_a = [101, 103, 105, 107, 109, 110]
store_b = [102, 104, 105, 107, 110, 112]

# Find common items between stores
common_items = set(store_a).intersection(set(store_b))

# Generate all possible pairs of items from store A
pairs = list(itertools.combinations(store_a, 2))

# Select items whose ID is present in both pairs and common items
selected_items = []
for pair in pairs:
    avg_id = sum(pair) / 2
    if avg_id > 105:
        selected_items.extend(pair)

# Count unique elements in the selection
unique_elements = len(set(selected_items))

# Calculate final inventory metric
inventory_metric = unique_elements + len(common_items)

print(f"Result: {unique_elements}")