from itertools import combinations
from math import log

# Simulated system metrics and benchmark weights
def generate_metrics():
    base_metrics = {
        'latency': 42.5,
        'throughput': 876,
        'error_rate': 0.0034,
        'cpu_load': 0.78,
        'memory_usage': 0.61
    }
    # Distractor: irrelevant transformations
    temp_data = [base_metrics['latency'] * 2, base_metrics['throughput'] // 100]
    temp_data.append(log(temp_data[0]) if temp_data[0] > 0 else 0)
    derived = {k: v * 1.1 for k, v in base_metrics.items()}
    derived['jitter'] = 0.012  # Red herring metric
    return derived

# Decoy function – looks relevant but unused in final calculation
def analyze_stability(metrics):
    critical = ['latency', 'error_rate']
    score = 0
    for m in critical:
        if m in metrics:
            score += 100 * (0.01 / metrics[m]) if metrics[m] > 0 else 0
    return score // len(critical)

# Another decoy: complex combinatorics with no impact
def compute_interaction_pairs(data_dict):
    keys = list(data_dict.keys())
    pairs = list(combinations(keys, 2))
    xor_sum = 0
    for a, b in pairs:
        xor_sum ^= hash(a) & hash(b)  # Bitwise red herring
    return xor_sum % 1000

# Real weight adjustment logic buried in noise
def adjust_weights(raw_weights, version='final'):
    adjusted = {}
    multiplier = 1.0
    if version == 'final':
        multiplier = 0.9
    # Distractor: conditional on unused flag
    debug_mode = False
    if debug_mode:
        print("Debug: adjusting weights")
    for k, v in raw_weights.items():
        temp_val = v * multiplier
        if k in ['latency', 'error_rate']:
            temp_val *= 1.2  # Higher penalty for critical metrics
        adjusted[k] = round(temp_val, 4)
    return adjusted

# Core evaluation logic
def normalize_metric(value, metric_name):
    # Ideal ranges for each metric (lower is better for these)
    ideals = {
        'latency': 50.0,
        'error_rate': 0.01,
        'cpu_load': 1.0,
        'memory_usage': 1.0,
        'throughput': 1000
    }
    if metric_name not in ideals:
        return 0.5  # Neutral score for unknowns (e.g., jitter)
    ideal = ideals[metric_name]
    if metric_name == 'throughput':
        return min(value / ideal, 1.0)  # Higher is better
    else:
        return max(ideal / max(value, 1e-8), 0.0) if value > 0 else 0.0

# Main scoring function
def evaluate_performance(log_entry, weights):
    raw_score = 0.0
    norm_scores = {}
    used_keys = ['latency', 'throughput', 'error_rate', 'cpu_load', 'memory_usage']
    
    # Distractor: create unused normalized values
    for key in log_entry.keys():
        norm_scores[key] = normalize_metric(log_entry[key], key)
    
    # Actual scoring uses only specific keys
    for key in used_keys:
        contribution = norm_scores[key] * weights.get(key, 1.0)
        raw_score += contribution
    
    # Final scaling based on throughput tier (hidden logic)
    tp_tier = 1.0
    tp = log_entry.get('throughput', 0)
    if tp > 900:
        tp_tier = 1.15
    elif tp > 700:
        tp_tier = 1.05
    
    final = raw_score * tp_tier
    
    # Dead code path: never executed due to data
    if final < 0:
        fallback = 0
        for val in norm_scores.values():
            fallback += val * 0.2
        final = fallback  # Unused
    
    return round(final, 6)

# Setup
metrics_log = generate_metrics()

# Distractor: unused combination analysis
pair_hash = compute_interaction_pairs(metrics_log)

# Base weights (subject to adjustment)
benchmark_weights = {
    'latency': 0.25,
    'throughput': 0.30,
    'error_rate': 0.20,
    'cpu_load': 0.15,
    'memory_usage': 0.10
}

# Adjust weights using real logic
benchmark_weights = adjust_weights(benchmark_weights, version='final')

# Critical execution point
final_score = evaluate_performance(metrics_log, benchmark_weights)

# Irrelevant post-processing
adjusted_final = final_score * 1.0
double_checked = abs(adjusted_final) if adjusted_final >= 0 else adjusted_final

# Output the target result
print(f"Result: {final_score}")