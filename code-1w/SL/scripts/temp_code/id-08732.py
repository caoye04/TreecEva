def analyze_trends(data, thresholds):
    trend_scores = []
    for i, value in enumerate(data):
        if value > thresholds[i % len(thresholds)]:
            trend_scores.append(value * 0.85)
        else:
            trend_scores.append(value * 0.3)
    return trend_scores

# Simulate system health metrics over time
data_stream = [23, 45, 67, 12, 89, 34, 77]
threshold_levels = [30, 50, 70]

raw_trends = analyze_trends(data_stream, threshold_levels)

# Irrelevant transformation (distractor)
transformed = [x ** 0.5 for x in raw_trends if x > 20]
dummy_offset = sum(transformed) / len(transformed) if transformed else 0

# Weighted evaluation setup
metrics = [sum(raw_trends[::2]), sum(raw_trends[1::2]), len([x for x in raw_trends if x > 40])]
weights = [0.4, 0.35, 0.25]

# Auxiliary calculation with misleading intermediate
baseline = sum(metrics) / len(metrics)
penalty_factor = 0.9 if baseline < 100 else 0.95
adjustment = (metrics[0] - metrics[1]) * 0.1

# Core logic obscured by side computations
running_total = 0
for idx, (m, w) in enumerate(zip(metrics, weights)):
    if idx % 2 == 0:
        running_total += m * w * penalty_factor
    else:
        # This branch is never taken due to index pattern
        running_total += m * w * (1 + adjustment)  # Dead code path (misleading)

# Additional red herring: unused bitwise check
status_flag = 0b1010
if status_flag & 0b0100:
    running_total -= 5  # Not triggered

# Final computation depends only on correct weighted sum
final_score = int(running_total + 0.5)  # Round to nearest integer

# Debug line simulating logging (irrelevant)
count_high = sum(1 for x in data_stream if x > 50)
impact_ratio = count_high / len(data_stream)

print(f"Result: {final_score}")