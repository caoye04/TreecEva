def analyze_trends(data, threshold=0.5):
    trends = []
    for i, value in enumerate(data):
        if value > threshold:
            trends.append((i, value))
    return trends

# Simulated sensor readings over time
readings = [0.3, 0.7, 0.4, 0.9, 0.6, 0.2, 0.8]

# Extract significant upward trends
significant_events = analyze_trends(readings)

# Irrelevant transformation - distractor
transformed = list(map(lambda x: (x[0], round(x[1] * 100)), significant_events))

# Auxiliary data structures with partial relevance
baseline = [0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8]
deviations = [abs(readings[i] - baseline[i]) for i in range(len(readings))]

# Misleading cumulative calculation (unused)
cumulative_drift = sum(deviations) * 0.1

# Key metrics for performance evaluation
metrics = [
    len(significant_events),
    sum(x[1] for x in significant_events),
    len([d for d in deviations if d > 0.1])
]

# Weighting scheme - some weights are red herrings
all_weights = [0.8, 0.5, 1.2, 0.3, 0.9]
weights = [all_weights[i] for i in [0, 1, 4]]  # Only first, second, and last used

# Dead code path - misleading conditional
if cumulative_drift > 1.0:
    final_score = -1
else:
    # Core logic embedded in distraction
    weighted_sum = sum(m * w for m, w in zip(metrics, weights))
    adjustment = len(transformed) * 0.2  # Minor correction factor
    final_score = weighted_sum - adjustment

# Additional irrelevant computation
noise_estimate = sum(1 for d in deviations if d < 0.05)

# Final output
Result: {final_score}