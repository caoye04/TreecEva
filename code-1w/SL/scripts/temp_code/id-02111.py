def analyze_trends(data, threshold=10):
    moving_avg = []
    for i in range(2, len(data)):
        avg = (data[i-2] + data[i-1] + data[i]) / 3
        moving_avg.append(avg)
    return [x for x in moving_avg if x > threshold]


def calculate_weighted_sum(values):
    weights = [0.1, 0.2, 0.3, 0.4]
    total = 0.0
    for i in range(len(values)):
        total += values[i] * weights[i % 4]
    return total

# Simulate sensor stability index (distractor - not used in final result)
sensor_stability = [98, 95, 97, 96, 100, 99]
stability_avg = sum(sensor_stability) / len(sensor_stability)

# Core dataset: daily user engagement scores
engagement_data = [5, 12, 8, 15, 20, 18, 25, 17, 22]

# Extract trends above threshold
filtered_trends = analyze_trends(engagement_data, threshold=14)

# Apply transformation to normalize trend values
normalized_trends = [round(x * 0.85, 2) for x in filtered_trends]

# Calculate base metric (semi-relevant)
base_metric = sum(normalized_trends) / len(normalized_trends) if normalized_trends else 0

# Secondary processing: detect upward momentum
upward_momentum = 0
for i in range(1, len(normalized_trends)):
    if normalized_trends[i] > normalized_trends[i-1]:
        upward_momentum += 1

# Auxiliary debug log (dead code path - distractor)
debug_info = {"trends": filtered_trends, "base": base_metric, "momentum": upward_momentum}

# Key evaluation logic
adjustment_factor = 1.2 if upward_momentum > 2 else 0.9
raw_performance = calculate_weighted_sum(normalized_trends)
penalty = 0
if len(normalized_trends) < 4:
    penalty = 5

# Final performance score computation
final_score = (raw_performance * adjustment_factor) - penalty

# Print result as required
print(f"Result: {final_score}")