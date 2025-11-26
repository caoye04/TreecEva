from collections import Counter

# Analyze inventory discrepancies across warehouses
warehouse_data = [
    {'items': ['A', 'B', 'C', 'A', 'D'], 'id': 1},
    {'items': ['B', 'C', 'E', 'F', 'B'], 'id': 2},
    {'items': ['A', 'D', 'F', 'G', 'A'], 'id': 3}
]

# Intermediate computations (some distractor operations)
all_items = []
warehouse_counts = []

for wh in warehouse_data:
    item_count = Counter(wh['items'])
    warehouse_counts.append(item_count)
    all_items.extend(wh['items'])
    
# Distractor operation - not used in final result
unique_items = set(all_items)
total_unique = len(unique_items)

# Main analysis
overall_counter = Counter(all_items)
common_items = [item for item, count in overall_counter.items() if count >= 2]

# More intermediate steps
item_positions = {}
for idx, item in enumerate(common_items):
    item_positions[item] = idx

# Calculate inventory ratios (distractor)
ratios = []
for wh_count in warehouse_counts:
    ratio = sum(wh_count.values()) / len(wh_count) if wh_count else 0
    ratios.append(ratio)

# Core logic for finding target warehouses
valid_warehouses = []
for i, wh in enumerate(warehouse_data):
    common_in_wh = [item for item in common_items if item in wh['items']]
    if len(common_in_wh) >= 2:
        valid_warehouses.append(i)

# Final result calculation
final_results = []
for idx in valid_warehouses:
    wh_items = warehouse_data[idx]['items']
    item_freq = Counter(wh_items)
    max_freq = max(item_freq.values()) if item_freq else 0
    final_results.append(max_freq * len(wh_items))

# Target operation
valid_indices = [i for i, val in enumerate(final_results) if val > 0]
target_value = final_results[valid_indices[-1]]

print(f"Target result: {target_value}")