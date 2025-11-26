def process_data(values, limit):
    # Filter values above threshold and calculate weighted sum
    filtered = list(filter(lambda x: x > limit, values))
    
    # Distractor: Calculate average but don't use it
    avg = sum(values) / len(values) if values else 0
    
    # Apply transformation and compute final result
    transformed = list(map(lambda x: x * 2 - 5, filtered))
    result = sum(transformed)
    
    # Red herring: Additional unused calculation
    unused_product = len(filtered) * limit
    
    return result

data_points = [12, 8, 15, 6, 20, 9, 11]
threshold = 10

# Main execution with intermediate steps
intermediate = process_data(data_points, threshold)
final_result = intermediate + len(data_points)

# Print the target variable
print(f"Result: {final_result}")