from collections import Counter

# Warehouse inventory analysis
initial_stock = [15, 23, 15, 42, 23, 15, 8, 42, 15, 23]
stock_counter = Counter(initial_stock)

# Find most common item and its frequency
most_common_item, frequency = stock_counter.most_common(1)[0]
total_items = len(initial_stock)

# Calculate processing metrics
base_processing = frequency * 3
secondary_calc = total_items * 2  # This doesn't affect final result
temp_adjustment = most_common_item // 2  # Intermediate unused calculation

# Process items with efficiency factor
processed_items = base_processing + frequency
efficiency_factor = 1.75
adjustment_value = total_items - frequency

# Distraction calculations
unused_metric = (frequency * total_items) / 2
redundant_check = stock_counter[8] * 3  # Unused operation

# Final quantity calculation
final_quantity = processed_items * efficiency_factor - adjustment_value

print(f"Result: {final_quantity}")