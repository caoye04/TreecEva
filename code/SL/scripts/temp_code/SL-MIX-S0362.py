def process_scores(data):
    # Initialize processing variables
    base_offset = 127
    temp_buffer = [0] * 8
    unused_calc = base_offset * 3 - 45
    
    # Main processing logic
    processed = []
    for idx, val in enumerate(data):
        # Calculate intermediate value (distractor)
        mod_val = (val + idx) % 17
        temp_buffer[idx % 8] = mod_val
        
        # Actual processing path
        if val > 50:
            processed.append(val - 10)
        else:
            processed.append(val + 5)
    
    # Set operations for filtering
    unique_vals = set(processed)
    large_nums = {x for x in unique_vals if x > 40}
    
    # Slicing operations
    middle_slice = processed[2:6]
    slice_sum = sum(middle_slice)
    
    # Misleading calculation
    fake_total = sum(temp_buffer) + unused_calc
    
    # Character counting distractor (unused)
    test_string = "evaluation_metrics"
    char_count = len([c for c in test_string if c in 'aeiou'])
    
    # Final calculation
    final_score = len(large_nums) * slice_sum - base_offset
    
    return final_score

# Main execution
scores = [45, 78, 32, 91, 67, 23, 84, 56, 39, 72]
unrelated_data = [10, 20, 30, 40]
unused_result = sum(unrelated_data) * 2

# Key execution point
result = process_scores(scores)
final_score = result + 3

print(f"Target result: {final_score}")