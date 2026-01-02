import math

# Simulated sensor fusion module for autonomous drone navigation

def preprocess_signals(raw_readings):
    filtered = [x for x in raw_readings if -100 < x < 100]
    baseline = sum(filtered) / len(filtered)
    normalized = [x - baseline for x in filtered]
    return normalized


def extract_features(series):
    magnitude = sum([abs(x) for x in series])
    variance = sum([(x - sum(series)/len(series))**2 for x in series]) / len(series)
    peaks = [i for i in range(1, len(series)-1) if series[i] > series[i-1] and series[i] > series[i+1]]
    peak_count = len(peaks)
    # Irrelevant transformation (distractor)
    dummy_transform = [math.sin(math.radians(x)) for x in series[::3]]
    return {'magnitude': magnitude, 'variance': variance, 'peaks': peak_count}


def evaluate_stability(metrics):
    mag = metrics['magnitude']
    var = metrics['variance']
    pks = metrics['peaks']
    score = (mag * 0.3) + (var * 0.5) - (pks * 2)
    # Misleading intermediate result (dead path)
    if score > 100:
        return 999  # Never reached due to data scale
    return score


def generate_timed_sequence(base, interval_ms, count):
    sequence = []
    t = 0
    for _ in range(count):
        sequence.append(base + math.sin(math.radians(t)))
        t += interval_ms
    return sequence


def slice_and_window(data, window_size, step=1):
    windows = []
    for i in range(0, len(data) - window_size + 1, step):
        windows.append(data[i:i+window_size])
    # Distractor: unused complex slicing pattern
    edge_cases = data[::2][1::3][-5:] if len(data) > 10 else []
    return windows


def detect_anomalies(windows):
    anomalies = []
    for window in windows:
        mean_val = sum(window) / len(window)
        deviance = sum([abs(x - mean_val) for x in window])
        if deviance > 15:
            anomalies.append(mean_val)
    # Decoy logic with plausible but unused output
    if len(anomalies) > 5:
        return [-1] * len(anomalies)
    return anomalies


def aggregate_metrics(time_series, flag_set):
    # Critical operation: compute diagnostic code based on control flow
    base_code = 0
    if flag_set['calibrated']:
        base_code += 100
    if flag_set['synced'] and not flag_set['legacy_mode']:
        base_code += 205
    if flag_set['encrypted']:
        base_code -= 50
    
    # Real computation path
    processed = preprocess_signals(time_series)
    features = extract_features(processed)
    stability = evaluate_stability(features)
    
    # Red herring: elaborate but unused anomaly detection chain
    windows = slice_and_window(processed, 6, 2)
    alerts = detect_anomalies(windows)
    alert_penalty = len(alerts) * 10
    
    # Meaningful distractor: complex bit manipulation with no effect
    temp_flag = (flag_set['calibrated'] << 3) ^ 7
    temp_flag = (temp_flag | 0b1010) & 0b1111
    
    # Final aggregation uses only stability and base_code
    final_score = int(round(base_code + stability))
    
    # Dead code branch (never executed due to logic)
    if alert_penalty < 0:
        final_score = -9999
        
    return final_score

# Main execution flow
if __name__ == "__main__":
    # Simulated telemetry input
    raw_sensor_data = [95, -12, 43, 88, -5, 37, 92, -8, 41, 85, -3, 39, 94, -10, 42]
    
    # Configuration flags (some relevant, some distracting)
    system_flags = {
        'calibrated': True,
        'synced': True,
        'encrypted': False,
        'debug_mode': True,
        'legacy_mode': False,
        'verbose_logging': True
    }
    
    # Generate extended timing sequence
    timing_base = 50
    timing_interval = 15
    sample_count = 12
    timing_data = generate_timed_sequence(timing_base, timing_interval, sample_count)
    
    # Apply signal processing pipeline
    cleaned = preprocess_signals(raw_sensor_data)
    
    # Extract feature set (used downstream)
    extracted_features = extract_features(cleaned)
    
    # Perform windowing analysis (partially irrelevant)
    segments = slice_and_window(cleaned, 5)
    
    # Compute diagnostic metric
    final_diagnostic = aggregate_metrics(timing_data, system_flags)
    
    # Output target result
    print(f"Result: {final_diagnostic}")