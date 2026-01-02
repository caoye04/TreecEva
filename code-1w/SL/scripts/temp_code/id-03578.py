def analyze_trend(data, threshold=50):
    above_threshold = {x for x in data if x > threshold}
    below_threshold = {x for x in data if x <= threshold}
    trend_value = len(above_threshold) - len(below_threshold)
    return trend_value


def normalize_readings(raw_values):
    min_val, max_val = min(raw_values), max(raw_values)
    range_val = max_val - min_val or 1
    normalized = [(v - min_val) / range_val * 100 for v in raw_values]
    adjusted = [round(n + 10) for n in normalized]  # Simulated calibration
    return adjusted

baseline = [23, 45, 67, 89, 12]
readings = [33, 55, 66, 77, 88, 44, 55]

# Preprocessing step with distractor variables
summed_data = sum(baseline) + sum(readings)  # irrelevant aggregation
duplicate_count = len(readings) - len(set(readings))  # red herring metric

processed = normalize_readings(readings)
primary_trend = analyze_trend(processed, threshold=60)
secondary_trend = analyze_trend(processed, threshold=40)

# Misleading intermediate calculation
shadow_factor = (primary_trend * 2) + (duplicate_count - 5) if primary_trend > 0 else 0

# Core logic embedded among distractions
efficiency_ratio = (secondary_trend + abs(primary_trend)) / 2.0 if secondary_trend != 0 else 0.0

scaling_factor = 1.5 if efficiency_ratio >= 2.0 else 1.2  # conditional expression

adjusted_trend = primary_trend * scaling_factor

# Final performance calculation
final_score = 0
if adjusted_trend > 0:
    final_score = int(adjusted_trend * 10)
elif adjusted_trend < 0:
    final_score = int(adjusted_trend * 5)
else:
    final_score = 100

# Irrelevant print statements (dead code for distraction)
# print(f'Shadow factor: {shadow_factor}')
# print(f'Summed data: {summed_data}')

Result: final_score