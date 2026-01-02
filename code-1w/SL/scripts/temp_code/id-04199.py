from itertools import cycle

# Simulate time-series sensor data over 5 cycles
time_points = [0.1, 0.2, 0.3, 0.4, 0.5]
sensor_a = [10, 15, 20, 25, 30]
sensor_b = [5,  8, 12, 18, 22]

# Irrelevant auxiliary data (distractor)
baseline_offset = 7
calibration_factor = 1.05
noise_floor = [0.01, 0.02, 0.015, 0.03, 0.025]

# Misleading intermediate computation (dead path)
adjusted_noise = [round((x * calibration_factor) + baseline_offset, 3) for x in noise_floor]

# Real processing: normalize sensor readings
max_sensor_a = max(sensor_a)
normalized_a = [round(x / max_sensor_a, 3) for x in sensor_a]

max_sensor_b = max(sensor_b)
normalized_b = [round(x / max_sensor_b, 3) for x in sensor_b]

# Combine normalized values using alternating pattern (itertools used)
combined_signal = []
cycle_pattern = cycle([0, 1])
for i in range(len(normalized_a)):
    if next(cycle_pattern):
        combined_signal.append(normalized_a[i] * normalized_b[i])
    else:
        combined_signal.append((normalized_a[i] + normalized_b[i]) / 2)

# Compute dynamic metrics
mean_signal = sum(combined_signal) / len(combined_signal)
signal_variance = sum((x - mean_signal) ** 2 for x in combined_signal) / len(combined_signal)
skew_adjustment = (mean_signal * 0.95) if signal_variance > 0.05 else (mean_signal * 1.05)

# Define evaluation metrics (some are red herrings)
metrics = {
    'stability': round(1 / (signal_variance + 0.1), 3),
    'amplitude': max(combined_signal),
    'consistency': skew_adjustment,
    'baseline_rms': round(sum(x**2 for x in adjusted_noise)/len(adjusted_noise), 3),  # unused
    'temporal_drift': 0.0  # placeholder, not updated
}

# Weight assignment (only first three weights matter)
weights = {
    'stability': 0.4,
    'amplitude': 0.35,
    'consistency': 0.25,
    'baseline_rms': 0.0,  # irrelevant
    'temporal_drift': 0.0 # irrelevant
}

# Evaluate performance score
weighted_sum = 0.0
valid_keys = ['stability', 'amplitude', 'consistency']
for key in valid_keys:
    weighted_sum += metrics[key] * weights[key]

final_score = int(round(weighted_sum * 100))

# Print result as required
print(f"Result: {final_score}")