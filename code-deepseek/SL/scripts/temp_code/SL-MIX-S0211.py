def calculate_fib(n):
    return n if n <= 1 else calculate_fib(n-1) + calculate_fib(n-2)

def process_data(data_tuple):
    primary, secondary, flags = data_tuple
    
    # Distractor computations
    temp_sum = sum([i**2 for i in range(primary)])
    irrelevant_metric = (temp_sum % 17) * 3.14159
    
    # Main logic with conditional expression
    threshold_check = lambda x: x > 50 if secondary % 2 == 0 else x <= 30
    adjusted_value = primary * 3 if threshold_check(secondary) else primary // 2
    
    # Bitwise operations and dead code path
    bit_shifted = (adjusted_value << 2) ^ 0xFF
    misleading_result = bit_shifted - irrelevant_metric  # This is never used
    
    # Early return based on flags
    if flags.get('skip_processing', False):
        return -999  # Dead code path
    
    # Combinatorics calculation
    combination_count = len([(i, j) for i in range(1, adjusted_value) 
                            for j in range(i+1, min(adjusted_value+1, 8))])
    
    # Final computation chain
    fib_result = calculate_fib(combination_count % 7)
    result = (fib_result + adjusted_value) * (1 if secondary > 25 else -1)
    
    return result

# Main execution with multiple assignments
data_config = (18, 32, {'validation': True})
backup_data = (22, 28, {'skip_processing': True})  # Misleading data
cache_value = calculate_fib(5)  # Irrelevant computation

main_data = data_config
final_value = process_data(main_data)

print(f"Target result: {final_value}")