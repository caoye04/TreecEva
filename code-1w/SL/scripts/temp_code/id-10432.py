def analyze_performance(metrics, thresholds):
    # Irrelevant tracking variables (distractors)
    total_evaluations = 0
    outlier_count = 0
    debug_log = []

    normalized = {}
    for key, value in metrics.items():
        if value < 0:
            debug_log.append(f"Negative metric: {key}")
            continue
        normalized[key] = max(0.1, min(value / 100.0, 1.0))

    # Semi-relevant preprocessing
    adjusted = [normalized[k] for k in sorted(normalized.keys()) if k in thresholds]
    
    # Use of enumerate and conditional expression
    penalties = []
    for i, val in enumerate(adjusted):
        threshold = thresholds.get(f'metric_{i+1}', 0.75)
        penalty = 0.2 if val < threshold else (0.1 if val < 0.9 else 0.0)
        penalties.append(penalty)

    # Use of zip to align data
    score_components = [val - pen for val, pen in zip(adjusted, penalties)]

    # Complex but partially irrelevant filtering
    filtered_scores = []
    cumulative_shift = 0
    for idx, comp in enumerate(score_components):
        if idx % 2 == 0:
            filtered_scores.append(comp + 0.05)
        else:
            filtered_scores.append(comp - 0.02)
        cumulative_shift += abs(comp - filtered_scores[-1])

    # Dead computation - does not affect final result
    avg_shift = cumulative_shift / len(filtered_scores) if filtered_scores else 0.0
    consistency_flag = avg_shift < 0.05

    # Core logic hidden among distractions
    raw_average = sum(filtered_scores) / len(filtered_scores) if filtered_scores else 0.0
    bonus = 0.05 if len(filtered_scores) >= 4 else 0.0
    final_normalized = raw_average + bonus

    return round(final_normalized * 100, 2)


def compute_aggregate(data_block, config):
    temp_results = []n    intermediate_sum = 0
    
    for entry in data_block:
        # Simulate multiple checks
        if 'status' in entry and entry['status'] != 'active':
            continue
        
        metrics = entry.get('metrics', {})
        thresholds = config.get('thresholds', {})
        
        # Key call with meaningful but buried computation
        score = analyze_performance(metrics, thresholds)
        temp_results.append(score)
        
        # Distractor: accumulating unused sum
        intermediate_sum += sum([v for v in metrics.values()])

    # Final aggregation
    valid_scores = [s for s in temp_results if s > 0]
    base_result = sum(valid_scores) / len(valid_scores) if valid_scores else 0
    
    # Apply experience multiplier (constant)
    exp_multiplier = config.get('experience_factor', 1.1)
    final_score = int(base_result * exp_multiplier)
    
    # Print required output
    print(f"Result: {final_score}")
    return final_score

# Input data
data_block = [
    {
        'id': 101,
        'status': 'active',
        'metrics': {'throughput': 85, 'latency': 45, 'errors': 2, 'load': 78}
    },
    {
        'id': 102,
        'status': 'inactive',  # This will be skipped
        'metrics': {'throughput': 92, 'latency': 30, 'errors': 0, 'load': 88}
    },
    {
        'id': 103,
        'status': 'active',
        'metrics': {'throughput': 76, 'latency': 60, 'errors': 5, 'load': 70}
    },
    {
        'id': 104,
        'status': 'active',
        'metrics': {'throughput': 95, 'latency': 25, 'errors': 1, 'load': 90}
    }
]

config = {
    'thresholds': {
        'metric_1': 0.80,
        'metric_2': 0.70,
        'metric_3': 0.75,
        'metric_4': 0.85
    },
    'experience_factor': 1.1
}

# Execute
final_score = compute_aggregate(data_block, config)