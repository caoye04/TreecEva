inventory_counts = [45, 23, 67, 12, 89, 34, 56]
processed_items = []
odd_count = 0

# Process inventory with some intermediate calculations
for idx, count in enumerate(inventory_counts):
    processed_items.append(count * 2 if idx % 2 == 0 else count + 10)
    if count % 2 != 0:
        odd_count += count

# Some intermediate calculations that don't affect final result
inventory_sum = sum(inventory_counts)
average_count = inventory_sum / len(inventory_counts)

# Sort and filter relevant values
filtered_values = [x for x in processed_items if x > 30]
sorted_values = sorted(filtered_values)

# Distractor calculation that seems relevant but isn't used
distractor_sum = sum(sorted_values) // len(sorted_values) if sorted_values else 0

# Final calculation using conditional expression
final_result = sorted_values[odd_count % 3] if len(sorted_values) > (odd_count % 3) else -1

print(f"Target result: {final_result}")