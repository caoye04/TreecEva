def analyze_trend(data, threshold=0.5):
    trend = list(map(lambda x: 1 if x > threshold else -1, data))
    return trend

# Simulate sensor readings over time
readings = [0.3, 0.6, 0.4, 0.8, 0.2]
smoothed = [round(x * 1.1, 1) for x in readings]
adjusted = [min(x, 1.0) for x in smoothed]

# Extract trend direction
movement = analyze_trend(adjusted)

# Irrelevant transformation (distractor)
decay_curve = [x ** 0.5 for x in readings if x < 0.5]
baseline_shift = sum(decay_curve) / len(decay_curve) if decay_curve else 0.0

# Weighting scheme for performance metrics
weights = {
    'stability': 0.3,
    'responsiveness': 0.4,
    'consistency': 0.2,
    'drift': 0.1
}

# Simulated metric scores (some are red herrings)
metrics = {
    'stability': sum(1 for i in range(1, len(adjusted)) if abs(adjusted[i] - adjusted[i-1]) < 0.3),
    'responsiveness': sum(1 for m in movement if m == 1),
    'consistency': len([x for x in readings if 0.35 <= x <= 0.65]),
    'drift': baseline_shift * 10,  # semi-relevant but down-weighted
    'noise_floor': sum(1 for x in adjusted if x < 0.4),  # unused distractor
    'peak_count': len([x for x in adjusted if x > 0.7])   # unused distractor
}

# Aggregation logic with lambda-based weighting
def aggregate_performance(mets, wts):
    weighted_sum = 0.0
    total_weight = 0.0
    for key, weight in wts.items():
        if key in mets:
            weighted_sum += mets[key] * weight
            total_weight += weight
    return int(round(weighted_sum / total_weight)) if total_weight > 0 else 0

# Final computation
intermediate_bias = sum(metrics.values()) * 0.01  # minor adjustment not used
normalization_factor = max(metrics.values()) or 1  # dead-end variable

final_score = aggregate_performance(metrics, weights)

print(f"Result: {final_score}")