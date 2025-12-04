def process_data_points(values):
    # Misleading helper function - not actually used in final computation
    processed = [v * 2 + 5 for v in values if v > 0]
    return sum(processed) - len(processed)

def analyze_patterns(items):
    # Another distractor function with complex but irrelevant operations
    pattern_sum = 0
    for i, item in enumerate(items):
        if i % 2 == 0:
            pattern_sum += item << 2
        else:
            pattern_sum -= item | 0b1010
    return pattern_sum

def compute_final_value(entries, threshold):
    # Main computation with multiple logical steps
    filtered_entries = [e for e in entries if e >= threshold]
    
    # Distractor variable - misleading intermediate calculation
    temp_analysis = sum([(x & 0xF) ^ 0xA for x in entries]) * 2
    
    if len(filtered_entries) == 0:
        # Dead code path - never executed with given data
        result = temp_analysis // 3
    else:
        # Actual computation path
        odd_count = sum(1 for e in filtered_entries if e % 2 != 0)
        even_count = len(filtered_entries) - odd_count
        
        # More distractor operations
        bit_operations = (odd_count << 3) | (even_count & 0x7)
        
        # Final result calculation
        if odd_count > even_count:
            result = odd_count * even_count + bit_operations
        else:
            result = (odd_count + even_count) * (bit_operations ^ 0xF)
    
    # Unused computation that looks relevant
    verification_check = result % 17 + temp_analysis // 10
    
    return result

# Main execution with data setup
data_entries = [12, 8, 15, 7, 20, 3, 18, 25, 9, 14]
threshold_value = 10

# Multiple distractor variables
distractor_sum = sum(data_entries) * 2 - 15
pattern_result = analyze_patterns(data_entries)
process_result = process_data_points(data_entries)

# The key computation
final_result = compute_final_value(data_entries, threshold_value)

# Final output
print(f"Target result: {final_result}")