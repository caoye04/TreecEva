def process_data_stream(stream, mask):
    # Distractor: unused lambda function
    filter_condition = lambda x: x > 0
    
    # Main processing logic
    processed_values = []
    temp_sum = 0
    count_valid = 0
    
    # Misleading intermediate variable
    accumulator = 100
    
    for idx, (data, is_valid) in enumerate(zip(stream, mask)):
        if is_valid:
            # Relevant computation
            temp_sum += data * (idx + 1)
            count_valid += 1
            processed_values.append(data)
            
            # Distractor: dead code path
            if idx > len(stream) + 5:
                accumulator -= data
        else:
            # Misleading computation
            temp_sum -= idx * 2
            
            # Distractor: unused operation
            processed_values.append(-1)
    
    # More distractions
    average_check = sum(processed_values) / len(processed_values) if processed_values else 0
    
    # Key computation
    weighted_average = temp_sum / count_valid if count_valid else 0
    
    # Final transformation with modular arithmetic
    result = int((weighted_average * 7) % 256)
    
    # Distractor: unused variable
    verification_flag = result > 128
    
    return result

# Main execution
base_sequence = [15, 22, 8, 34, 12, 19, 27]
validation_flags = [True, False, True, True, False, True, True]

# Distractor: misleading intermediate computation
preliminary_result = sum(base_sequence) // len(base_sequence)

# Irrelevant dictionary operations
coordinate_mapping = dict(enumerate(base_sequence))
max_coordinate = max(coordinate_mapping.values()) if coordinate_mapping else 0

# Key function call
result_aggregator = process_data_stream(base_sequence, validation_flags)

# Final computation with bitwise operations
final_output = (result_aggregator ^ 0b10101010) & 0xFF

# Distractor: dead code
if final_output > 200:
    print("High value detected")
elif final_output < 50:
    print("Low value range")

print(f"Target result: {final_output}")