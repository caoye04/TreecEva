from collections import Counter

def compute_final_result(sequence):
    # Misleading intermediate calculations (irrelevant)
    temp_sum = sum(sequence) * 2 - len(sequence)  # Dead code path
    misleading_multiplier = (temp_sum % 7) + 3
    
    # Actual relevant processing
    if len(sequence) > 5:
        filtered = [x for x in sequence if x % 2 == 0]
        if filtered:
            sliced = filtered[1:-1]  # Slicing operation
            freq_count = Counter(sliced)
            
            # Distractor calculations
            distractor_result = (misleading_multiplier * 3) // 2
            irrelevant_list = [x * 2 for x in sequence[:3]]
            
            # Key computation
            if freq_count:
                most_common = freq_count.most_common(1)[0]
                result = most_common[0] * len(sliced) + most_common[1]
                
                # More irrelevant operations
                dummy_var = result + misleading_multiplier - distractor_result
                unused_calc = dummy_var * 2
                
                return result
    
    # Alternative path (never taken with given input)
    backup_calc = sum(sequence) * misleading_multiplier
    return backup_calc

# Main execution with mixed data
data_sequence = [8, 3, 8, 5, 8, 7, 9, 8, 2, 6]

# Multiple irrelevant variable assignments
initial_offset = data_sequence[0] * 2
unused_tracker = initial_offset + len(data_sequence)
dummy_array = [x + 1 for x in data_sequence]

# Key function call
final_output = compute_final_result(data_sequence)

# Print final result
print(f"Result: {final_output}")