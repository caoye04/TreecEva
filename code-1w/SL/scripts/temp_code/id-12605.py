import math

# Sensor simulation and analysis system for environmental monitoring

def generate_synthetic_data(base, count):
    return [base * (1.05 ** i) + (i % 7) for i in range(count)]

def apply_calibration(readings, factor=1.02, offset=0.5):
    calibrated = []
    for val in readings:
        adjusted = val * factor + offset
        if adjusted > 30:
            adjusted -= 5
        calibrated.append(round(adjusted, 3))
    return calibrated

def filter_outliers(data, threshold=2.5):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    filtered = [x for x in data if abs(x - mean_val) / std_dev <= threshold]
    return filtered

def compute_entropy(values):
    total = sum(values)
    probabilities = [(v / total) for v in values if v > 0]
    entropy = -sum(p * math.log(p) for p in probabilities)
    return round(entropy, 4)

def rolling_average(series, window=3):
    if len(series) < window:
        return series[:]
    averages = []
    for i in range(len(series) - window + 1):
        averages.append(sum(series[i:i+window]) / window)
    return [round(x, 3) for x in averages]

def detect_anomalies(pattern):
    anomalies = []
    for i in range(1, len(pattern)):
        if pattern[i] - pattern[i-1] > 8:
            anomalies.append(i)
    return anomalies or [0]

def phase_shift_analysis(data):
    shifted = [data[-i] for i in range(1, min(6, len(data)+1))]
    return {f'delay_{i}': shifted[i] * 0.87 for i in range(len(shifted))}

def temporal_weighting(sequence):
    n = len(sequence)
    weights = [math.exp(-i/10) for i in range(n)]
    weighted_sum = sum(sequence[i] * weights[i] for i in range(n))
    return round(weighted_sum, 3)

def transform_magnitude(raw):
    magnitude = [abs(math.sin(x/10)) * 100 for x in raw]
    normalized = [m / max(magnitude) for m in magnitude]
    return normalized

def frequency_domain_approx(data):
    # Simulated frequency domain features
    feature_set = {}
    for idx, val in enumerate(data[:5]):
        feature_set[f'freq_component_{idx}'] = round(val * (idx+1) % 3.14, 3)
    return feature_set

def integrate_multi_source(primary, secondary):
    combined = []
    for i in range(min(len(primary), len(secondary))):
        fusion = primary[i] * 0.7 + secondary[i] * 0.3
        combined.append(round(fusion, 3))
    return combined

def calculate_stability_index(seq):
    diffs = [abs(seq[i+1] - seq[i]) for i in range(len(seq)-1)]
    stability = 100 / (1 + sum(diffs)/len(diffs))
    return int(stability)

def analyze_readings(metrics):
    entropy_score = compute_entropy(metrics)
    time_weight = temporal_weighting(metrics)
    stability = calculate_stability_index(metrics)
    peak = max(metrics)
    
    # Irrelevant transformations (distractors)
    dummy_transform = [math.cos(x/5) for x in metrics]
    shadow_map = {i: math.tan(v/10) for i, v in enumerate(metrics) if i % 3 == 0}
    decoy_aggregate = sum(math.asin(min(1, v/100)) for v in dummy_transform[:4])
    
    # Critical calculation path
    base_score = (entropy_score * 10) + (time_weight / 2) + stability
    adjustment_factor = 0.9 if len(metrics) > 10 else 1.1
    refined_score = base_score * adjustment_factor
    
    # More red herrings
    debug_snapshot = {
        'timestamp': 1678886400,
        'node_id': 'DBG-X9A',
        'buffer_state': [0.1, 0.2, 0.15],
        'checksum': 0xDEADBEEF
    }
    
    # Final diagnostic computation (answer depends only on this)
    final_diagnostic = int(refined_score - 50)  # Key result
    
    # Dead code path (never executed but looks important)
    if False:
        recovery_mode = True
        fallback_diagnostic = sum(int(b) for b in format(hash(str(metrics)), 'b')[-8:])
        final_diagnostic = fallback_diagnostic
    
    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    # Generate initial sensor readings
    raw_sensor_data = generate_synthetic_data(base=12.5, count=18)
    
    # Apply calibration (irrelevant precision adjustments)
    calibrated_readings = apply_calibration(raw_sensor_data, factor=1.03)
    
    # Filter outliers (modifies data meaningfully)
    cleaned_data = filter_outliers(calibrated_readings)
    
    # Compute rolling trends (used later)
    trend_data = rolling_average(cleaned_data, window=4)
    
    # Transform magnitude space (distractor)
    magnitude_profile = transform_magnitude(trend_data)
    
    # Phase shift analysis (completely irrelevant)
    phase_features = phase_shift_analysis(trend_data)
    
    # Frequency domain approximation (red herring)
    freq_features = frequency_domain_approx(magnitude_profile)
    
    # Simulate secondary sensor source (unused but plausible)
    auxiliary_stream = generate_synthetic_data(base=8.2, count=len(trend_data))
    merged_input = integrate_multi_source(trend_data, auxiliary_stream)
    
    # Detect anomalies (result not used)
    anomaly_positions = detect_anomalies(merged_input)
    
    # Apply final processing to get target variable
    processed_metrics = [round(x * 1.08, 3) for x in merged_input]
    
    # Core diagnostic analysis
    final_diagnostic = analyze_readings(processed_metrics)
    
    # Output the required result
    print(f"Result: {final_diagnostic}")