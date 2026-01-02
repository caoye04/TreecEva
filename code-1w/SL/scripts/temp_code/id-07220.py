def transform_values(values, threshold):
    transformed = []
    temp_result = 0
    for val in values:
        if val > threshold:
            temp_result += val * 2
        else:
            temp_result -= val // 2
    transformed.append(temp_result)

    intermediate = [v**2 for v in values]
    shifted = [intermediate[i] - intermediate[i-1] for i in range(1, len(intermediate))]
    
    base_offset = 7
    adjusted = [s + base_offset for s in shifted]
    processed_data = adjusted[:len(adjusted)//2] if len(adjusted) > 4 else adjusted
    
    filtered_sum = sum([x for x in processed_data if x % 3 == 0])
    
    extra_var_a = 'irrelevant_string'
    extra_var_b = {'note': 'this does not affect computation'}
    
    print(f"Result: {filtered_sum}")

# Input data
data_input = [3, 5, 2, 8, 6]
transform_values(data_input, 4)