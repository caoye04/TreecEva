from itertools import combinations

# Process inventory data for a warehouse
data_entries = [('A123', 15), ('B456', 8), ('C789', 12), ('D321', 6), ('E654', 18)]

# Initial processing with some unnecessary computations
processed_data = []
intermediate_sum = 0
temp_list = []

for entry in data_entries:
    item_code, quantity = entry
    processed_data.append((item_code, quantity * 2))
    intermediate_sum += quantity
    temp_list.append(item_code[::-1])  # Reverse codes (distractor)

# Filter items based on quantity threshold
filtered_items = []
threshold_check = 10

for item_code, doubled_quantity in processed_data:
    if doubled_quantity > threshold_check:
        filtered_items.append(item_code)
    # Add some irrelevant processing
    dummy_calc = len(item_code) * 3

# Unused combination calculation (distractor)
if len(filtered_items) >= 2:
    combos = list(combinations(filtered_items, 2))
    combo_count = len(combos)

# Final result calculation
final_count = len(filtered_items)

# Additional unused computations
remaining_items = len(data_entries) - final_count
backup_check = sum([q for _, q in data_entries])

print(f"Result: {final_count}")