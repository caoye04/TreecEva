from itertools import compress, cycle
import math

# Simulated sensor data processing pipeline for environmental monitoring station
def collect_sensor_data():
    return [23.4, 19.5, 25.1, 20.0, 22.3, 18.7, 24.0]

# Irrelevant auxiliary function - simulates humidity adjustment (not used in final calculation)
def adjust_for_humidity(values, humidity=0.65):
    return [v * (1 + 0.1 * math.sin(humidity)) for v in values]

# Noise filter using moving average - partially relevant but bypassed by control flag
def smooth_signal(signal, window_size=3):
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - window_size + 1)
        smoothed.append(sum(signal[start:i+1]) / (i - start + 1))
    return smoothed

# Legacy system compatibility layer - unused but plausible
legacy_mode = False
temp_offset_table = {i: i * 0.05 for i in range(10)}

# Core transformation: normalize and classify readings
def classify_reading(temp):
    if temp < 20:
        return 1
    elif temp < 23:
        return 2
    else:
        return 3

# Scoring heuristics based on classification
scoring_rules = {
    1: lambda x: x * 0.8,
    2: lambda x: x * 1.1,
    3: lambda x: x * 1.3
}

# Secondary metrics derived from raw classifications
def compute_stability_index(classifications):
    changes = sum(1 for i in range(1, len(classifications)) if classifications[i] != classifications[i-1])
    return round((1 - changes / (len(classifications) - 1)) * 100, 2) if len(classifications) > 1 else 100.0

# Data validity checker - always passes in current mode
validation_threshold = 0.85
def validate_integrity(data):
    return len([x for x in data if x > 15]) / len(data) >= validation_threshold

# Main processing workflow
raw_temps = collect_sensor_data()

# Misleading preprocessing branch
if legacy_mode:
    processed_temps = [t + temp_offset_table[i % 10] for i, t in enumerate(raw_temps)]
else:
    processed_temps = [round(t, 1) for t in raw_temps]  # Actual path

# Apply classification
classified_zones = [classify_reading(t) for t in processed_temps]

# Compute auxiliary metrics (some used, some not)
base_scores = [scoring_rules[cls](temp) for cls, temp in zip(classified_zones, processed_temps)]
stability_metric = compute_stability_index(classified_zones)
variance_score = round(math.sqrt(sum((x - sum(processed_temps)/len(processed_temps))**2 for x in processed_temps) / len(processed_temps)), 2)

# Unused diagnostic metrics - red herrings
spike_count = sum(1 for i in range(1, len(processed_temps)) if abs(processed_temps[i] - processed_temps[i-1]) > 2.0)
drift_estimate = (processed_temps[-1] - processed_temps[0]) / len(processed_temps)

# Weighted metric combination
metrics = {
    'thermal_load': sum(base_scores),
    'system_stability': stability_metric,
    'uniformity': 100 - variance_score,
    'noise_level': spike_count * -5.0  # This will be masked out
}

# Dynamic weight assignment with masking
weight_config = {
    'thermal_load': 0.4,
    'system_stability': 0.3,
    'uniformity': 0.3,
    'noise_level': 0.0  # Effectively ignored
}

# Mask out zero-weight components
active_metrics = list(compress(metrics.keys(), [weight_config[k] > 0 for k in metrics.keys()]))
active_weights = [weight_config[k] for k in active_metrics]

# Final aggregation function
def aggregate_performance(met_dict, weights):
    selected = {k: met_dict[k] for k in active_metrics}
    total = sum(selected[k] * weights[i] for i, k in enumerate(selected))
    return round(total, 4)

# Critical execution point
final_score = aggregate_performance(metrics, weights)

# Output result
print(f"Result: {final_score}")