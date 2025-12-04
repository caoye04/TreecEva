def process_data_sequence():
    import itertools
    
    data_stream = [4, 8, 15, 16, 23, 42]
    processing_buffer = []
    
    # Main processing chain with some irrelevant computations
    for i, value in enumerate(data_stream):
        temp_mod = (value * 3 + 7) % 11
        processing_buffer.append(temp_mod)
    
    # Distractor: string processing that doesn't affect final result
    dummy_text = "processing_data_sequence_xyz"
    dummy_count = dummy_text.count('e')
    
    # Key computation with conditional logic
    filtered_values = [x for x in processing_buffer if x > 5]
    
    # Irrelevant computation that gets discarded
    unused_sum = sum(data_stream) + len(data_stream)
    
    if len(filtered_values) >= 2:
        # Main logical chain
        first_val = filtered_values[0]
        last_val = filtered_values[-1]
        intermediate = (first_val ^ last_val) & 0b1111
        
        # Another distractor computation
        cycle_check = list(itertools.islice(itertools.cycle([1, 2, 3]), 5))
        
        result = intermediate * 3 - 7
    else:
        result = unused_sum % 100  # This branch won't be taken
    
    return result

def calculate_final_output():
    primary_result = process_data_sequence()
    
    # Final adjustment with bitwise operation
    adjustment = (primary_result >> 1) | 1
    
    # Another irrelevant string operation
    validation_string = "result_verification"
    string_length = len(validation_string)
    
    final_output = adjustment + 10
    
    # Print the target variable
    print(f"Target result: {final_output}")
    return final_output

result = calculate_final_output()