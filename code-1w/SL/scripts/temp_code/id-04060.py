def analyze_trend(data, threshold=0.5):
    above_threshold = [x for x in data if x > threshold]
    below_threshold = [x for x in data if x <= threshold]
    trend_ratio = len(above_threshold) / len(below_threshold) if below_threshold else 0
    return trend_ratio > 1.5


def validate_readings(logs):
    valid_count = 0
    total_magnitude = 0.0
    for log in logs:
        magnitude = sum([abs(x) for x in log])
        total_magnitude += magnitude
n    avg_magnitude = total_magnitude / len(logs) if logs else 0
    
    # Distractor: irrelevant filtering
    filtered = [log for log in logs if sum(log) > avg_magnitude * 0.8]
    valid_count = len(filtered)
    return valid_count

# Simulated sensor readings over time
baseline = [0.3, 0.7, 0.4, 0.9]
readings = [
    [0.2, 0.8, 0.6],
    [0.9, 0.1, 0.5],
    [0.7, 0.6, 0.8],
    [0.4, 0.3, 0.2],
    [0.9, 0.9, 0.7]
]

# Auxiliary computation - partially relevant
normalization_factor = sum(baseline) / len(baseline)
scaled_readings = [[val * normalization_factor for val in r] for r in readings]

# Secondary metric (distractor)
count_high = 0
for row in scaled_readings:
    for val in row:
        if val > 0.7:
            count_high += 1

# Core logic embedded in function
status_flags = [analyze_trend(r, 0.6) for r in scaled_readings]
activation_count = sum(1 for flag in status_flags if flag)

# Main performance calculation
baseline_active = analyze_trend(baseline, 0.6)

# Conditional expression used
base_multiplier = 1.5 if baseline_active else 0.8

# Final score depends only on activation_count and base_multiplier
final_score = int(activation_count * 10 * base_multiplier)

# Irrelevant aggregation
total_elements = sum(len(r) for r in readings)
dummy_metric = total_elements / (activation_count + 1) if activation_count != -1 else 0

# This print is required for output visibility
print(f"Result: {final_score}")