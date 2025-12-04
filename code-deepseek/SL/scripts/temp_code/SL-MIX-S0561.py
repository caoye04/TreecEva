from collections import Counter

# Inventory analysis for warehouse stock
product_counts = [12, 8, 15, 8, 20, 12, 12, 8, 15, 10]
count_freq = Counter(product_counts)

# Find most common inventory level
most_common = count_freq.most_common(1)[0]
target_value = most_common[0] + most_common[1]

# Calculate adjustment factor
modifier = len([x for x in product_counts if x > 10]) / 2

# Final computation
final_result = target_value * modifier
print(f"Result: {final_result}")