def analyze_trend(data, threshold=0.5):
    trend_scores = []
    for i in range(1, len(data)):
        diff = data[i] - data[i-1]
        if diff > threshold:
            trend_scores.append(1)
        elif diff < -threshold:
            trend_scores.append(-1)
        else:
            trend_scores.append(0)
    return trend_scores

# Simulate sensor readings over time
readings = [0.1, 0.6, 0.4, 0.9, 1.2, 0.8, 0.3, 0.7]
trends = analyze_trend(readings, threshold=0.35)

# Misleading auxiliary calculation (distractor)
smoothed = [round((readings[i] + readings[i+1]) / 2, 2) for i in range(len(readings)-1)]
noise_estimate = sum(abs(readings[i+1] - readings[i]) for i in range(len(readings)-1)) / len(readings)

# Key performance metrics (some are red herrings)
metrics = {
    'stability': sum(1 for x in trends if x == 0),
    'positive_momentum': sum(1 for x in trends if x == 1),
    'volatility': sum(1 for x in trends if x == -1),
    'baseline_drift': sum(readings) / len(readings),
    'peak_count': len([x for x in readings if x > 0.75])
}

# Weight mapping - only some weights affect final result
weights = {
    'stability': 0.2,
    'positive_momentum': 0.5,
    'volatility': -0.3,
    'baseline_drift': 0.0,  # Neutral weight (distractor)
    'peak_count': 0.0       # Irrelevant in final formula
}

# Helper lambda for weighted contribution (used in evaluation)
weighted_contribution = lambda m, w: sum(m[key] * w[key] for key in m if key in w)

# Secondary analysis with dead-end logic (misleading path)
if metrics['volatility'] > 2:
    adjusted_volatility = metrics['volatility'] * 1.2
else:
    adjusted_volatility = metrics['volatility']

# Unused transformation (dead code - distractor)
dummy_transform = [x ** 2 for x in readings if x > 0.5]
dummy_sum = sum(dummy_transform)

# Core evaluation logic
normalization_factor = max(metrics.values()) or 1
efficiency_ratio = metrics['positive_momentum'] / normalization_factor
risk_penalty = metrics['volatility'] * 0.1

# Final scoring using only subset of metrics
partial_metrics = {k: v for k, v in metrics.items() if k in ['stability', 'positive_momentum', 'volatility']}
raw_score = weighted_contribution(partial_metrics, weights)
scaled_score = raw_score * efficiency_ratio
final_score = int(scaled_score - risk_penalty + 10)  # Final deterministic assignment

# Print result as required
print(f"Result: {final_score}")