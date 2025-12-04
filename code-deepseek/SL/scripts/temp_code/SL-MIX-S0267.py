def compute_final_value(data, transform):
    # Initial processing with irrelevant computations
    base_value = sum(data[:3]) * 2
    temp_buffer = [x ^ 0b1010 for x in data[1:4]]  # Misleading XOR operation
    
    # Lambda function with slicing for actual transformation
    transformation_fn = lambda arr: (arr[0] & 0b1111) + (arr[-1] >> 1)
    
    # Multiple irrelevant calculations
    dummy_metric = base_value // 3
    fake_result = (dummy_metric * 7) % 11
    
    # Dead code path that looks relevant
    if fake_result > 5:
        unused_value = fake_result * 2 - 1
    else:
        unused_value = fake_result + 10
    
    # The actual critical computation chain
    processed_data = [x * 2 if x % 2 == 0 else x // 2 for x in data]
    transformed_result = transform(processed_data)
    
    # More distractions
    noise_factor = len([x for x in data if x > 10])
    distraction_value = (noise_factor * transformed_result) ^ 0b1100
    
    # Final computation with bitwise operations
    intermediate = (transformed_result & 0b0110) | (distraction_value >> 2)
    target_result = intermediate + (base_value % 7)
    
    return target_result

# Main execution
input_data = [8, 15, 22, 9, 17, 4, 11]

# Misleading transformation that's never used
redundant_transform = lambda x: sum(x[::2]) - min(x)

# The actual transformation used
actual_transform = lambda arr: (arr[1] | arr[3]) & (arr[2] ^ arr[4])

# Compute the target value
result = compute_final_value(input_data, actual_transform)
print(f"Target result: {result}")