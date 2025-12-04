from collections import Counter

# Process inventory data for different warehouse sections
inventory_counts = [15, 8, 23, 15, 8, 42, 15, 23, 8]
count_freq = Counter(inventory_counts)

# Calculate processing factors (some operations are distractor)
total_items = sum(inventory_counts)
weighted_sum = sum([count * freq for count, freq in count_freq.items()])
avg_weight = weighted_sum / total_items if total_items > 0 else 0

# Main processing logic (relevant operations)
unique_counts = len(count_freq)
most_common_count, most_common_freq = count_freq.most_common(1)[0]
processed_count = unique_counts * most_common_freq

# Additional computations (partially relevant)
factor = (len(inventory_counts) + unique_counts) // 2
secondary_factor = factor * 2 - 1  # Distractor calculation

# Final computation (key statement)
adjustment = total_items % (unique_counts + 1)
final_computation = (processed_count * factor) - adjustment

# Print target result
print(f"Target result: {final_computation}")