def process_data_chain(data_stream):
    # Helper function for bitwise processing
    def bitwise_transform(value):
        # Distractor: unused operation path
        temp = (value << 2) & 0xFF
        irrelevant_mask = 0b10101010
        misleading = (temp | irrelevant_mask) ^ 0b11110000
        
        # Actual transformation
        transformed = (value & 0x0F) | ((value >> 4) << 4)
        return transformed
    
    # Primary data processing with multiple steps
    filtered_data = [x for x in data_stream if x % 3 != 0]
    
    # Distractor: misleading intermediate calculation
    fake_sum = sum([x * 2 for x in data_stream if x > 10])
    dead_code_path = [x for x in range(5) if x % 2 == 0]
    
    # Bitwise processing chain
    processed = [bitwise_transform(x) for x in filtered_data]
    
    # Set operations for unique processing
    unique_vals = set(processed)
    complement_set = {x ^ 0xFF for x in unique_vals}
    
    # Distractor: unused complex calculation
    complex_distractor = len([x for x in processed if (x & 1) == 0])
    
    # Final computation with enumerate
    accumulator = 0
    for idx, val in enumerate(processed):
        if idx % 2 == 0:
            accumulator += val
        else:
            accumulator -= val
    
    # Zip operation for coordinate processing
    coords = list(zip(processed, [x * 2 for x in processed]))
    final_value = sum([x + y for x, y in coords if x > y])
    
    # Return the actual target value
    return accumulator + len(unique_vals)

# Main execution with mixed operations
raw_inputs = [15, 22, 8, 31, 45, 12, 7, 18]

# Distractor variables and operations
misleading_result = sum([x | 0x0F for x in raw_inputs])
unused_calculation = [x << 1 for x in raw_inputs if x < 20]
dead_counter = len([x for x in raw_inputs if x % 5 == 0])

# Target execution point
final_signal = process_data_chain(raw_inputs)

# Print the result
print(f"Result: {final_signal}")