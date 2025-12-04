from collections import Counter

# Simulate inventory tracking with intervention level 7
initial_stock = [5, 12, 8, 15, 3, 9, 7, 11]
restock_items = [2, 4, 6, 8, 10]

# Primary calculation path with relevant operations
stock_counter = Counter(initial_stock)
restock_counter = Counter(restock_items)

# Combined inventory after restocking
combined_inventory = stock_counter + restock_counter

# Calculate total items (this affects final result)
base_total = sum(combined_inventory.values())

# Distractor operations that don't affect final result
partial_sum = sum(item for item in initial_stock if item % 2 == 0)
weight_factor = len(restock_items) * 1.5

# Key calculations with moderate nesting
processing_adjustment = 0
for item, count in combined_inventory.items():
    if count > 1:
        processing_adjustment += item * (count - 1)

# Intermediate variable not used in final answer
intermediate_value = processing_adjustment // len(initial_stock)

# Final computation chain
final_adjustment = base_total - processing_adjustment
offset_correction = (final_adjustment % 3) * 2

# Target variable and execution point
processed_total = final_adjustment * 2 - offset_correction

print(f"Result: {processed_total}")