from collections import Counter

# Analyze inventory data
inventory_data = ['A', 'B', 'C', 'A', 'A', 'B', 'D', 'E', 'A', 'C']
category_counts = Counter(inventory_data)

# Initial processing - some operations are relevant, some are not
total_items = len(inventory_data)
processing_fee = total_items * 2  # This doesn't affect final result

# Filter categories with count > 1 and create processed list
filtered_data = []
for item, count in category_counts.items():
    if count > 1:
        filtered_data.append(count)

# Some intermediate calculations that aren't used in final answer
intermediate_sum = sum(filtered_data)
redundant_calc = intermediate_sum * 0.1

# Process the filtered data further
processed_values = [x * 2 for x in filtered_data]
adjustment = len(processed_values) - 2

# The critical execution point
final_count = filtered_data[-1] + adjustment

print(f"Result: {final_count}")