from collections import defaultdict
import itertools

def calculate_signal_strength(sequence):
    cache = defaultdict(int)
    
    def recursive_decode(seq, index):
        if index >= len(seq):
            return 1
        
        if index in cache:
            return cache[index]
        
        current_val = seq[index]
        combinations_count = sum(1 for _ in itertools.combinations(range(current_val), min(2, current_val)))
        
        # Recursive exploration with backtracking
        sub_result = recursive_decode(seq, index + 1) * (current_val ^ (current_val >> 1))
        
        # Apply ternary operator for conditional adjustment
        adjusted_value = sub_result + 10 if combinations_count > current_val else sub_result - 5
        
        cache[index] = adjusted_value
        return adjusted_value
    
    return recursive_decode(sequence, 0)

input_sequence = [3, 7, 1, 4]
intermediate_result = calculate_signal_strength(input_sequence)
final_metric = intermediate_result & 0xFF  # Mask to 8-bit value
print(f"Result: {final_metric}")