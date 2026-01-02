def analyze_trends(data, threshold=0.5):
    trends = {}
    for i, value in enumerate(data):
        if value > threshold:
            trends[i] = 'positive'
        elif value < -threshold:
            trends[i] = 'negative'
        else:
            trends[i] = 'neutral'
    return trends

values = [0.6, -0.3, 0.8, 0.0, -0.7, 0.4]
trend_map = analyze_trends(values)

# Simulate feedback weights from multiple sources
weights = [1, 2, 1, 3, 2, 1]
feedback_map = {i: values[i] * weights[i] for i in range(len(values))}

# Distractor: irrelevant computation on trend keys
key_analysis = sum(k * (k % 2) for k in trend_map.keys() if trend_map[k] == 'positive')

# Misleading normalization attempt
normalized_feedback = list(map(lambda x: round(x + 0.1, 2), feedback_map.values()))

# Dead code path: never used later
if len(normalized_feedback) > 10:
    adjusted = [x * 1.1 for x in normalized_feedback]
else:
    temp_sum = sum(normalized_feedback[:3])  # unused variable

# Core logic hidden among distractions
def aggregate_performance(feedbacks):
    total = 0
    count = 0
    for idx, fb in feedbacks.items():
        if abs(fb) >= 0.5:
            total += fb ** 2
            count += 1
    if count == 0:
        return 0.0
    avg_sq = total / count
    return round(avg_sq * 100, 4)

intermediate_calc = sum(v**2 for v in values)  # irrelevant to final result

final_score = aggregate_performance(feedback_map)
print(f"Result: {final_score}")