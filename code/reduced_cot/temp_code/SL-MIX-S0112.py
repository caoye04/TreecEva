def compute_final_result(data_stream, transformation_mask):
    # Distractor variables and operations
    temp_buffer = [x * 2 for x in range(10)]
    validation_flag = sum(temp_buffer) > 100
    metadata_tracker = {'processed': False, 'verified': True}
    
    # Relevant processing with interference
    filtered_data = [item for item in data_stream if item % transformation_mask == 0]
    
    # Misleading intermediate computation
    redundant_sum = sum(data_stream) * 2
    dead_code_check = redundant_sum > 1000  # This result is never used
    
    # Core logic with nested operations
    if len(filtered_data) > 0:
        processed_values = []
        for value in filtered_data:
            if value > 5:
                # Bitwise operation interference
                bit_adjust = value & 0b1111
                transformed = (value // transformation_mask) + bit_adjust
                processed_values.append(transformed)
            else:
                processed_values.append(value * transformation_mask)
        
        # Final computation with list comprehension
        final_result = sum([x * x for x in processed_values if x % 2 == 0])
    else:
        # Alternative path that should not be taken
        final_result = transformation_mask * len(data_stream)
    
    # More distraction
    verification_counter = len([x for x in data_stream if x < transformation_mask])
    
    return final_result

# Main execution with interference
data_stream = [8, 12, 5, 18, 7, 24, 3, 15]
transformation_mask = 3
secondary_mask = 4  # Unused variable
cache_hit_ratio = 0.85  # Red herring

# Distractor computation
auxiliary_sum = sum([x for x in data_stream if x % 2 == 1])

final_solution = compute_final_result(data_stream, transformation_mask)

# Final output
print(f"Result: {final_solution}")