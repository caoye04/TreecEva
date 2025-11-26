def analyze_data_sequence(pattern):
    # Process data pattern using slicing operations
    primary_data = pattern[2:8]
    secondary_data = pattern[1:6]
    
    # Calculate base metrics (some are distractors)
    data_sum = sum(primary_data)
    avg_data = sum(secondary_data) / len(secondary_data)
    max_value = max(primary_data)
    
    # Core logic with early termination
    threshold = 25
    filtered_values = []
    for value in primary_data:
        if value > threshold:
            filtered_values.append(value)
            if len(filtered_values) >= 2:  # Early break condition
                break
    
    # Distractor calculation (not used in final result)
    unused_metric = (data_sum + avg_data) * 0.75
    
    # Key computation - string operations on numerical data
    if filtered_values:
        result_string = ''.join(str(x) for x in filtered_values)
        final_output = int(result_string) % 100
    else:
        final_output = data_sum % 50
    
    return final_output

# Main execution
data_pattern = [5, 12, 8, 31, 42, 17, 23, 9, 14]
result = analyze_data_sequence(data_pattern)
print(f"Result: {result}")