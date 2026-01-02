def sensor_calibration(raw_values):
    calibrated = []
    offset = 0.05
    gain = 1.02
    for val in raw_values:
        corrected = (val + offset) * gain
        if corrected > 100:
            corrected = 98.5  # artificial cap
        calibrated.append(corrected)
    return calibrated

# Irrelevant calibration helper (dead function - red herring)
def legacy_calibrate(x):
    return x * 0.97 + 3.2

# Unused sensor weighting matrix (distractor data)
weight_matrix = [
    [1.1, 0.9],
    [0.8, 1.2]
]

# Simulated raw sensor readings
raw_sensor_data = [89.3, 92.1, 87.4, 95.6, 83.2, 90.8, 94.0, 86.7]

# Apply main calibration
calibrated_readings = sensor_calibration(raw_sensor_data)

# Secondary processing with distractors
temp_buffer = []
dropout_indices = []
for i, val in enumerate(calibrated_readings):
    if val < 88.0:
        dropout_indices.append(i)
    temp_buffer.append(val * 1.001)  # minor adjustment (not used later)

# Real processing path
processed_data = []
smoothing_factor = 0.85
prev = 0
for i, val in enumerate(calibrated_readings):
    if i == 0:
        processed_data.append(val)
        prev = val
    else:
        filtered = smoothing_factor * prev + (1 - smoothing_factor) * val
        processed_data.append(filtered)
        prev = filtered

# Decoy statistical analysis (never called)
def compute_entropy(data):
    from math import log
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    total = len(data)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p)
    return entropy

# Threshold logic with string-based mode switch (irrelevant mode check)
operation_mode = "diagnostic"
threshold = 90.0 if "debug" in operation_mode else 89.5

# Simulate fault detection flags (some are decoys)
fault_flags = {
    'overheat': False,
    'no_signal': len(dropout_indices) > 3,
    'drift': True  # always set (misleading)
}

# Main diagnostic analyzer
def analyze_readings(readings, thresh):
    count_above = 0
    cumulative = 0.0
    peak = float('-inf')
    for reading in readings:
        if reading > thresh:
            count_above += 1
        cumulative += reading
        if reading > peak:
            peak = reading
    
    # Use conditional expression and string method as required
    adjustment = 1.05 if 'DIAGNOSTIC'.lower() in operation_mode.upper() else 1.0
    
    # This intermediate result is misleading
    fake_score = (count_above * 100) / len(readings) if len(readings) > 0 else 0
    
    # Actual answer computation (non-obvious)
    base_metric = cumulative / len(readings)
    final_value = (base_metric + peak) * adjustment
    
    # Dead code branch (never executes due to fixed mode)
    if operation_mode == "test_sim":
        final_value *= 0.9
    
    return final_value

# Critical execution point
final_diagnostic = analyze_readings(processed_data, threshold)

# Output the target result
print(f"Target result: {final_diagnostic}")