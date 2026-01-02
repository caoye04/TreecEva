import itertools

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.6, 26.7, 24.3, 23.9, 25.1]
humidity_readings = [45, 48, 50, 55, 60, 53, 49, 51]
pressure_readings = [1013, 1015, 1012, 1009, 1008, 1010, 1014, 1016]

# Irrelevant auxiliary metrics (distractor variables)
sound_levels = [32, 35, 40, 38, 36, 34, 33, 41]  # Decoy sensor data
light_intensity = [800, 780, 810, 790, 805, 815, 795, 785]  # Unused in logic

# Preprocessing: Normalize readings using sliding window average (not used in final path)
def smooth_signal(signal):
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - 2)
        end = min(len(signal), i + 3)
        smoothed.append(sum(signal[start:end]) / (end - start))
    return smoothed

# Misleading diagnostic function (dead code path)
def analyze_trend(data_stream):
    increasing = sum(1 for a, b in zip(data_stream, data_stream[1:]) if b > a)
    decreasing = sum(1 for a, b in zip(data_stream, data_stream[1:]) if b < a)
    return 'upward' if increasing > decreasing else 'downward'

# Unused transformation chain (distractor)
transformed_humidity = [h * 1.02 for h in humidity_readings if h > 47]
decimated_pressure = [p for i, p in enumerate(pressure_readings) if i % 2 == 0]

# Key computation: detect anomalies above threshold
anomaly_flags = []
for temp in temperature_readings:
    if temp > 25.0:
        anomaly_flags.append(1)
    else:
        anomaly_flags.append(0)

# Extract indices of anomalous readings
anomaly_indices = [i for i, flag in enumerate(anomaly_flags) if flag == 1]

# Filter valid data windows using overlapping criteria (complex filtering)
valid_windows = []
for i in range(len(temperature_readings) - 2):
    temp_window = temperature_readings[i:i+3]
    humidity_window = humidity_readings[i:i+3]
    if all(t < 26.0 for t in temp_window) and any(h > 50 for h in humidity_window):
        valid_windows.append(i)

# Real processing begins here — critical path
filtered_data = [temperature_readings[i] for i in anomaly_indices if i in valid_windows]

def apply_offset(values, base_offset):
    return [v + base_offset for v in values]

def calculate_entropy(values):
    from math import log
    total = sum(values)
    if total == 0:
        return 0.0
    probabilities = [v / total for v in values]
    return -sum(p * log(p) for p in probabilities if p > 0)

# Complex multi-step calibration logic
baseline = 0.87
adjustment_curve = [round(baseline * (1.05 ** i), 3) for i in range(10)]
calibration_factor = adjustment_curve[len(filtered_data) % 6] if filtered_data else 0.92

# Red herring: advanced signal fusion (never called)
def fuse_modalities(temps, humids, press):
    combined = []
    for t, h, p in zip(temps, humids, press):
        score = t * (h / 100) + (p - 1000) * 0.3
        combined.append(round(score, 2))
    return combined

def process_readings(readings, calib):
    if not readings:
        return -999.0
    
    # Step 1: Apply calibration offset
    calibrated = apply_offset(readings, calib)
    
    # Step 2: Pair with synthetic reference using itertools
    reference_template = [22.0, 24.5, 27.0]
    pairs = list(itertools.zip_longest(calibrated, reference_template, fillvalue=25.0))
    
    # Step 3: Compute deviation-adjusted mean
    deviations = [(a - b) ** 2 for a, b in pairs]
    mse = sum(deviations) / len(deviations)
    
    # Step 4: Use conditional expression to determine output mode
    result = mse if len(calibrated) > 1 else (calibrated[0] if calibrated else 0)
    
    # Step 5: Final transformation based on entropy side-channel
    entropy_value = calculate_entropy([len(calibrated), len(pairs), int(sum(calibrated))])
    final_result = result * (1 + entropy_value * 0.1)
    
    return round(final_result, 4)

# Dead code: unused aggregation pattern (misleading)
aggregation_modes = {'avg': True, 'median': False, 'rms': True}
selected_mode = next((k for k, v in aggregation_modes.items() if v), 'avg')

# Trigger point: this is where the answer is computed
temp_snapshot = temperature_readings[::2]
reference_diagnostic = sum(temp_snapshot) / len(temp_snapshot)

final_diagnostic = process_readings(filtered_data, calibration_factor)

# Output the target result
print(f"Target result: {final_diagnostic}")