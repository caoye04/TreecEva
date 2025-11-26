def analyze_data_sequence(data_stream):
    # Distractor: Calculate sum that won't be used
    total_sum = sum(x * 2 for x in data_stream)
    
    # Relevant: Process data with enumerate and slicing
    processed_values = []
    for idx, value in enumerate(data_stream):
        if idx % 2 == 0 and value > 5:
            processed_values.append(value // 2)
    
    # Distractor: Create lambda that won't be used
    square_lambda = lambda x: x ** 2
    
    # Relevant: Use zip and slicing for validation
    first_half = processed_values[:len(processed_values)//2]
    second_half = processed_values[len(processed_values)//2:]
    
    validation_results = []
    for a, b in zip(first_half, second_half):
        if (a + b) % 3 == 0:
            validation_results.append(a + b)
    
    # Distractor: Calculate average that won't be used
    if validation_results:
        avg_result = sum(validation_results) / len(validation_results)
    else:
        avg_result = 0
    
    # Relevant: Final count logic
    valid_entries_counter = len(validation_results)
    
    # Distractor: Additional computation that won't affect result
    temp_adjustment = valid_entries_counter * 2 - 5
    
    final_count = valid_entries_counter
    print(f"Result: {final_count}")

# Main execution
input_data = [8, 3, 12, 7, 9, 4, 15, 6, 11, 2]
analyze_data_sequence(input_data)