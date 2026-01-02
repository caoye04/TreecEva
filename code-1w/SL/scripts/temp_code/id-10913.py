from itertools import combinations
from functools import reduce

# Simulated system performance metrics over time
metrics = {
    'latency': [120, 85, 95, 110, 90],
    'throughput': [480, 520, 490, 510, 515],
    'error_rate': [0.003, 0.005, 0.002, 0.004, 0.001],
    'cpu_util': [78, 82, 75, 80, 77]
}

# Weight configuration for scoring (higher weight = more important)
weights = {
    'latency': 0.3,
    'throughput': 0.35,
    'error_rate': 0.25,
    'cpu_util': 0.1
}

# Auxiliary data - not all used directly
historical_baselines = {
    'latency_avg': 100,
    'throughput_avg': 500,
    'error_rate_avg': 0.003
}

# Misleading intermediate variables (some irrelevant)
temp_data = [x for x in metrics['latency'] if x > 90]  # distractor
outlier_count = sum(1 for window in combinations(metrics['latency'], 2) if abs(window[0] - window[1]) > 25)  # semi-relevant but unused

# Helper function to normalize metric values (0-1 scale, lower is better for inverse metrics)
def normalize(metric_name, values, reverse=False):
    extrema = {'latency': (80, 120), 'throughput': (480, 520), 'error_rate': (0.001, 0.005), 'cpu_util': (75, 85)}
    low, high = extrema[metric_name]
    if reverse:
        return [(high - v) / (high - low) for v in values]
    else:
        return [(v - low) / (high - low) for v in values]

# Compute rolling average (3-point) for smoothing - only applied selectively
def rolling_average(data, window=3):
    if len(data) < window:
        return [data[0]]
    return [sum(data[i:i+window]) / window for i in range(len(data) - window + 1)]

# Apply normalization and aggregation logic
def evaluate_performance(metrics, weights):
    scores = {}
    
    # Process each metric with appropriate normalization
    for name in weights.keys():
        raw_vals = metrics[name]
        
        # Special handling: latency and error_rate are "lower is better"
        reverse = name in ['latency', 'error_rate']
        
        normalized = normalize(name, raw_vals, reverse=reverse)
        
        # Apply rolling average only if metric length > 3 and it's not cpu_util (distractor logic)
        if len(raw_vals) > 3 and name != 'cpu_util':
            smoothed = rolling_average(normalized)
            avg_val = sum(smoothed) / len(smoothed)
        else:
            avg_val = sum(normalized) / len(normalized)
        
        scores[name] = avg_val * weights[name]
    
    # Aggregate final weighted score
    final = sum(scores.values())
    
    # Additional logic to compute auxiliary quality tier (not affecting final_score)
    quality_tier = 'A' if final >= 0.7 else 'B' if final >= 0.5 else 'C'
    
    # Red herring computation: combinatorics on normalized throughput bins
    normalized_throughput = normalize('throughput', metrics['throughput'], reverse=True)
    binned = [int(nt * 10) for nt in normalized_throughput]
    pair_interactions = list(combinations(binned, 2))  # computed but unused
    
    # Final adjustment based on consistency (standard deviation penalty)
    consistency_penalty = 0.0
    if 'latency' in metrics:
        lat_vals = metrics['latency']
        mean_lat = sum(lat_vals) / len(lat_vals)
        var = sum((x - mean_lat) ** 2 for x in lat_vals) / len(lat_vals)
        std = var ** 0.5
        consistency_penalty = max(0, std / 150 - 0.05)  # small possible deduction
    
    final -= consistency_penalty  # minor adjustment
    
    return final

# Irrelevant helper function (dead code path)
lambdas = {
    'square': lambda x: x ** 2,
    'invert': lambda x: 1 / x if x != 0 else 0
}

def unused_diagnostics(data_map):
    flat = reduce(lambda a, b: a + b, [v for v in data_map.values() if isinstance(v, list)], [])
    return {"count": len(flat), "unique": len(set(flat))}

# Execution point of interest
diag = unused_diagnostics(metrics)  # distractor call
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")