from itertools import combinations

def analyze_efficiency(values):
    # Irrelevant helper: computes pairwise products (not used in final result)
    pairs = list(combinations(values, 2))
    products = [a * b for a, b in pairs]
    return sum(products) // len(products) if products else 0

def calculate_baseline(data):
    # Semi-relevant: baseline uses part of data but is overridden later
    base = sum(data) / len(data)
    adjustment = len([x for x in data if x > base])
    return base + adjustment

def evaluate_performance(metrics, weights):
    # Core logic begins
    weighted_sum = 0.0
    temp_shift = 0
    
    # Distractor: complex string parsing with no impact
    labels = ['metric_A', 'metric_B', 'metric_C']
    key_map = {i: label.upper() for i, label in enumerate(labels)}
    unused_buffer = [s.replace('_', '-') + '_proc' for s in key_map.values()]
    
    # Real computation starts
    for i, (m, w) in enumerate(zip(metrics, weights)):
        if m < 50:
            temp_shift += 1
        elif m >= 80:
            temp_shift -= 1
        weighted_sum += m * (w + 0.1 * temp_shift)  # Adaptive weighting
    
    # Additional logic: apply bonus only if certain metrics dominate
    high_performers = len([m for m in metrics if m >= 85])
    bonus = 10 if high_performers >= 2 else 0
    
    # State tracking with dictionary (used)
    status_log = {
        'high_count': high_performers,
        'bonus_applied': bonus > 0,
        'adjusted_sum': weighted_sum
    }
    
    # Final score calculation
    raw_score = weighted_sum + bonus
    scaling_factor = 1.05 if status_log['bonus_applied'] else 1.0
    final_score = int(raw_score * scaling_factor)
    
    # Dead code: never executed
    if False:
        fallback = calculate_baseline(metrics)
        final_score = max(final_score, fallback)
    
    return final_score

# Main execution
metrics_data = [78, 82, 88, 67]
benchmark_weights = [0.2, 0.3, 0.4, 0.1]

# Unused variables - distractions
system_load = [0.7, 0.9, 1.2, 0.5]
analysis_modes = ['quick', 'deep', 'hybrid']
config_flags = {'debug': False, 'trace': True, 'strict': False}

# Trigger evaluation
interim_result = analyze_efficiency([3, 5, 7, 8])  # distractor call
baseline_ref = calculate_baseline(metrics_data)       # semi-relevant but not used

final_score = evaluate_performance(metrics_data, benchmark_weights)
print(f"Result: {final_score}")