def analyze_metrics(data_map):
    temp_results = {}
    scaling_factor = 1.75
    offset_correction = -0.2
    
    for key, values in data_map.items():
        raw_sum = sum(values)
        normalized = raw_sum * scaling_factor + offset_correction
        temp_results[key] = max(normalized, 0)
    
    return temp_results


def filter_outliers(score_dict, threshold=150):
    cleaned = {}
    outlier_log = []  # Dead variable - not used later
    count_filtered = 0
    
    for k, v in score_dict.items():
        if v < threshold:
            cleaned[k] = v
        else:
            count_filtered += 1  # Computation has no effect on result
    
    return cleaned


def calculate_cycle_weight(length, base=0.98):
    weight = 1.0
    for i in range(length):
        weight *= base  # Simulates decay, but only final value matters
    return weight


def calculate_performance(dataset):
    # Initial processing
    intermediate_scores = {}
    adjustment_tracker = []  # Unused tracking list
    
    processed_data = analyze_metrics(dataset)
    clean_scores = filter_outliers(processed_scores)
    
    total_contribution = 0.0
    weight_sum = 0.0
    
    # Use enumerate and zip together on relevant filtered data
    indices = list(range(len(clean_scores)))
    keys = list(clean_scores.keys())
    scores = list(clean_scores.values())
    
    for idx, (key, score) in enumerate(zip(keys, scores)):
        cycle_length = len(key) % 7 + 3  # Artificial length variation
        cycle_weight = calculate_cycle_weight(cycle_length)
        
        # Actual contribution calculation
        contribution = score * cycle_weight
        total_contribution += contribution
        weight_sum += cycle_weight
        
        intermediate_scores[key] = contribution  # Stored but not used
    
    # Final weighted score
    final_score = total_contribution / weight_sum if weight_sum != 0 else 0
    
    # Irrelevant post-processing (distraction)
    if final_score > 100:
        final_score *= 0.95
    elif final_score > 50:
        final_score *= 1.05  # This branch will actually execute
    else:
        final_score += 10

    return final_score

# Main execution block
benchmark_data = {
    'alpha': [4, 7, 2],
    'beta': [9, 1, 8, 2],
    'gamma': [5, 5],
    'delta': [3, 6, 1, 1, 1],
    'epsilon': [10, 2]
}

# Extraneous variable computations (distractors)
baseline_avg = sum(sum(v) for v in benchmark_data.values()) / len(benchmark_data)
dummy_matrix = [[i*j for j in range(3)] for i in range(3)]  # Dead code structure

final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")