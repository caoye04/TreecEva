def primary_calculation(value):
    # Distractor: unused lambda for filtering
    filter_func = lambda x: x % 3 == 0
    
    # Main calculation logic with intervention
    bitwise_transform = lambda x: (x ^ 0b1010) & 0b1111
    intermediate = bitwise_transform(value)
    
    # Semi-relevant processing that doesn't affect final result
    unused_intermediate = intermediate + 5
    temp_list = [i for i in range(intermediate)]
    
    # Key recursive component
    def recursive_adjust(n):
        if n <= 1:
            return n
        return recursive_adjust(n - 1) + 2
    
    core_value = recursive_adjust(intermediate)
    
    # Final transformation with bitwise operation
    final_output = (core_value | 0b1100) ^ 0b0110
    
    return final_output

composite_input = 12
preliminary_check = composite_input >> 1  # Unused distractor
final_result = primary_calculation(composite_input)
print(f"Result: {final_result}")