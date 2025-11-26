data_stream = [15, 28, 42, 57, 63, 71, 89, 94]

# Process each item with integer division and rounding
processed_items = [item // 3 for item in data_stream]

# Additional processing step (distractor)
temp_sum = sum(processed_items[:3])

# Calculate final result using slicing operations
final_result = processed_items[2] + processed_items[4]

print(f"Result: {final_result}")