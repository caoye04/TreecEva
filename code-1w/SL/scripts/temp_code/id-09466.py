def analyze_trends(data, window_size):
    trends = []
    for i in range(len(data) - window_size + 1):
        segment = data[i:i + window_size]
        avg = sum(segment) / window_size
        trend = 1 if segment[-1] > avg * 1.1 else (-1 if segment[-1] < avg * 0.9 else 0)
        trends.append(trend)
    return trends

# Simulate sensor readings over time
temperature_data = [23.5, 24.1, 25.3, 24.9, 26.7, 27.2, 25.8, 24.6, 23.9, 24.2]

# Extract short-term trend using moving window
temp_trends = analyze_trends(temperature_data, 3)

# Irrelevant calculation: average fluctuation (not used later)
fluctuations = [abs(temperature_data[i] - temperature_data[i-1]) for i in range(1, len(temperature_data))]
avg_fluctuation = round(sum(fluctuations) / len(fluctuations), 3)

# System metrics and corresponding weights
metrics = [
    sum(1 for t in temp_trends if t == 1),           # number of positive trends
    sum(1 for t in temp_trends if t == -1),          # number of negative trends
    len([t for i, t in enumerate(temp_trends) if i % 2 == 0]),  # even-indexed trends
    max(temp_trends, default=0),                    # peak trend value
]

weights = [0.4, -0.3, 0.1, 0.2]

# Misleading intermediate transformation (semi-relevant but unused)
normalized_metrics = [m / (sum(metrics) or 1) for m in metrics]
distorted_score = sum(m**1.1 * w for m, w in zip(normalized_metrics, weights))

# Core evaluation logic
def evaluate_performance(mets, wts):
    adjusted = [m * w for m, w in zip(mets, wts)]
    base_score = sum(adjusted)
    penalty = 0
    if mets[0] < mets[1]:  # more negative trends than positive
        penalty = -2.5
    elif mets[0] > 2 * (mets[1] or 1):  # significantly more positives
        penalty = 1.8
    
    # Additional rule: if max trend is positive and index is odd
    trend_indices = [i for i, t in enumerate(temp_trends) if t == max(temp_trends, default=0)]
    bonus = 0.7 if any(i % 2 == 1 for i in trend_indices) else 0
    
    return base_score + penalty + bonus

# Final computation
final_score = evaluate_performance(metrics, weights)

# Print result as required
print(f"Result: {final_score}")