def apply_composite_operation(data_list):
    # Process incoming data with filtering and transformation
    filtered_data = [x * 2 for x in data_list if x > 3]
    
    # Create intermediate mapping (partially relevant)
    temp_mapping = {x: x ** 2 for x in range(len(filtered_data))}
    
    # Compute main transformation
    intermediate_sum = sum(filtered_data)
    
    # Apply logical operations with lambda
    transform_func = lambda x: x + 10 if x % 2 == 0 else x - 5
    transformed = transform_func(intermediate_sum)
    
    # Redundant calculation (distractor)
    unused_metric = sum(temp_mapping.values()) + len(data_list)
    
    return transformed

# Initialize dataset
input_data = [2, 5, 3, 8, 1, 7]

# Sort the data (relevant operation)
sorted_data = sorted(input_data, reverse=True)

# Perform composite operation
final_transform = apply_composite_operation(sorted_data)

# Final target variable
target_value = final_transform

print(f"Target result: {target_value}")