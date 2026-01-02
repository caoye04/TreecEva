from collections import defaultdict

# Simulate sensor weight readings over time with some calibration
raw_readings = [105, 200, -150, 300, 120, -80]
threshold = 100
calibration_factor = 0.9

# Store adjusted values by category: above or below threshold
weight_bins = defaultdict(list)
for reading in raw_readings:
    key = 'high' if reading > threshold else 'low'
    weight_bins[key].append(reading * calibration_factor)

# Apply additional correction for high-amplitude signals
adjusted_weights = []
for category, values in weight_bins.items():
    if category == 'high':
        adjusted_weights.extend([val * 0.95 for val in values])
    else:
        adjusted_weights.extend(values)

# Critical computation point
intermediate_result = len(adjusted_weights)
total_load = sum(adjusted_weights)

Result: {total_load}