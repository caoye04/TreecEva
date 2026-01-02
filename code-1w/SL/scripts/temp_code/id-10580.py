def process_data(input_str, threshold):
    # Split string into tokens and convert to numbers
    raw_tokens = input_str.split(',')
    numeric_values = [float(token.strip()) for token in raw_tokens]
    
    # Apply filtering condition
    filtered_values = [val for val in numeric_values if val > threshold]
    
    # Compute final result
    temp_offset = 10  # Irrelevant variable (distractor)
    debug_mode = False  # Another irrelevant flag
    filtered_sum = sum(filtered_values)
    
    print(f"Result: {filtered_sum}")
    return filtered_sum

# Main execution
data_string = "3.5, 7.2, 1.8, 9.9, 4.6, 2.1"
limit = 4.0
result = process_data(data_string, limit)