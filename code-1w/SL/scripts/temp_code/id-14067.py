def analyze_data(sequence):
    offset = 7
    shifted_values = [num + offset for num in sequence]
    
    doubled_values = [x * 2 for x in shifted_values]
    processed_values = [x - 5 for x in doubled_values]
    
    temp_debug = [x for x in processed_values if x < 0]  # Irrelevant diagnostic trace
    
    filtered_sum = sum([x for x in processed_values if x % 3 == 0])
    return filtered_sum

input_sequence = [1, -4, 6, 8, -2, 9]
result = analyze_data(input_sequence)
print(f"Result: {result}")