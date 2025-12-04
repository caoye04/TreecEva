def validate_data_quality(raw_values):
    temp_sum = sum(raw_values)
    irrelevant_counter = len(raw_values) * 3 - 5  # Dead code path
    quality_score = temp_sum // len(raw_values) if raw_values else 0
    
    # Misleading intermediate calculation
    misleading_avg = (sum(raw_values) + 15) / (len(raw_values) + 1)
    
    if quality_score > 50:
        adjusted_score = quality_score - (quality_score % 7)
    else:
        adjusted_score = quality_score + (8 - quality_score % 8)
    
    # Distractor operations
    unused_metric = adjusted_score * 2 + 17
    validation_flag = adjusted_score % 3 == 0
    
    return adjusted_score

def process_quality_check(input_data):
    # Irrelevant string operations (dead code)
    data_strings = [str(x) for x in input_data]
    string_lengths = [len(s) for s in data_strings]
    
    primary_score = validate_data_quality(input_data)
    
    # Misleading conditional with dead branch
    if primary_score > 100:
        secondary_adjustment = primary_score // 4
    else:
        secondary_adjustment = primary_score // 3
    
    # Actual relevant computation
    data_range = max(input_data) - min(input_data) if input_data else 0
    composite_metric = (primary_score * 2 + data_range) // 2
    
    # More distractions
    unused_variance = sum((x - primary_score) ** 2 for x in input_data) if input_data else 0
    
    # Final calculation with bitwise distraction
    bitwise_distraction = composite_metric & 0xFF
    final_result = composite_metric - (bitwise_distraction % 5)
    
    return final_result

# Main execution
sample_data = [45, 67, 89, 23, 56, 78, 34]
data_validation_results = sample_data
final_metrics = process_quality_check(data_validation_results)

# Print the target result
print(f"Result: {final_metrics}")