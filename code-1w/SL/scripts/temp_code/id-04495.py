def process_signals(data):
    magnitude_threshold = 5.0
    adjusted_values = []
    
    for val in data:
        if val < 0:
            abs_val = -val
        else:
            abs_val = val
        
        if abs_val > magnitude_threshold:
            adjusted_values.append(abs_val * 0.9)
        else:
            adjusted_values.append(abs_val + 0.1)
    
    squared_chain = [x**2 for x in adjusted_values if x > 3]
    temp_sum = sum(squared_chain)
    
    # Irrelevant transformation chain (distractor)
    case_shifted = ''.join([chr(ord('a') + (i % 26)) for i in range(len(adjusted_values))])
    metadata_flag = len(case_shifted) > 5
    
    reduction_factor = 0.85 if metadata_flag else 0.7
    reduced_total = temp_sum * reduction_factor
    
    # Secondary processing path with conditional expression
    correction_offset = 10 if any(x > 7 for x in adjusted_values) else 5
    
    # Final computation
    final_score = reduced_total - correction_offset
    
    # Normalize using lambda-based scaling (partially irrelevant)
    scaler = lambda x, r: x * (1 + r / 100)
    normalized_result = scaler(final_score, 2.5)  # Minor adjustment
    
    # Key assignment
    final_output = int(normalized_result)  # Truncate to integer
    return final_output

# Simulate sensor input data
raw_sensor_data = [1.2, -6.5, 3.1, 7.8, -2.0, 4.4]

# Preprocessing with filtering (relevant)
def apply_filter(seq):
    return [x for x in seq if x != -2.0]  # Remove invalid reading

filtered_data = apply_filter(raw_sensor_data)

# Misleading auxiliary calculation (dead-end)
baseline_energy = sum([abs(x)**1.5 for x in raw_sensor_data])
dummy_state = {'level': 'nominal', 'count': baseline_energy > 20}

# Main execution point
final_output = process_signals(filtered_data)
print(f"Result: {final_output}")