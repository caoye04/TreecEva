def transform_signal(raw_values, factor):
    """Apply non-linear transformation to sensor signal (distraction function)."""
    return [abs(x) ** 0.5 * factor for x in raw_values]


def validate_checksum(data):
    """Validate data integrity using a checksum (dead code path - never called)."""
    return sum(data) % 256 == 0

# Simulated environmental sensor readings
primary_readings = [14, -28, 35, -47, 53, 62, -19, 8, 41]
secondary_readings = [3, 7, -12, 18, -25, 33, 42]

# Irrelevant baseline calibration values (distractor)
calibration_offsets = {
    'sensor_a': 0.98,
    'sensor_b': 1.02,
    'sensor_c': 0.95,
    'dummy_sensor': 2.1
}

# Noise filtering using moving average (irrelevant preprocessing)
def smooth_data(data, window=3):
    smoothed = []
    for i in range(len(data)):
        start = max(0, i - window + 1)
        end = i + 1
        smoothed.append(sum(data[start:end]) / (end - start))
    return smoothed

filtered_primary = smooth_data(primary_readings)
filtered_secondary = smooth_data(secondary_readings)

# Signal transformation with irrelevant factor (red herring)
scaled_primary = transform_signal(filtered_primary, 1.7)
scaled_secondary = transform_signal(filtered_secondary, 1.7)

# Core processing: extract anomalies based on magnitude thresholds
processed_data = [abs(x) for x in primary_readings]  # Only this matters

# Multiple distractor mappings (only one used)
threshold_map = {
    'low': 20,
    'medium': 35,
    'high': 50,
    'critical': 60,
    'unused_mode': 100
}

status_flags = [False, True, False, True, False]
flag_summary = any(status_flags) and len(status_flags) > 3  # Misleading boolean result

# Decoy statistical analysis (never used)
mean_value = sum(primary_readings) / len(primary_readings)
variance = sum((x - mean_value) ** 2 for x in primary_readings) / len(primary_readings)
std_deviation = variance ** 0.5

# Real computation begins here — complex conditional logic with enumeration and zip
anomaly_count = 0
for i, value in enumerate(processed_data):
    level = 'low'
    if value > threshold_map['medium']:
        level = 'medium'
        if value > threshold_map['high']:
            level = 'high'
            if value > threshold_map['critical']:
                level = 'critical'
    
    # Nested condition with logical operations (core logic)
    if (level == 'high' or level == 'critical') and (i % 2 == 0 or value < 65):
        anomaly_count += 1

# Secondary validation using zip and enumerate (essential step)
consistency_checks = []
for idx, (orig, proc) in enumerate(zip(primary_readings, processed_data)):
    if orig != 0:
        ratio = proc / abs(orig)
        consistency_checks.append(abs(ratio - 1.0) < 0.001)

# Final diagnostic depends only on these two values (hidden dependency)
base_score = anomaly_count * 100
adjustment = sum(1 for valid in consistency_checks if valid) * 2

# Critical statement
final_diagnostic = analyze_readings(processed_data, threshold_map)

# This function is defined late to obscure relevance
def analyze_readings(readings, config):
    """Determine system health based on processed sensor data."""
    count = 0
    for val in readings:
        if val > config['medium']:
            count += 1
            if val > config['high']:
                count += 2  # Weighted increment
    return count * 7 - 3

# Print final result
Result: {final_diagnostic}