from itertools import combinations
from functools import reduce

# Simulate sensor data aggregation and weighted performance scoring
def collect_metrics(sensors):
    raw_data = [sum(sensor) / len(sensor) for sensor in sensors]
    normalized = [(x - min(raw_data)) / (max(raw_data) - min(raw_data) + 1e-8) for x in raw_data]
    return {f'sensor_{i}': val for i, val in enumerate(normalized)}

sensors = [
    [0.4, 0.5, 0.38, 0.42],
    [0.7, 0.68, 0.71, 0.69],
    [0.2, 0.25, 0.18, 0.22],
    [0.9, 0.88, 0.91, 0.89]
]

metrics = collect_metrics(sensors)

# Irrelevant: analyze pairwise correlations (not used in final score)
correlation_pairs = list(combinations(metrics.keys(), 2))
dummy_correlations = [{"pair": pair, "score": abs(metrics[pair[0]] - metrics[pair[1]])} for pair in correlation_pairs]

# Weight assignment with red herring logic
base_weights = [1, 2, 1, 3]
adjustment_factor = 0.9
weights = [w * adjustment_factor for w in base_weights]

# Misleading entropy calculation (dead code path)
entropy_lambda = lambda p: -p * (p + 1e-9) * math.log(p + 1e-9)
try:
    import math
    entropy = sum(entropy_lambda(v) for v in metrics.values() if v > 0)
except:
    entropy = 0  # fallback not triggered

# Real evaluation logic obscured by structure
def evaluate_performance(met, wts):
    ordered_vals = [met[f'sensor_{i}'] for i in range(len(wts))]
    
    # Apply non-linear boost to high performers
    boosted = [v**2 if v > 0.5 else v for v in ordered_vals]
    
    # Weighted sum
    weighted_sum = sum(v * w for v, w in zip(boosted, wts))
    total_weight = sum(wts)
    
    # Dummy filtering operation (no effect due to all values being valid)
    filtered_vals = [x for x in boosted if x >= 0]
    if len(filtered_vals) == len(boosted):
        pass  # placeholder, no-op
    
    # Final normalized performance score
    return weighted_sum / total_weight

final_score = evaluate_performance(metrics, weights)

# Distractor: secondary unused metric
aggregate_risk = reduce(lambda acc, k: acc + (1 - metrics[k]), metrics.keys(), 0)

# Output target result
print(f"Result: {final_score}")