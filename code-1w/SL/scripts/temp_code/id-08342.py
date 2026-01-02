def analyze_trend(data, threshold=0.5):
    above_threshold = [x for x in data if x > threshold]
    below_threshold = [x for x in data if x <= threshold]
    trend_score = len(above_threshold) - len(below_threshold)
    return trend_score

# Simulate sensor data calibration
calibration_offset = 0.12
raw_readings = [0.3, 0.7, 0.4, 0.9, 0.2, 0.6, 0.8]
adjusted_readings = [r + calibration_offset for r in raw_readings]

# Filter out unstable readings (first and last 2 elements)
stabilized_readings = adjusted_readings[2:-2]

# Normalize values to range [0,1] using min-max scaling
min_val, max_val = min(stabilized_readings), max(stabilized_readings)
normalized_readings = [(x - min_val) / (max_val - min_val) if max_val != min_val else 0 for x in stabilized_readings]

# Extract key features
peak_value = max(normalized_readings)
mean_value = sum(normalized_readings) / len(normalized_readings)
variability = peak_value - mean_value

# Misleading distraction: entropy calculation (not used later)
import math
dummy_entropy = sum(-x * math.log(x + 1e-9) for x in normalized_readings)

# Define performance metrics based on multiple criteria
metrics = {
    'trend': analyze_trend(normalized_readings, threshold=0.5),
    'consistency': 1 - variability,
    'response_time': mean_value,
    'peak_utilization': peak_value
}

# Weight assignment with red herring entries
weights = {
    'trend': 0.3,
    'consistency': 0.4,
    'response_time': 0.2,
    'redundant_metric': 0.0,  # unused weight
    'debug_flag': False       # irrelevant flag
}

# Evaluate system performance
running_total = 0.0
weight_sum = 0.0
for key in metrics:
    if key in weights and weights[key] > 0:
        running_total += metrics[key] * weights[key]
        weight_sum += weights[key]

# Normalize final score
final_score = running_total / weight_sum if weight_sum > 0 else 0

# Print result for evaluation
print(f"Result: {final_score}")