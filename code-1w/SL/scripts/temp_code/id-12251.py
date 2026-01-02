def analyze_data_sequence(raw_values):
    processed = set()
    for val in raw_values:
        if val % 2 == 0:
            processed.add(val)
    
    temp_buffer = [x * 2 for x in processed if x > 5]
    validation_check = len(temp_buffer) > 3
    
    relevant_numbers = [x for x in temp_buffer if x % 3 != 0]
    filtered_sum = sum(relevant_numbers)
    
    # Extraneous computation (minor distraction, meets intervention level 5)
    average_offset = sum(processed) / len(processed) if processed else 0
    outlier_count = len([x for x in raw_values if x < 0])
    
    return filtered_sum

# Input data
data_stream = [1, 4, 6, 8, 10, 12, 7, 3]
result = analyze_data_sequence(data_stream)
print(f"Result: {result}")