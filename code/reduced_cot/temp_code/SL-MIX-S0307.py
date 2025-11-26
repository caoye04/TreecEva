from collections import Counter

def analyze_data_pattern(data_sequence):
    # Distractor computations - irrelevant to final result
    temp_sum = sum(x * 2 for x in data_sequence if x > 5)
    pattern_score = len([x for x in data_sequence if x % 3 == 0])
    
    # Main logic path
    counter = Counter(data_sequence)
    most_common = counter.most_common(2)
    
    # More distractions
    unused_value = (temp_sum * pattern_score) // 7
    secondary_pattern = [x for x in data_sequence if x < 10]
    
    if len(most_common) >= 2:
        primary, secondary = most_common[0], most_common[1]
        # Core computation - XOR and bit manipulation
        xor_result = primary[0] ^ secondary[0]
        shift_value = xor_result << 2
        
        # Additional irrelevant operations
        dead_branch = shift_value * 3 if xor_result > 15 else shift_value // 2
        misleading_temp = dead_branch + pattern_score
        
        # The actual checksum calculation
        checksum = (shift_value & 0b1111) | ((xor_result >> 2) & 0b1111)
    else:
        checksum = 255  # Dead code path
    
    # Result mapping with some irrelevant entries
    result_mapper = {
        5: 42,
        9: 78,
        12: 156,
        7: 91,
        15: 203,
        3: 67
    }
    
    # Final assignment with default case
    final_result = result_mapper.get(checksum, -1)
    
    # Print verification
    print(f"Result: {final_result}")
    return final_result

# Test execution
data = [8, 12, 8, 15, 12, 8, 6, 12, 9, 8]
analyze_data_pattern(data)