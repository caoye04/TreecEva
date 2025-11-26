def data_processor(raw_values):
    # Irrelevant processing for distraction
    temp_sum = sum([x * 2 for x in raw_values if x % 3 == 0])
    misleading_value = temp_sum // len(raw_values) if len(raw_values) > 0 else 0
    
    # Actual relevant processing
    filtered_data = [x for x in raw_values if x % 2 == 0]
    processed = [x * 3 + 1 for x in filtered_data]
    
    # More distractions
    unused_data = [x - 5 for x in raw_values if x < 10]
    dummy_calc = (misleading_value * 2) if temp_sum > 20 else (misleading_value // 2)
    
    return processed

# Main execution
input_data = [4, 7, 12, 15, 8, 11, 6, 9]
processed_data = data_processor(input_data)

# Distracting calculations
base_offset = 17
adjustment_value = (base_offset ^ 5) & 15  # XOR and bitwise AND

# Misleading path that's never used
if len(processed_data) > 10:
    alternative_result = sum(processed_data) - adjustment_value
else:
    alternative_result = max(processed_data) if processed_data else 0

# The critical execution point
final_result = processed_data[-1] + adjustment_value

# Print the target result
print(f"Target result: {final_result}")