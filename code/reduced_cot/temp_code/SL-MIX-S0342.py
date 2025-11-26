def analyze_quality_samples(samples):
    irrelevant_calc = samples[0] * 3.14 + len(samples) ** 2
    temp_buffer = [x * 2 for x in samples]
    processed_data = [sample // 2 if sample % 2 == 0 else sample * 3 + 1 for sample in samples]
    
    # Misleading intermediate processing
    dummy_metrics = [x + 5 for x in processed_data]
    shadow_calc = sum(dummy_metrics) // len(dummy_metrics)
    
    # Actual quality processing
    quality_metrics = [sample * 2 - 3 for sample in processed_data]
    processed_indices = [i for i in range(len(quality_metrics)) if quality_metrics[i] > 10]
    
    # Dead code path - never executed
    if shadow_calc > 100:
        unused_result = shadow_calc * 2
    else:
        unused_result = shadow_calc // 2
    
    # Slicing operations for key processing
    relevant_slice = quality_metrics[:len(quality_metrics)//2]
    processed_indices = [i for i, val in enumerate(quality_metrics) if val in relevant_slice]
    
    # Critical execution point
    final_quality_score = quality_metrics[processed_indices[-1]]
    
    print(f"Result: {final_quality_score}")
    return final_quality_score

# Main execution with distractor variables
sample_data = [8, 15, 22, 7, 19, 11]
redundant_check = [x % 4 for x in sample_data]
misleading_total = sum(sample_data) * 2

result = analyze_quality_samples(sample_data)
dummy_output = misleading_total // len(sample_data)