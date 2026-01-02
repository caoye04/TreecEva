import math

# Simulated sensor data processing for environmental monitoring system
def analyze_readings(readings):
    baseline = 24.7
    adjusted = [(r - baseline) ** 2 for r in readings]
    return sum(adjusted) / len(adjusted)

# Secondary metric: stability index
def calculate_stability(values):
    if len(values) < 2:
        return 0
    diffs = [abs(values[i] - values[i-1]) for i in range(1, len(values))]
    return round(sum(diffs) / len(diffs), 3)

# Red herring function - looks relevant but not used in final path
def deprecated_normalization(arr):
    max_val, min_val = max(arr), min(arr)
    return [(x - min_val) / (max_val - min_val) for x in arr]

# Core transformation pipeline
raw_data = [22.1, 25.6, 24.3, 26.8, 23.9, 25.1, 24.0, 27.2, 22.5, 26.4]

scaling_factor = 1.85
offset_correction = 0.12

# Irrelevant pre-processing (distractor)
distorted_data = [x * scaling_factor + offset_correction for x in raw_data]
noise_floor = sum([math.sin(x) for x in distorted_data])  # Dead-end computation

# Key analysis chain
variance_metric = analyze_readings(raw_data)
stability_metric = calculate_stability(raw_data)

# Composite scoring with weighted factors
weight_a = 0.6
weight_b = 0.4

intermediate_score = (variance_metric * weight_a) + (stability_metric * weight_b)

efficiency_score = 100 * math.exp(-intermediate_score / 10)

# Unused alternative scoring method (distractor)
alt_scores = list(map(lambda x: x ** 0.5, raw_data))
mean_alt = sum(alt_scores) / len(alt_scores)
penalty_factor = mean_alt > 4.8

# Final aggregation step (contains target variable)
final_output = process_metrics(raw_data) if 'process_metrics' in globals() else efficiency_score

# Define missing function to avoid error and maintain flow
def process_metrics(data):
    variance = analyze_readings(data)
    stability = calculate_stability(data)
    score = 100 * math.exp(-((0.6 * variance) + (0.4 * stability)) / 10)
    return score

# Update final output correctly
final_output = process_metrics(raw_data)

# Print result as required
print(f"Target result: {efficiency_score}")