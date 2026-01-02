def analyze_trends(values):
    trend_data = []
    for i, val in enumerate(values):
        if i == 0:
            trend_data.append(0)
        else:
            trend_data.append(val - values[i-1])
    return trend_data

values = [12, 15, 14, 18, 20, 25]
trend_result = analyze_trends(values)

extra_calc = sum([x**2 for x in trend_result if x > 0])
ignored_total = extra_calc * 0.1

weights = [0.1, 0.2, 0.1, 0.3, 0.2, 0.1]
data = [30, 45, 20, 50, 60, 40]

# Simulate sensor drift correction (irrelevant to final result)
sensor_offset = 2.5
drift_corrected = [d - sensor_offset for d in data]

# Misleading normalization path (not used in final computation)
normalized_data = [d / sum(data) for d in data]
scaling_factor = 100
rescaled = [int(n * scaling_factor) for n in normalized_data]

# Real processing begins here
combined_pairs = list(zip(data, weights))
weighted_sum = 0
weight_accum = 0

for datum, weight in combined_pairs:
    weighted_sum += datum * weight
    weight_accum += weight

adjusted_mean = weighted_sum / weight_accum if weight_accum != 0 else 0

# Secondary adjustment based on trend magnitude
trend_magnitude = sum(abs(x) for x in trend_result)
magnitude_factor = 1 + (trend_magnitude / 100)

interim_score = adjusted_mean * magnitude_factor

# Apply bonus only if trend is consistently positive
is_increasing = all(t > 0 for t in trend_result[1:])
bonus_applied = 5 if is_increasing else 0

final_score = interim_score + bonus_applied

# Dead code branch — never executed but adds cognitive load
if __debug__:
    import sys
    sys.stdout.write('Debug mode active\n')

print(f'Result: {final_score}')