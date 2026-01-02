from itertools import combinations

def analyze_efficiency(values):
    # Irrelevant helper function – distractor
    return sum(v ** 0.5 for v in values if v > 10)

def compute_baseline(data):
    # Another distraction: computes something unused later
    base = 0
    for i in range(len(data)):
        if i % 3 == 0:
            base += data[i] * 0.1
    return round(base, 3)

def evaluate_performance(metrics, weights):
    weighted_sum = 0.0
    normalization_factor = 0.0
    
    # Real logic starts here
    for key in metrics:
        if key in weights and 'efficiency' in key:
            weighted_sum += metrics[key] * weights[key]
            normalization_factor += weights[key]
    
    # Additional meaningful computation
    temp_result = []
    for a, b in combinations([metrics[k] for k in metrics if 'time' in k], 2):
        temp_result.append(abs(a - b))
    
    # Distractor: sorting but not using sorted result directly
    temp_result.sort(reverse=True)
    adjustment = temp_result[0] * 0.05 if temp_result else 0
    
    # Core answer computation
    if normalization_factor > 0:
        final_value = weighted_sum / normalization_factor
    else:
        final_value = 0
    
    # Final adjustment based on valid logic
    final_value += adjustment
    
    # Dead code path – misleading
    if normalization_factor > 100:
        final_value *= 0.9
    
    return final_value

# Main execution block
raw_data = [12, 15, 8, 22, 30, 5]
baseline_check = compute_baseline(raw_data)  # Unused later

# Actual relevant data structures
metrics = {
    'efficiency_batch': 88.0,
    'efficiency_stream': 92.0,
    'time_initial': 4.5,
    'time_recover': 6.3,
    'memory_usage': 70.2
}

weights = {
    'efficiency_batch': 0.6,
    'efficiency_stream': 0.9,
    'other_metric': 0.3  # Not used due to filtering
}

intermediate_distractor = analyze_efficiency(raw_data)
sorted_pairs = sorted(combinations([1, 3, 5], 2))  # No effect on output

final_score = evaluate_performance(metrics, weights)
print(f"Target result: {final_score}")