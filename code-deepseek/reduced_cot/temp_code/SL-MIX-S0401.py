from collections import Counter

# Process inventory data with quality checks
inventory_counts = {'widgets': 45, 'gadgets': 32, 'tools': 28, 'parts': 51}
supply_orders = [('widgets', 15), ('gadgets', 8), ('tools', 12), ('parts', 20)]

# Calculate total incoming supply (distractor - not used)
total_incoming = sum(order[1] for order in supply_orders)

# Process inventory with quality filtering
quality_scores = {'widgets': 0.85, 'gadgets': 0.92, 'tools': 0.78, 'parts': 0.95}
filtered_inventory = {item: count for item, count in inventory_counts.items() 
                     if quality_scores[item] > 0.8}

# Calculate adjusted counts with processing loss
processing_loss_factor = 0.03
adjusted_counts = {item: int(count * (1 - processing_loss_factor)) 
                  for item, count in filtered_inventory.items()}

# Convert to list and apply additional processing (distractor)
processed_data = list(adjusted_counts.values())
intermediate_sum = sum(processed_data)  # Not used in final calculation

# Apply final adjustment factor
adjustment_factor = lambda x: x * 1.05 if x > 30 else x * 0.95
final_output = processed_data[-1] + adjustment_factor(processed_data[0])

print(f"Target result: {final_output}")