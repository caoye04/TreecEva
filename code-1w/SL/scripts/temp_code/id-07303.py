def compute_transformed_value():
    base_values = [3, 7, 4, 9, 2]
    offset = 2
    mod_index = (len(base_values) * 2 - 5) % 6  # Modular arithmetic index calculation
    
    # Irrelevant distraction: unused variable (minimal interference)
    temp_buffer = [x ** 2 for x in base_values if x % 2 == 0]
    
    scale_factor = 1.5
    data_slice = base_values[1:4]  # Slice: [7, 4, 9]
    
    # Key computation with slicing and concatenation
    result = (data_slice[1:] + data_slice[:-1])[mod_index] * scale_factor
    
    print(f"Result: {result}")
    return result

compute_transformed_value()