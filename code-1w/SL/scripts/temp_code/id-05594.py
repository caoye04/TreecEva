def analyze_efficiency(records):
    efficiency_list = [r['ops'] / r['time'] for r in records if r['time'] > 0]
    avg_efficiency = sum(efficiency_list) / len(efficiency_list)
    threshold = 100
    boosted = [e * 1.1 for e in efficiency_list if e > threshold]
    return sum(boosted) if boosted else avg_efficiency * 0.5


def transform_keys(data_map):
    # Irrelevant transformation on keys
    new_map = {}
    for k, v in data_map.items():
        if isinstance(v, str):
            new_map[k.upper() + '_X'] = v.lower()
        else:
            new_map[k + '_Y'] = v * 2
    return new_map


def filter_outliers(seq, limit=3):
    # Dead code path - never used with this limit
    mean_val = sum(seq) / len(seq)
    std_dev = (sum((x - mean_val) ** 2 for x in seq) / len(seq)) ** 0.5
    return [x for x in seq if abs(x - mean_val) <= limit * std_dev]


def compute_weighted_sum(values, weights=None):
    if weights is None:
        weights = [1] * len(values)
    total = 0.0
    for i in range(len(values)):
        total += values[i] * weights[i % len(weights)]
    return total


def evaluate_performance(metrics):
    # Core logic begins
    base_scores = []
    adjustment_factor = 0.0
    
    for entry in metrics:
        raw_score = entry['score']
        penalty = 0
        
        if entry['errors'] > 5:
            penalty += 15
        elif entry['errors'] == 0:
            penalty -= 5  # bonus
            
        adjusted = raw_score - penalty
        
        if entry['type'] == 'critical':
            adjusted *= 1.2
        
        base_scores.append(adjusted)
    
    sorted_scores = sorted(base_scores, reverse=True)
    top_three_avg = sum(sorted_scores[:3]) / 3
    
    # Use string method to determine multiplier
    mode_indicator = 'performance_mode_active'
    activation_flag = mode_indicator.replace('_', '').isalpha()  # Always True
    multiplier = 1.5 if activation_flag else 1.0
    
    # Dictionary operation to simulate config lookup
    config = {'scaling': 'dynamic', 'threshold': 75, 'multiplier': multiplier}
    scaling_mode = config.get('scaling')
    
    if scaling_mode == 'dynamic':
        dynamic_boost = len([s for s in base_scores if s > config['threshold']]) * 2.5
    else:
        dynamic_boost = 0
    
    intermediate_result = top_three_avg + dynamic_boost
    
    # Additional distraction: unused sorting and min/max
    all_time_high = max(base_scores)
    all_time_low = min(base_scores)
    score_range = all_time_high - all_time_low
    stability_score = compute_weighted_sum(base_scores) / len(base_scores)  # Not used
    
    # Final computation
    final_score = int(intermediate_result * config['multiplier'])
    
    # Critical print statement for result
    return final_score

# Main execution block
if __name__ == '__main__':
    metric_data = [
        {'score': 88, 'errors': 2, 'type': 'routine'},
        {'score': 94, 'errors': 0, 'type': 'critical'},
        {'score': 76, 'errors': 8, 'type': 'routine'},
        {'score': 90, 'errors': 1, 'type': 'critical'},
        {'score': 82, 'errors': 3, 'type': 'routine'}
    ]

    # Irrelevant data structures
    system_log = {
        'init': 'complete',
        'stage_1': [1, 1, 2, 3, 5, 8],
        'stage_2': {'status': 'nominal', 'codes': [0, 0, 0]},
        'final': None
    }

    temp_records = [
        {'ops': 1200, 'time': 10},
        {'ops': 800, 'time': 9},
        {'ops': 1500, 'time': 0}  # Invalid time, filtered out
    ]

    # Unused function calls (distractors)
    _ = analyze_efficiency(temp_records)
    _ = transform_keys({'A': 10, 'B': 'Text'})
    _ = filter_outliers([10, 12, 9, 11, 1000], limit=1)  # Outlier exists but not used

    # Key execution point
    final_score = evaluate_performance(metric_data)
    
    # Output result
    print(f"Result: {final_score}")