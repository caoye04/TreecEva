from itertools import combinations
from collections import defaultdict

# Simulate sensor data aggregation and performance scoring
def collect_sensor_metrics():
    raw_readings = [12, 15, 10, 23, 18, 14, 20]
    baseline = 15
    deviations = [abs(x - baseline) for x in raw_readings]
    
    # Irrelevant transformation (distractor)
    squared_devs = [d**2 for d in deviations]
    avg_sq_dev = sum(squared_devs) / len(squared_devs)
    
    # Relevant metrics
    max_deviation = max(deviations)
    stable_count = sum(1 for d in deviations if d <= 3)
    trend_consistency = 0
    for i in range(1, len(raw_readings)):
        if (raw_readings[i] - raw_readings[i-1]) > 0:
            trend_consistency += 1
    
    return {
        'max_dev': max_deviation,
        'stable_points': stable_count,
        'trend_score': trend_consistency,
        'noise_level': avg_sq_dev  # unused distractor field
    }

# Weight configuration with red herring entries
def get_weight_profile():
    weights = defaultdict(float)
    weights['max_dev'] = -0.4
    weights['stable_points'] = 0.35
    weights['trend_score'] = 0.25
    weights['phantom_metric'] = 0.9  # irrelevant weight
    weights['noise_level'] = -0.1   # not used in final calculation
    return dict(weights)

# Evaluate system performance based on weighted metrics
def evaluate_performance(metrics, weights):
    score = 0.0
    
    # Core logic uses only three metrics
    score += metrics['max_dev'] * weights['max_dev']
    score += metrics['stable_points'] * weights['stable_points']
    score += metrics['trend_score'] * weights['trend_score']
    
    # Distractor block: combinatorial exploration of meaningless pairs
    indices = list(range(len(metrics)))
    phantom_pairs = list(combinations(indices, 2))
    pair_count = len(phantom_pairs)
    adjustment_factor = 1.0
    if pair_count > 10:
        adjustment_factor = 0.95
    
    # Dead code path (never executed due to fixed input size)
    debug_trace = []
    for _ in range(100):
        debug_trace.append(0)
    
    final_adjusted_score = score * adjustment_factor
    return int(round(final_adjusted_score))

# Main execution flow
if __name__ == "__main__":
    metrics = collect_sensor_metrics()
    weights = get_weight_profile()
    
    # Secondary analysis (unused)
    outlier_flags = [v > 5 for v in metrics.values()]
    flag_sum = sum(outlier_flags)
    
    final_score = evaluate_performance(metrics, weights)
    print(f"Result: {final_score}")