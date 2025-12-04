def compute_checksum(values, adjustment):
    # Initialize tracking variables (some are distractors)
    temp_sum = 0
    running_total = 100
    checksum_candidate = -50
    irrelevant_counter = 0
    
    # Process values with enumerate
    for idx, val in enumerate(values):
        temp_sum += val * (idx + 1)
        irrelevant_counter += val % 3  # Distractor operation
        
        # Nested conditional logic
        if val > 15:
            checksum_candidate += val // 2
            running_total -= 5
        else:
            checksum_candidate -= val
            running_total += 3
    
    # More distractor operations
    misleading_value = temp_sum ^ running_total
    dead_code_path = checksum_candidate * 2  # Never used
    
    # Actual computation with bit operations
    base_result = temp_sum & 0xFF
    adjusted_result = base_result | adjustment
    
    # Final adjustment with tuple operations
    result_tuple = (adjusted_result, running_total, checksum_candidate)
    final_checksum = result_tuple[0] ^ result_tuple[1]
    
    return final_checksum

def irrelevant_helper(data):
    # This function is never called - pure distraction
    return sum(x * x for x in data) % 100

# Main execution
data_points = [8, 12, 25, 7, 18, 31, 9, 22]
modifier = 0b10101010
secondary_data = [5, 10, 15]  # Unused data

dummy_calc = sum(secondary_data) * 2  # Dead calculation
final_result = compute_checksum(data_points, modifier)

print(f"Result: {final_result}")