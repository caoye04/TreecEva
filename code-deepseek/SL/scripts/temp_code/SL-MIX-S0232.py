def analyze_data_quality(dataset_entries):
    # Distractor variables - irrelevant to final computation
    data_validation_flag = True
    preprocessing_overhead = 12.5
    cache_hit_ratio = 0.75
    compression_efficiency = 0.92
    
    # Actual data processing
    raw_scores = [entry * 2 if entry % 3 == 0 else entry // 2 for entry in dataset_entries]
    
    # Misleading intermediate calculations
    average_throughput = sum(raw_scores) / len(raw_scores) if raw_scores else 0
    data_consistency_check = len(set(raw_scores)) == len(raw_scores)
    
    # Critical path calculations
    max_score = max(raw_scores) if raw_scores else 0
    min_score = min(raw_scores) if raw_scores else 0
    scaling_factor = 1.5 if max_score > min_score else 0.5
    
    # Dead code path - never executed due to condition
    if data_validation_flag and compression_efficiency > 0.95:
        optimization_gain = cache_hit_ratio * preprocessing_overhead
        # This branch is never taken
        
    # Final computation
    final_metric = (max_score - min_score) * scaling_factor
    
    # More distractors after final computation
    normalized_range = (max_score - min_score) / (max_score if max_score != 0 else 1)
    data_density = len(raw_scores) / (max_score - min_score) if max_score != min_score else 0
    
    print(f"Result: {final_metric}")
    return final_metric

# Main execution
dataset = [15, 8, 22, 17, 9, 31, 12, 25]
result = analyze_data_quality(dataset)
