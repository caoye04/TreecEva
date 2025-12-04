def process_data(data):
    # Extract unique elements using set operations
    unique_values = set(data)
    
    # Apply slicing to get subset
    data_slice = data[2:6]
    
    # Simple recursion to calculate sum of unique values
    def recursive_sum(values):
        if not values:
            return 0
        return values.pop() + recursive_sum(values)
    
    # Calculate result
    base_sum = sum(data_slice)
    unique_sum = recursive_sum(unique_values.copy())
    
    # Final computation
    result = (base_sum * 2) - (unique_sum // 3)
    return result

# Main execution
initial_data = [8, 3, 5, 8, 2, 7, 5, 1]
final_result = process_data(initial_data)
print(f"Result: {final_result}")