from itertools import combinations

def analyze_trends(data):
    trends = []
    for i in range(2, len(data) + 1):
        for combo in combinations(data, i):
            if sum(combo) / len(combo) > 50:
                trends.append(sum(combo))
    return trends

# Simulate sensor readings over time
readings = [45, 60, 52, 48, 70, 58]

# Extraneous processing: trend analysis not used in final result
trend_analysis = analyze_trends(readings)

# Core performance metrics (relevant)
metrics = {
    'accuracy': 88,
    'latency': 42,
    'throughput': 67,
    'stability': 76
}

# Weight configuration for scoring
weights = {
    'accuracy': 0.4,
    'latency': 0.1,
    'throughput': 0.3,
    'stability': 0.2
}

# Misleading normalization (unused)
normalized_metrics = {k: v / 100 for k, v in metrics.items()}

# Auxiliary function to compute weighted score
def evaluate_performance(m, w):
    total_weight = 0.0
    weighted_sum = 0.0
    for key in m:
        if key in w:
            weighted_sum += m[key] * w[key]
            total_weight += w[key]
    
    # Additional logic to simulate conditional adjustment
    adjustment_factor = 1.0
    if m['accuracy'] > 85:
        adjustment_factor *= 1.05
    if m['latency'] < 50:
        adjustment_factor *= 1.02
    
    adjusted_score = weighted_sum * adjustment_factor
    
    # Dummy tracking variables (distractors)
    debug_log = f'Score computed: {adjusted_score}'
    temp_cache = [weighted_sum, total_weight, adjustment_factor]
    
    return int(round(adjusted_score))

# Compute final score
baseline_offset = 5
noise_floor = 3
final_score = evaluate_performance(metrics, weights)

# Irrelevant string manipulation (distractor)
diagnostic_id = "PERF-" + "-".join([k[:2].upper() for k in metrics.keys()])
diagnostic_id = diagnostic_id.replace("TH", "THR").replace("ST", "STAT")

# Final output
print(f"Result: {final_score}")