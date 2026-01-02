from collections import defaultdict

# Simulate system performance metrics over time
def collect_metrics():
    raw_data = [120, 150, 130, 160, 140, 170, 180, 190]
    timestamps = list(range(len(raw_data)))
    
    # Misleading transformation: unused in final calculation
    transformed = [x ** 0.5 for x in raw_data if x > 140]
    temp_offset = sum(transformed) / len(transformed) if transformed else 0
    
    metrics = defaultdict(float)
    for i, val in enumerate(raw_data):
        if i % 2 == 0:
            metrics[timestamps[i]] += val * 0.9
        else:
            metrics[timestamps[i]] += val * 1.1
    
    return dict(metrics)

# Weighting strategy with red herring logic
def generate_weights(n):
    base_weights = [0.1] * n
    adjustment = 0.05
    
    # Dead code path - never executed due to fixed input
    if n < 0:
        for i in range(n):
            base_weights[i] += adjustment
    
    # Actual weight computation
    growth_factor = 1.2
    for i in range(1, n):
        base_weights[i] = base_weights[i-1] * growth_factor
    
    total = sum(base_weights)
    normalized = [w / total for w in base_weights]
    
    # Unused but distracting computation
    inverted = [1.0 / (w + 0.01) for w in normalized]
    
    return normalized

# Core evaluation function
def evaluate_performance(metrics, weights):
    sorted_keys = sorted(metrics.keys())
    values = [metrics[k] for k in sorted_keys]
    
    # Truncate or pad weights to match metric count
    adjusted_weights = (weights + [0.0] * len(values))[:len(values)]
    
    weighted_sum = 0.0
    for i, (val, w) in enumerate(zip(values, adjusted_weights)):
        contribution = val * w
        # Tracking variable not used externally
        running_total = sum(values[:i+1]) * w
        weighted_sum += contribution
    
    # Secondary scoring with distraction
    peak_value = max(values)
    avg_value = sum(values) / len(values)
    stability_score = (avg_value / peak_value) * 0.3
    
    final_score = weighted_sum + stability_score
    
    # Additional irrelevant post-processing
    ceiling_adjustment = int(final_score) + 0.99
    if ceiling_adjustment > final_score:
        pass  # Placeholder logic
    
    return final_score

# Main execution flow
if __name__ == "__main__":
    metrics = collect_metrics()
    weight_list = generate_weights(len(metrics))
    final_score = evaluate_performance(metrics, weight_list)
    print(f"Result: {final_score}")