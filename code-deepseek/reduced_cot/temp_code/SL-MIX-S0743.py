def process_quality_data(samples):
    temp_sum = 0
    irrelevant_counter = 0
    misleading_max = -1000
    
    # Distractor computations
    for i in range(len(samples)):
        irrelevant_counter += i * 2
        if i % 3 == 0:
            misleading_max = max(misleading_max, samples[i] * 2)
    
    # Dead code path
    if misleading_max > 100:
        unused_result = misleading_max // 5
    else:
        unused_result = misleading_max * 3
    
    # Actual relevant computation
    quality_values = [s for s in samples if s > 15]
    if not quality_values:
        return 0
    
    avg_quality = sum(quality_values) // len(quality_values)
    
    # More distractors
    bitwise_distractor = avg_quality & 0b1111
    string_check = "validation_phase_" + str(avg_quality)
    
    # Key variables for final calculation
    quality_factor = len(string_check) % 8
    adjustment_value = (bitwise_distractor | 0b1010) ^ 0b1100
    scale_divisor = max(1, avg_quality % 7)
    bitwise_check = avg_quality ^ 0b0101
    
    # Final target computation
    final_validation_score = quality_factor * (bitwise_check ^ adjustment_value) // scale_divisor
    
    # Print result for verification
    print(f"Result: {final_validation_score}")
    return final_validation_score

# Main execution with sample data
sample_data = [12, 25, 8, 31, 19, 42, 7, 28, 15, 33]
result = process_quality_data(sample_data)