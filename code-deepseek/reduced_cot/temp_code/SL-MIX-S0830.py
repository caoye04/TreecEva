from collections import Counter

# Process inventory data
inventory_data = ["apple", "banana", "apple", "cherry", "banana", "apple", "date", "elderberry", "fig"]
processed_items = [item.upper() for item in inventory_data if len(item) > 3]

# Count items and perform analysis
item_counts = Counter(processed_items)
primary_items = ["APPLE", "BANANA", "CHERRY"]
secondary_items = ["DATE", "ELDERBERRY", "FIG"]

# Relevant calculations
valid_items = sum(item_counts[item] for item in primary_items)
secondary_count = sum(item_counts[item] for item in secondary_items)

# Distractor calculations that don't affect final result
total_processed = len(processed_items)
average_length = sum(len(item) for item in processed_items) / len(processed_items) if processed_items else 0

# More distraction operations
unused_calculation = (total_processed * 2) - secondary_count
irrelevant_sum = valid_items + secondary_count + total_processed

# Key adjustment (relevant)
secondary_adjustment = secondary_count // 2 if secondary_count > 0 else 1

# Final calculation
final_count = valid_items + secondary_adjustment

print(f"Result: {final_count}")