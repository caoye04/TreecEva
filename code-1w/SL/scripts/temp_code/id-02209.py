from itertools import combinations
from functools import reduce

# Simulate sensor data processing with noise filtering and relevance scoring
def analyze_readings(readings):
    filtered = [r for r in readings if r > 0.1]
    squared_devs = [(x - 0.5) ** 2 for x in filtered]
    avg_dev = sum(squared_devs) / len(squared_devs) if squared_devs else 0
    return avg_dev * 100

# Auxiliary function to compute combinatorial consistency score
def combinatorial_stability(data):
    pairs = list(combinations(data, 2))
    stable_count = 0
    total = len(pairs)
    for a, b in pairs:
        if abs(a - b) < 0.3:
            stable_count += 1
    return stable_count / total if total else 0

# Misleading helper: computes string entropy (not used in final logic)
def string_entropy(s):
    from collections import Counter
    freqs = Counter(s).values()
    probs = [f / len(s) for f in freqs]
    from math import log2
    return -sum(p * log2(p) for p in probs if p > 0)

# Core evaluation logic
def evaluate_performance(metrics, weights):
    # Apply non-linear transformation to emphasize high values
    transformed = [w * (m ** 1.5) for m, w in zip(metrics, weights)]
    
    # Irrelevant distraction: process dummy labels
    labels = ['A', 'B', 'C', 'D']
    label_lengths = [len(l) for l in labels]
    encoded = ''.join([l * length for l, length in zip(labels, label_lengths)])
    entropy = string_entropy(encoded)  # Computed but unused
    
    # Real computation path
    base_score = sum(transformed)
    adjustment_factor = 1.0
    
    # Conditional adjustment based on metric thresholds
    high_performers = [m for m in metrics if m > 0.7]
    if len(high_performers) >= 2:
        adjustment_factor *= 1.2
    elif len(high_performers) == 1:
        adjustment_factor *= 0.9
    else:
        adjustment_factor *= 0.7
    
    # Lambda-based aggregation of secondary effects
    secondary_boost = reduce(lambda acc, val: acc + (val * 0.1 if val > 0.5 else 0), metrics, 0)
    
    # Final composition
    raw_final = base_score * adjustment_factor + secondary_boost
    
    # Dead code branch: never executed due to fixed condition
    debug_mode = False
    if debug_mode:
        print(f'Debug: {raw_final}')
    
    return int(round(raw_final * 10))  # Scale and discretize

# Main execution
if __name__ == '__main__':
    # Input data from simulated system sensors
    sensor_metrics = [0.85, 0.42, 0.78, 0.63, 0.21]
    importance_weights = [0.3, 0.1, 0.25, 0.2, 0.15]
    
    # Preliminary analyses (some feed into final result)
    deviance_score = analyze_readings(sensor_metrics)
    stability_ratio = combinatorial_stability(sensor_metrics)
    
    # Key statement
    final_score = evaluate_performance(sensor_metrics, importance_weights)
    
    # Output target result
    print(f"Result: {final_score}")