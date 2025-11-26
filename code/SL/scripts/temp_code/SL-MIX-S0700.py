from collections import Counter

# Inventory management system analysis
initial_stock = ["widget_a", "widget_b", "widget_a", "widget_c", "widget_b", "widget_a", "widget_d"]

# Process inventory counts with list comprehension
inventory_counts = Counter(initial_stock)
total_items = len(initial_stock)

# Calculate various metrics (some are distractors)
avg_per_item = total_items / len(inventory_counts)
most_common_item = inventory_counts.most_common(1)[0][0]
item_diversity = len(inventory_counts)

# Unused intermediate calculation
potential_stock_adjustment = avg_per_item * 2 - 1

# Filter out low-stock items
threshold = 2
remaining_items = [item for item, count in inventory_counts.items() if count >= threshold]
remaining_stock = sum(inventory_counts[item] for item in remaining_items)

# Final calculation (answer)
final_inventory_count = remaining_stock

# Print result for verification
print(f"Result: {final_inventory_count}")