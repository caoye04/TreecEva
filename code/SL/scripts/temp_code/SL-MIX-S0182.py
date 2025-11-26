def process_payload(data_stream):
    # Initialize tracking variables
    data_buffer = [x for x in data_stream if x % 2 == 0]
    temp_sum = sum(data_buffer) * 3
    
    # Distractor: unused calculation
    unused_max = max(data_stream) if data_stream else 0
    unused_avg = temp_sum / len(data_stream) if data_stream else 0
    
    # Core processing with conditional expressions
    filtered_data = [x for x in data_stream if x > 5]
    primary_sum = sum(filtered_data) if filtered_data else 0
    
    # Misleading intermediate calculation
    misleading_total = primary_sum * 2 + temp_sum
    
    # Dead code path (never executed)
    if len(data_stream) > 100:
        dead_result = misleading_total / 2
        return dead_result
    
    # Actual logic with nested conditional expressions
    adjustment = 10 if primary_sum > 50 else 5
    result = (primary_sum - temp_sum // 3) + adjustment
    
    # Final adjustment based on data characteristics
    final_adjustment = 7 if len(filtered_data) > len(data_buffer) else 3
    return result - final_adjustment

# Main execution
input_data = [8, 12, 3, 7, 15, 9, 14, 6]
redundant_calc = sum([x * 2 for x in input_data])
distractor_var = redundant_calc // len(input_data)

final_output = process_payload(input_data)
print(f"Target result: {final_output}")