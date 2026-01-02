import itertools

# Simulated sensor data processing for wind turbine diagnostics
def preprocess_readings(raw_readings):
    filtered = [x for x in raw_readings if -100 <= x <= 100]
    baseline_offset = 23.7
    adjusted = [round(x - baseline_offset, 3) for x in filtered]
    return adjusted

# Irrelevant auxiliary function - dead code path
def calculate_efficiency_curve(values):
    total = 0
    for i in range(len(values)):
        total += values[i] * (i % 7 + 1)
    efficiency_score = total / (len(values) + 1e-5)
    return efficiency_score

# Misleading transformation with decoy logic
def apply_calibration_noise(data, factor=0.987):
    calibrated = []
    for val in data:
        if val > 10:
            calibrated.append(val * factor + 1.5)
        elif val < -10:
            calibrated.append(val * factor - 0.8)
        else:
            calibrated.append(val * factor)  # Neutral zone
    return calibrated

# Core diagnostic aggregation
def detect_anomalies(signal_stream, threshold_config):
    anomalies = []
    moving_avg = 0
    count = 0
    for val in signal_stream:
        moving_avg = (moving_avg * count + val) / (count + 1) if count > 0 else val
        count += 1
        
        # Real condition: detect significant deviations
        if abs(val - moving_avg) > threshold_config['deviation_limit']:
            anomalies.append(val)
    
    return anomalies

# Red herring function using itertools - appears relevant but unused in final path
def generate_synthetic_peaks(base_values, intensity=3):
    peak_candidates = []
    for combo in itertools.combinations_with_replacement(base_values, 2):
        peak_candidates.append((combo[0] + combo[1]) * intensity)
    return [p for p in peak_candidates if p > 50]

# Real metric aggregator used in final computation
def aggregate_metrics(dataset, config):
    prep_data = preprocess_readings(dataset)
    
    # Decoy intermediate variables
    temp_analysis_1 = [x ** 2 for x in prep_data if x > 5]
    temp_analysis_2 = sum(1 for x in prep_data if x < -5)
    
    # Apply actual but disguised core logic
    anomaly_list = detect_anomalies(prep_data, config)
    
    # Critical distractor: complex-looking but unused calculation
    shadow_metric = 0
    window_size = 4
    for i in range(len(prep_data) - window_size + 1):
        window = prep_data[i:i+window_size]
        diff_pair = [(window[j+1] - window[j]) for j in range(len(window)-1)]
        if len(diff_pair) > 0:
            avg_diff = sum(diff_pair) / len(diff_pair)
            if avg_diff > 2.1:
                shadow_metric += 1
    
    # Another red herring: tuple unpacking with irrelevant results
    summary_stats = (sum(prep_data), len(prep_data), len(anomaly_list))
    base_total, _, _ = summary_stats
    
    # Real final computation - well hidden among noise
    contribution = 0
    for a in anomaly_list:
        if a > 0:
            contribution += int(a // 3)
        else:
            contribution -= int(abs(a) // 4)
    
    # Final result derived from non-obvious combination
    final_diagnostic = base_total + contribution + len(anomaly_list)
    
    # Only this line matters for output
    return final_diagnostic

# Setup realistic input data
raw_sensor_input = [85, -12, 43, 67, 15, -88, 23, 91, 11, -44, 37, 76, -9, 52, 103, -205, 61]

# Threshold configuration with meaningful parameters
thresholds = {
    'deviation_limit': 35.0,
    'sensitivity_boost': False
}

# Execute main pipeline
turbine_data = [x for x in raw_sensor_input if x != -205]  # Remove invalid reading

# Key statement that produces the target variable
diag_base = preprocess_readings(turbine_data)
calib_diag = apply_calibration_noise(diag_base)
synthetic_enhancements = generate_synthetic_peaks([1, 2, 3])
final_diagnostic = aggregate_metrics(turbine_data, thresholds)

print(f"Result: {final_diagnostic}")