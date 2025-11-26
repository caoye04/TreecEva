def compute_final_score(data_set):
    # Initial processing with irrelevant operations
    temp_buffer = [x * 2 for x in data_set]
    redundant_sum = sum(temp_buffer)
    
    # Misleading intermediate calculations
    fake_modulo = redundant_sum % 17
    fake_binary = bin(fake_modulo)
    
    # Actual core logic with set operations
    unique_values = set(data_set)
    filtered_set = {x for x in unique_values if x % 3 != 0}
    
    # Lambda function for processing
    transform_fn = lambda x: (x ** 2) % 13
    transformed_data = map(transform_fn, filtered_set)
    
    # More distractions
    dead_code_path = sum([i for i in range(10) if i % 2 == 0])
    unused_string = "placeholder_" + str(dead_code_path)
    
    # Critical calculation chain
    intermediate_sum = sum(transformed_data)
    adjustment_factor = (len(filtered_set) * 7) % 11
    
    # Final computation (the answer)
    final_score = intermediate_sum + adjustment_factor
    
    # Print irrelevant values for distraction
    print(f"Debug: fake_modulo = {fake_modulo}")
    print(f"Debug: dead_code_path = {dead_code_path}")
    
    return final_score

# Main execution with input data
input_data = [4, 8, 15, 16, 23, 42]
processed_data = [x + 1 for x in input_data if x > 10]

# Additional irrelevant operations
misdirection_sum = sum(input_data) * 3
bogus_list = [i * 2 for i in range(5)]

# The key execution point
final_score = compute_final_score(processed_data)

# Print the target result
print(f"Result: {final_score}")