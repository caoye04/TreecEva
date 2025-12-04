product_codes = ['A123', 'B456', 'C789', 'D012', 'E345']
active_codes = ['A123', 'C789', 'E345']

# Filter active products using set intersection
active_set = set(product_codes)
reference_set = set(active_codes)
valid_items = active_set.intersection(reference_set)

# Process multiplier based on conditions
base_value = 3
if len(valid_items) > 2:
    multiplier = base_value + 1
else:
    multiplier = base_value - 1

# Calculate final count
final_count = len(valid_items) * multiplier
print(f"Target result: {final_count}")