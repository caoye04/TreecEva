def analyze_trends(values):
    trend_flags = []
    for i, val in enumerate(values):
        if i == 0:
            trend_flags.append(0)
        else:
            diff = val - values[i-1]
            trend_flags.append(1 if diff > 0 else (-1 if diff < 0 else 0))
    return trend_flags

values = [12, 15, 15, 18, 14, 20, 22]
trend_result = analyze_trends(values)

# Irrelevant transformation (dead-end computation)
transformed = [x * 2 + 1 for x in values if x % 2 == 0]
sum_transformed = sum(transformed)  # Not used later

weights = [0.1, 0.2, 0.15, 0.25, 0.1, 0.05, 0.15]
data = [3, 7, 4, 9, 6, 8, 5]

# Misleading normalization (not actually applied)
normalized_data = [d / max(data) for d in data]
scale_factor = 10  # Distractor variable

offset_correction = 0
for idx, (d, w) in enumerate(zip(data, weights)):
    if d > 6:
        offset_correction += w * 0.5
    elif d < 5:
        offset_correction -= w * 0.3

# Simulate confidence weighting with dummy logic
confidence_scores = []
for d in data:
    if d >= 7:
        confidence_scores.append(1.1)
    elif d <= 3:
        confidence_scores.append(0.8)
    else:
        confidence_scores.append(1.0)

weighted_sum = 0.0
for i in range(len(data)):
    weighted_sum += data[i] * weights[i] * confidence_scores[i]

# Extra unused metric
binary_flags = [1 if c > 1.0 else 0 for c in confidence_scores]
flag_count = sum(binary_flags)  # Unused

penalty = 0
for i, t in enumerate(trend_result):
    if t == 1 and data[i] < 6:
        penalty += weights[i] * 1.2

final_score = weighted_sum - penalty + offset_correction

Result: {final_score}