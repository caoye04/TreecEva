import itertools

# Simulated sensor data processing pipeline for autonomous drone navigation
raw_readings = [0.88, 0.91, 0.76, 0.85, 0.99, 0.64, 0.55, 0.77]
external_noise = [0.1, -0.05, 0.2, -0.15, 0.08, 0.11, -0.03, 0.07]
baseline_offset = 0.12

def apply_calibration(data, offset):
    """Apply baseline calibration to sensor data."""
    return [x + offset for x in data]

def filter_outliers(seq, threshold=0.75):
    """Remove values below threshold (simulated noise filtering)."""
    filtered = [x for x in seq if x >= threshold]
    # Distractor: unused computation
    stats_summary = {'count': len(filtered), 'sum': sum(filtered)}
    return filtered

def compute_rolling_average(values, window=3):
    """Compute rolling average over a window."""
    if len(values) < window:
        return [0.0]
    averages = []
    for i in range(len(values) - window + 1):
        averages.append(sum(values[i:i+window]) / window)
    return averages

def detect_anomalies(series):
    """Detect sudden drops in data sequence."""
    anomalies = 0
    for i in range(1, len(series)):
        if series[i] < series[i-1] * 0.85:  # 15% drop threshold
            anomalies += 1
    return anomalies

def generate_pairs(data):
    """Generate overlapping pairs for correlation analysis (unused distractor)."""
    return list(itertools.combinations(data, 2))

def calculate_entropy(data):
    """Calculate Shannon entropy of normalized distribution (red herring)."""
    from math import log2
    total = sum(data)
    if total == 0:
        return 0.0
    probs = [x / total for x in data]
    return -sum(p * log2(p) for p in probs if p > 0)

def adjust_for_environment(metrics_dict, factor=1.05):
    """Slightly boost all metrics due to environmental calibration."""
    adjusted = {}
    for k, v in metrics_dict.items():
        adjusted[k] = v * factor
        # Decoy logic
        if v < 0.8:
            adjusted[k] += 0.02
    return adjusted

def validate_integrity(check_sequence):
    """Verify data integrity using XOR checksum (distractor function)."""
    checksum = 0
    for val in check_sequence:
        checksum ^= int(val * 100)
    return checksum % 17

# Main processing workflow
calibrated_data = apply_calibration(raw_readings, baseline_offset)
noise_filtered = filter_outliers(calibrated_data, threshold=0.78)

# Dead code path — never used
expanded_grid = [x * 1.03 for x in calibrated_data if x > 0.8]
decoy_pairs = generate_pairs(noise_filtered[:4])

# Compute time-series characteristics
rolling_avgs = compute_rolling_average(noise_filtered)
anomaly_count = detect_anomalies(noise_filtered)

# Simulate multi-metric evaluation
metric_pool = {
    'stability': rolling_avgs[0] if len(rolling_avgs) > 0 else 0.0,
    'consistency': len(noise_filtered) / len(raw_readings),
    'response_time': 0.88,
    'signal_strength': sum(noise_filtered) / len(noise_filtered),
    'drop_rate': anomaly_count / len(noise_filtered) if noise_filtered else 0
}

# Distractor: irrelevant entropy calculation
entropy_value = calculate_entropy(noise_filtered)
integrity_flag = validate_integrity([int(x*100) for x in raw_readings])

# Adjust weights based on environmental feedback (partially unused)
environment_factor = 1.05 if anomaly_count < 2 else 0.98
adjusted_metrics = adjust_for_environment(metric_pool, environment_factor)

# Weight assignment — only some weights affect final outcome
weights = {
    'stability': 0.25,
    'consistency': 0.20,
    'response_time': 0.15,
    'signal_strength': 0.30,
    'drop_rate': 0.10  # Inverted later
}

# Critical inversion: drop rate is negative impact
adjusted_metrics['drop_rate'] = 1 - adjusted_metrics['drop_rate']

# Final weighted score computation
final_score = 0
for key in weights:
    if key in adjusted_metrics:
        final_score += adjusted_metrics[key] * weights[key]

# Output result as required
print(f"Target result: {final_score}")