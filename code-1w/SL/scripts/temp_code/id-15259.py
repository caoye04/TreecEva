import math

# Sensor calibration constants (used in decoy functions)
CALIBRATION_OFFSET = 0.87
NOISE_FLOOR = 0.05
TEMPERATURE_BIAS = -0.12

# Irrelevant sensor types for distraction
SENSOR_TYPES = ['humidity', 'pressure', 'light', 'uv', 'proximity']
ACTIVE_SENSORS = {s: True for s in SENSOR_TYPES}

# Simulated raw readings from environmental sensors
raw_readings = [
    [3.2, 1.8, 4.5, 2.1, 0.9],
    [2.9, 2.0, 4.1, 2.3, 1.2],
    [3.5, 1.6, 4.8, 1.9, 0.7],
    [3.1, 1.9, 4.3, 2.2, 1.0]
]

# Mapping of expected baseline values per channel
baseline_profile = {
    'channel_0': 3.0,
    'channel_1': 2.0,
    'channel_2': 4.0,
    'channel_3': 2.0,
    'channel_4': 1.0
}

# Threshold configuration for anomaly detection (ACTUALLY USED)
threshold_map = {
    'high': 1.3 * baseline_profile['channel_2'],
    'low': 0.7 * baseline_profile['channel_1'],
    'critical_delta': 0.25
}

# Decoy function - looks important but unused
def calibrate_sensor(data, offset=CALIBRATION_OFFSET):
    return [[max(0, sample + offset) for sample in row] for row in data]

# Another red herring - processes irrelevant sensor types
def activate_redundant_sensors(sensor_list):
    status_log = []
    for sensor in sensor_list:
        if sensor == 'uv':
            status_log.append(f'{sensor}: recalibrating')
        else:
            status_log.append(f'{sensor}: nominal')
    return status_log

# Misleading transformation that is never called
def compute_fourier_components(signal_stream):
    fft_magnitude = []
    for seq in signal_stream:
        transformed = [math.sin(x * math.pi / 2) for x in seq]
        magnitude = sum([abs(t) for t in transformed]) / len(transformed)
        fft_magnitude.append(magnitude)
    return fft_magnitude

# Data normalization function with distractor logic
def normalize_and_filter(readings, baseline=baseline_profile):
    normalized = []
    anomalies_detected = 0
    
    # Real processing begins here
    keys = sorted(baseline.keys())
    for i, reading_row in enumerate(readings):
        norm_row = []
        for j, val in enumerate(reading_row):
            key = keys[j]
            expected = baseline[key]
            deviation = abs(val - expected)
            
            # Actual relevant computation
            adjusted = val / expected if expected else val
            
            # Introduce dead condition (never triggers)
            if deviation > 5.0:  # Impossible threshold
                anomalies_detected += 1
                adjusted = 0.0
            
            norm_row.append(adjusted)
        
        normalized.append(norm_row)
    
    # Dead code path - result unused
    if anomalies_detected > 0:
        print(f'Warning: {anomalies_detected} extreme deviations')
    
    return normalized

# Core analysis function with nested logic
def analyze_readings(data, thresholds):
    high_threshold = thresholds['high']
    low_threshold = thresholds['low']
    delta_limit = thresholds['critical_delta']
    
    # Accumulators (some used, some not)
    spike_count = 0
    stability_score = 0.0
    cumulative_drift = 0.0
    segment_analysis = []
    
    # Real diagnostic variable
    diagnostic_weight = 100.0
    
    for idx, segment in enumerate(data):
        # Extract specific elements for evaluation
        primary_signal = segment[2]  # channel_2 derived
        secondary_signal = segment[1]  # channel_1 derived
        
        # Meaningful conditional branch
        if primary_signal > high_threshold:
            spike_count += 1
            diagnostic_weight *= 0.9
        elif primary_signal < (high_threshold * 0.92):
            diagnostic_weight *= 1.05

        # Another evaluation path
        if secondary_signal < low_threshold:
            stability_score -= 5.0
        
        # Compute moving delta (only last value matters)
        if idx > 0:
            prev_primary = data[idx-1][2]
            current_delta = abs(primary_signal - prev_primary)
            cumulative_drift += current_delta
            
            if current_delta > delta_limit:
                stability_score -= 2.5
            else:
                stability_score += 1.0
        
        # Unused list accumulation for distraction
        segment_analysis.append({
            'index': idx,
            'spike_risk': 'high' if primary_signal > high_threshold else 'normal',
            'drift_observed': cumulative_drift
        })
    
    # Final computation - only this matters
    adjustment_factor = 1 + (stability_score / 100)
    diagnostic_weight *= adjustment_factor
    
    # Dead code - prints but doesn't affect result
    if len(segment_analysis) > 2:
        critical_segments = [s for s in segment_analysis if s['spike_risk'] == 'high']
    
    return int(diagnostic_weight)  # deterministic integer output

# Irrelevant preprocessing step (looks important)
activation_log = activate_redundant_sensors(SENSOR_TYPES)

# Real data flow starts here
processed_data = normalize_and_filter(raw_readings)

# Key execution point
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Output result as required
print(f"Result: {final_diagnostic}")