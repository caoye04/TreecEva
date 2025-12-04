def compute_data_checksum(data_points):
    # Initial processing - irrelevant for final result
    temp_buffer = [x * 2 for x in data_points if x % 3 == 0]
    offset_calc = sum(temp_buffer) // len(temp_buffer) if temp_buffer else 0
    
    # Main computation path
    valid_entries = [x for x in data_points if x > 0]
    checksum_candidates = []
    
    for entry in valid_entries:
        # Distractor: intermediate calculations that don't affect final result
        parity_check = entry & 0x01
        if parity_check:
            checksum_candidates.append(entry * 3 - 7)
        else:
            checksum_candidates.append(entry + 15)
    
    # Final computation
    if checksum_candidates:
        base_sum = sum(checksum_candidates[:len(checksum_candidates)//2])
        adjustment = sum(checksum_candidates[len(checksum_candidates)//2:]) % 100
        final_sum = base_sum + adjustment
    else:
        final_sum = -999  # Dead code path
    
    # More irrelevant computations
    redundant_calc = offset_calc * 2 + 5
    dummy_var = redundant_calc // 3
    
    return final_sum

# Main execution
raw_data = [12, 7, 4, 9, 15, 2, 8, 11, 6]

# Distractor: multiple variable assignments
preliminary_sum = sum(raw_data)
filtered_data = [x for x in raw_data if x % 2 == 1]
processed_data = [x + 2 for x in raw_data[:5]]

# Key statement
result = compute_data_checksum(processed_data)

print(f"Target result: {result}")