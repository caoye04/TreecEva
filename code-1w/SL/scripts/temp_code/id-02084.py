from itertools import combinations

def analyze_sequence(values):
    total_pairs = 0
    max_product = -float('inf')
    seen_multiples = []
    
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            pair_sum = values[i] + values[j]
            if pair_sum % 3 == 0:
                total_pairs += 1
            product = values[i] * values[j]
            if product > max_product:
                max_product = product
    
    # Distractor: unused intermediate calculation
    temp_analysis = [x * 2 for x in values if x < 5]
    temp_analysis = [y - 1 for y in temp_analysis]

    return total_pairs

def compute_baseline(reference_list):
    baseline = 0
    adjustment = 0
    for val in reference_list:
        if val > 7:
            adjustment += 1
        baseline += val // 2
    
    # Dead code path (never executed due to logic)
    if False:
        baseline -= adjustment * 2
    
    return baseline

def evaluate_performance(metrics, threshold):
    count_valid = 0
    sum_adjusted = 0.0
    
    for entry in metrics:
        raw_value = entry['value']
        status_flag = entry['flag']
        
        if status_flag == 'inactive':
            continue
            
        normalized = raw_value / (entry['factor'] or 1)
        
        if normalized > threshold:
            count_valid += 1
            sum_adjusted += normalized

    # Semi-relevant transformation
    avg_normalized = sum_adjusted / count_valid if count_valid > 0 else 0
    
    # Key distraction: complex but unused combinatorial analysis
    indices = list(range(len(metrics)))
    combo_count = 0
    for combo in combinations(indices, 3):
        a, b, c = combo
        if metrics[a]['value'] < metrics[b]['value'] < metrics[c]['value']:
            combo_count += 1
    
    # Final result depends only on average, not on combo_count or anything else
    final_score = int(avg_normalized * 10)
    return final_score

# Main execution
if __name__ == '__main__':
    data_stream = [4, 6, 2, 8, 1, 9]
    
    # Irrelevant pre-processing (not used later)
    processed = analyze_sequence(data_stream)
    base_config = [10, 3, 8, 5]
    config_baseline = compute_baseline(base_config)
    
    metric_data = [
        {'value': 25, 'factor': 5, 'flag': 'active'},
        {'value': 18, 'factor': 3, 'flag': 'active'},
        {'value': 40, 'factor': 8, 'flag': 'inactive'},  # skipped
        {'value': 36, 'factor': 6, 'flag': 'active'},
        {'value': 14, 'factor': 7, 'flag': 'active'}
    ]
    
    base_threshold = 4.0
    final_score = evaluate_performance(metric_data, base_threshold)
    
    # Output result as required
    print(f"Result: {final_score}")