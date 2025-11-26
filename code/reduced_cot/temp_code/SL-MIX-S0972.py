from collections import Counter

def compute_final_validation(data_stream):
    # Distractor: Process temperature readings that won't be used
    temp_readings = [25.6, 18.3, 22.1, 19.8, 24.5]
    temp_sum = sum(temp_readings)
    temp_avg = temp_sum / len(temp_readings)
    temp_adjusted = [x * 1.1 for x in temp_readings]
    
    # Misleading: Character frequency analysis that goes unused
    sample_text = "evaluation benchmark for language models"
    char_counts = Counter(sample_text.replace(" ", ""))
    common_chars = char_counts.most_common(3)
    unused_metric = sum(count for char, count in common_chars)
    
    # Actual relevant processing
    numeric_values = [item for item in data_stream if isinstance(item, int)]
    filtered_values = [x for x in numeric_values if x % 2 == 0]
    
    # Distractor: Bitwise operations that don't affect final result
    bit_masks = [0xFF, 0x0F, 0x33]
    masked_values = []
    for val in filtered_values:
        masked = val
        for mask in bit_masks:
            masked &= mask
        masked_values.append(masked)
    
    # Core calculation
    if len(filtered_values) > 0:
        sorted_values = sorted(filtered_values)
        middle_index = len(sorted_values) // 2
        median_value = sorted_values[middle_index]
        checksum = median_value * len(filtered_values)
        
        # Final adjustment with misleading operations
        adjustment = (checksum % 17) - 5
        final_result = checksum + adjustment
        
        # Dead code path that looks relevant
        if final_result > 1000:
            backup_calc = sum(filtered_values) // len(filtered_values)
            final_result = backup_calc  # This path is never taken
    else:
        final_result = -1
    
    return final_result

# Main execution with intervention
data_stream = [42, 18, 73, 56, 29, 84, 11, 67, 92, 35]

# Misleading preprocessing
processed_data = [x + 2 for x in data_stream]
reversed_data = list(reversed(processed_data))

# Dead variable that looks important
quality_score = len([x for x in data_stream if x > 50])

# The key execution
checksum_result = compute_final_validation(data_stream)

# Final output
print(f"Result: {checksum_result}")