def process_data(raw_inputs):
    # Filter and transform input data
    valid_numbers = [x * 2 for x in raw_inputs if x % 3 == 0]
    
    # Intermediate calculation that doesn't affect final result
    temp_sum = sum([n + 5 for n in valid_numbers])
    temp_product = temp_sum * 2
    
    # Actual relevant processing
    processed_values = [num - 1 for num in valid_numbers]
    
    # Another distraction calculation
    alternative_result = len(processed_values) * 10
    
    return processed_values

def final_processing(data_list):
    # Calculate mean with some unnecessary steps
    count = len(data_list)
    total_sum = sum(data_list)
    
    # Distractor operation that gets discarded
    squared_sum = sum([x**2 for x in data_list])
    
    # Final relevant calculation
    result = total_sum // count
    
    # Final irrelevant adjustment that gets overridden
    result = result + 3
    return result

# Main execution
input_sequence = [12, 8, 15, 6, 21, 9, 18]
cleaned_data = process_data(input_sequence)

# Intermediate variable that's not used
partial_result = sum(cleaned_data) * 2

# The key statement
processed_total = final_processing(cleaned_data)

print(f"Result: {processed_total}")