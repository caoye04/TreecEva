def analyze_performance(metrics):
    # Irrelevant transformation
    normalized = {k: v ** 0.5 for k, v in metrics.items() if v > 10}
    adjusted = {}
    for key, val in metrics.items():
        if val < 5:
            adjusted[key] = val * 1.5
        elif val > 20:
            adjusted[key] = val * 0.9
        else:
            adjusted[key] = val
    
    # Distractor computation
    outlier_count = sum(1 for x in metrics.values() if x < 5 or x > 25)
    adjustment_factor = 1.05 if outlier_count > 2 else 0.98
    
    # Relevant aggregation
    base_score = sum(adjusted.values()) / len(adjusted)
    return base_score

# Weighted scoring with lambda
compute_weight = lambda w, f: w * (1.1 if f == 'accuracy' else 1.0)

results = {
    'accuracy': 22,
    'latency': 18,
    'throughput': 25,
    'memory_usage': 12,
    'stability': 28
}

weights = {
    'accuracy': 0.3,
    'latency': 0.2,
    'throughput': 0.25,
    'memory_usage': 0.15,
    'stability': 0.1
}

# Intermediate irrelevant mapping
performance_tiers = {
    'high': [k for k, v in results.items() if v >= 20],
    'medium': [k for k, v in results.items() if 10 <= v < 20],
    'low': [k for k, v in results.items() if v < 10]
}

# Unused helper function (dead code)
def validate_input(data):
    return all(isinstance(x, (int, float)) and x >= 0 for x in data.values())

# Another distractor variable
baseline_average = sum(results.values()) / len(results)

# Main processing chain
base_performance = analyze_performance(results)

weighted_components = {}
for metric, value in results.items():
    weight = weights[metric]
    adjusted_weight = compute_weight(weight, metric)
    weighted_components[metric] = value * adjusted_weight

# Secondary irrelevant calculation
harmonic_mean = len(results) / sum(1/v for v in results.values())

# Final score depends only on aggregated weighted sum and base performance
aggregated_weighted = sum(weighted_components.values())

# Key statement
final_score = (base_performance * 0.4) + (aggregated_weighted * 0.6)

print(f"Result: {final_score}")