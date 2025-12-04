def calculate_rotational_offset(data_stream, shift_value):
    processed_values = []
    for index, value in enumerate(data_stream):
        shifted_val = (value + shift_value) % 10
        processed_values.append(shifted_val)
    
    # Calculate offset between original and processed streams
    original_sum = sum(data_stream)
    processed_sum = sum(processed_values)
    offset_difference = abs(original_sum - processed_sum)
    
    # Final computation with enumerate result
    enumerate_result = [idx * val for idx, val in enumerate(processed_values)]
    final_offset = sum(enumerate_result)
    
    print(f"Target result: {final_offset}")
    return final_offset

# Data processing scenario
input_data = [3, 7, 2, 8, 5]
rotation_key = 4
calculate_rotational_offset(input_data, rotation_key)