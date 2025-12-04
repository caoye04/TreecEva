def analyze_sequence(data_sequence):
    # Calculate sum of all elements
    total_sum = sum(data_sequence)
    
    # Extract middle portion using slicing (python feature)
    middle_slice = data_sequence[2:5]
    middle_sum = sum(middle_slice)
    
    # XOR operations that don't affect final result
    xor_temp = total_sum ^ middle_sum
    xor_adjusted = xor_temp ^ 0xFF
    
    # Intermediate calculation that seems relevant but isn't used
    unused_metric = (total_sum + middle_sum) // len(middle_slice)
    
    # Bitwise masking operation
    masked_sum = total_sum & 0b11111111
    
    # Adjustment factor based on sequence properties
    sequence_length = len(data_sequence)
    bit_adjustment = sequence_length | 0b100
    
    # Final calculation - this is what matters
    final_result = masked_sum * bit_adjustment
    
    # Print the target variable
    print(f"Target result: {final_result}")

# Main execution
input_data = [15, 23, 42, 67, 89, 12, 34]
analyze_sequence(input_data)