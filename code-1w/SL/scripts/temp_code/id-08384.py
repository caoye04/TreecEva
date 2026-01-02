def transform_sequence(seq, factor):
    """Irrelevant transformation function (dead code path)"""
    return [x * factor + 2 for x in seq if x % 3 != 0]

# Sensor simulation parameters (some are decoys)
decoay_constant = 0.045
time_step = 0.1
sample_size = 512
scaling_factor = 1.75
offset_correction = -0.5

# Real-time signal buffers (mix of relevant and irrelevant)
signal_buffer_a = [i * 1.5 + 0.25 for i in range(10)]
signal_buffer_b = [i ** 0.5 for i in range(10)]

# Core diagnostic configuration
baseline_readings = [85, 92, 78, 96, 88, 77, 91, 84, 90]
threshold_map = {
    'low': 75,
    'optimal': 85,
    'high': 95,
    'critical': 100
}

# Data calibration factors (only some used)
calibration_x = 1.08
calibration_y = 0.97  # Unused
calibration_z = 1.03  # Unused

# Simulated raw sensor data
raw_data = [87, 95, 73, 98, 82, 76, 93, 89, 81]

# Filtering irrelevant noise (red herring operation)
filtered_data = [x for x in raw_data if x > 70]

# Actual processing chain
processed_data = []
for val in raw_data:
    adjusted = val * 1.05  # Apply known correction
    if adjusted < threshold_map['low']:
        processed_data.append(int(adjusted - 2))
    elif adjusted > threshold_map['high']:
        processed_data.append(int(adjusted + 1))
    else:
        processed_data.append(int(adjusted))

# Auxiliary diagnostic counters (distractors)
anomaly_count = 0
critical_flags = 0
suppressed_warnings = 0

# Secondary analysis (partially dead logic)
for reading in processed_data:
    if reading < 80:
        anomaly_count += 1
    if reading >= threshold_map['critical']:
        critical_flags += 1
        suppressed_warnings += 1  # Misleading increment

# Decoy statistical summary
data_mean = sum(processed_data) / len(processed_data)
data_variance = sum((x - data_mean) ** 2 for x in processed_data) / len(processed_data)

# Key diagnostic logic
status_counter = {'stable': 0, 'elevated': 0, 'critical': 0}
for item in processed_data:
    if item < threshold_map['optimal']:
        status_counter['stable'] += 1
    elif item < threshold_map['critical']:
        status_counter['elevated'] += 1
    else:
        status_counter['critical'] += 1

# Complex decision matrix with red herrings
boost_factor = 1.2 if status_counter['elevated'] > 2 else 0.8
penalty = 5 if anomaly_count > 3 else 0
bonus = 10 if critical_flags == 0 else -3  # Misleading bonus logic

# Final diagnostic computation
base_score = status_counter['stable'] * 8 + status_counter['elevated'] * 5 + status_counter['critical'] * 2
adjusted_score = base_score * boost_factor - penalty + bonus

# Normalization against baseline length
normalized_index = adjusted_score / len(baseline_readings)

# Final diagnostic: this is the actual target variable
final_diagnostic = int(round(normalized_index * 10))

# Print result as required
print(f"Result: {final_diagnostic}")