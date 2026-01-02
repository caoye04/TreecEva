def analyze_trend(data, threshold=5.0):
    above_threshold = [x for x in data if x > threshold]
    below_threshold = [x for x in data if x <= threshold]
    trend_value = len(above_threshold) - len(below_threshold)
    return trend_value

measurements = [3.2, 6.8, 7.1, 4.5, 9.0, 2.3, 8.8, 5.0, 1.9]

# Preliminary normalization (distraction)
normalized = [round(x * 1.05, 2) for x in measurements]
deviation_from_mean = sum([(x - sum(measurements)/len(measurements))**2 for x in measurements])

# Simulate auxiliary analysis (irrelevant but plausible)
count_high_peaks = 0
for val in measurements:
    if val > 7.0:
        count_high_peaks += 1

# Conditional expression used appropriately
is_volatility_high = 'yes' if deviation_from_mean > 30 else 'no'

# Key signal extraction
signal_strength = abs(analyze_trend(measurements, threshold=5.5))

# Weighted contribution from secondary pattern
secondary_weight = 0.7 if count_high_peaks >= 3 else 1.2
adjustment_factor = (sum(normalized) / sum(measurements)) if is_volatility_high == 'yes' else 1.0

# Core logic with distractors
base_metric = sum([x for x in measurements if x > 5.5])
penalty = len([x for x in measurements if x < 2.5]) * 2
bonus = 5 if signal_strength > 2 else 0

# Final performance evaluation (target line)
final_score = int((base_metric + bonus - penalty) * secondary_weight * adjustment_factor)

print(f"Result: {final_score}")