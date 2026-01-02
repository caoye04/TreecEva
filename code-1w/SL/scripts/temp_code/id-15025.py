from collections import defaultdict

# Simulate sensor readings over time with noise and calibration offsets
time_series_data = [102, 98, 100, 105, 97, 101, 99, 103, 96, 104]
noise_floor = 1.5
smoothing_factor = 0.8
base_value = sum(time_series_data) // len(time_series_data)

# Track frequency of deviations for anomaly detection (semi-relevant)
deviation_counts = defaultdict(int)
for reading in time_series_data:
    deviation = abs(reading - base_value)
    deviation_bin = max(1, int(deviation // 2))
    deviation_counts[deviation_bin] += 1

# Calculate moving average for trend analysis (distractor)
moving_avg = 0
for i, val in enumerate(time_series_data):
    weight = smoothing_factor ** (len(time_series_data) - i)
    moving_avg += val * weight
moving_avg /= sum(smoothing_factor ** i for i in range(len(time_series_data)))

# Simulate environmental compensation (partially relevant)
temperature_drift = -2.3
pressure_adjustment = 1.7
effective_drift = temperature_drift + pressure_adjustment
raw_offset = base_value - 100  # ideal baseline is 100

# Historical bias from previous calibrations (irrelevant)
historical_biases = [0.5, -0.3, 0.7, -0.6, 0.4]
bias_sum = sum(b for b in historical_biases if abs(b) > 0.4)
adjusted_bias = bias_sum * 0.1

# Core equilibrium logic
if raw_offset > 0:
    balance_offset = raw_offset * 0.9
else:
    balance_offset = raw_offset * 1.1

correction_factor = 1.0
if len(time_series_data) > 8:
    correction_factor *= 1.05
if deviation_counts[1] > 3:
    correction_factor *= 0.95

# Key computational statement
equilibrium_score = base_value + balance_offset * correction_factor

# Post-processing validation (distractor)
valid_range = (95, 105)
in_range_count = sum(1 for x in time_series_data if valid_range[0] <= x <= valid_range[1])
consistency_ratio = in_range_count / len(time_series_data)

# Final output
Result: {equilibrium_score}