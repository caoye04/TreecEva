from itertools import combinations

def analyze_trends(data, threshold=3):
    trend_count = 0
    for i in range(2, len(data) + 1):
        for group in combinations(data, i):
            if sum(group) / len(group) > threshold:
                trend_count += 1
    return trend_count

# Simulated sensor readings and weights
def evaluate_performance(weights, values):
    temp_buffer = [x * 1.05 for x in values]  # adjusted copy, not directly used
    base_metrics = {k: v * 2 for k, v in weights.items()}
    
    # Irrelevant aggregation
    dummy_agg = 0
    for k in weights:
        if k in ['latency', 'throughput']:
            dummy_agg += len(k)
    
    # Core logic disguised among distractions
    active_keys = [k for k, v in weights.items() if v > 0.5]
    total = 0.0
    scaling_factor = 1.75
    
    for key in active_keys:
        if key in values:
            index = list(weights.keys()).index(key)
            total += values[index] * weights[key] * scaling_factor
    
    # Misleading normalization step (not applied)
    if total > 100:
        normalized = total / 1.8  # dead code path due to logic
    
    adjustment = 0
    for val in values:
        if val % 2 == 0:
            adjustment += 0.1
    
    final_score = int(total - adjustment)  # actual assignment point
    return final_score

# Input data
metric_weights = {
    'latency': 0.9,
    'throughput': 0.7,
    'reliability': 0.4,
    'bandwidth': 0.8
}

raw_data = [12, 18, 7, 22]

# Trigger analysis (distraction)
dummy_trend = analyze_trends(raw_data, threshold=10)

# Critical execution point
final_score = evaluate_performance(metric_weights, raw_data)

print(f"Result: {final_score}")