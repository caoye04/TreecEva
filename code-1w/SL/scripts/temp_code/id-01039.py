import math

# Simulated sensor array data with noise and calibration factors
def fetch_sensor_data():
    raw_values = [127, 255, 64, 192, 32]
    calibration_map = {0: 1.05, 1: 0.98, 2: 1.02, 3: 0.99, 4: 1.01}
    return [(val * calibration_map[i]) for i, val in enumerate(raw_values)]

# Irrelevant auxiliary function – dead code path (distractor)
def deprecated_normalization(data):
    max_val = max(data)
    return [x / max_val for x in data] if max_val > 0 else data

# Signal processing pipeline
def denoise_signal(signal):
    filtered = []
    for i in range(len(signal)):
        left = signal[i-1] if i > 0 else signal[0]
        mid = signal[i]
        right = signal[i+1] if i < len(signal)-1 else signal[-1]
        smoothed = (left + mid + right) / 3
        filtered.append(smoothed)
    return filtered

# Bitmask-based anomaly detection (used later)
def detect_anomalies(readings):
    flags = 0
    for r in readings:
        if r > 150:
            flags |= 1 << 1
        if r < 50:
            flags ^= 1 << 3
        if 100 <= r <= 120:
            flags &= ~(1 << 2)
    return flags

# Data transformation stage
def extract_features(cleaned):
    avg = sum(cleaned) / len(cleaned)
    variance = sum((x - avg) ** 2 for x in cleaned) / len(cleaned)
    peak = max(cleaned)
    # Decoy intermediate calculation (irrelevant)
    dummy_score = (avg * 0.7) + (peak * 0.3)
    feature_vector = (avg, math.sqrt(variance), peak)
    return feature_vector

# Higher-level analysis with logical branching
def classify_state(features):
    mean_val, std_dev, p = features
    condition = None
    if mean_val > 100:
        if std_dev < 15:
            condition = 3  # Stable high
        else:
            condition = 5  # Fluctuating high
    elif mean_val < 70:
        if p > 140:
            condition = 4  # Critical spike
        else:
            condition = 2  # Low baseline
    else:
        condition = 1  # Normal
    # Dead branch – never reached due to logic above (misleading)
    if mean_val == 88.8:
        condition = 999
    return condition

# Composite diagnostic engine
def analyze_readings(sensors):
    # Step 1: Denoise
    clean_data = denoise_signal(sensors)
    
    # Step 2: Feature extraction
    features = extract_features(clean_data)
    
    # Step 3: State classification
    state_code = classify_state(features)
    
    # Step 4: Anomaly bitmask
    anomalies = detect_anomalies(clean_data)
    
    # Step 5: Apply corrective weight based on anomaly pattern
    correction = 1.0
    if anomalies & (1 << 1):
        correction -= 0.05
    if anomalies & (1 << 3):
        correction += 0.02
    adjusted_state = state_code * correction
    
    # Step 6: Final mapping through nonlinear transform
    final_diagnostic = int((adjusted_state ** 2) * 1.75)
    
    # Irrelevant logging (distractor)
    log_entry = {
        'raw_sum': sum(sensors),
        'timestamp': '2023-11-05',
        'version': '2.1.0',
        'diagnostic_raw': adjusted_state,
        'unused_flag': False
    }
    
    # Red herring computation (no effect)
    temp_result = [math.sin(x / 10) for x in clean_data]
    aggregate_index = sum(temp_result) * 100
    
    return final_diagnostic

# Unused legacy function (distractor)
def legacy_diagnostic(seq):
    return sum(x * (i+1) for i, x in enumerate(seq)) % 100

# Main execution flow
if __name__ == '__main__':
    # Fetch and preprocess sensor inputs
    raw_signals = fetch_sensor_data()
    processed_signals = [max(min(x, 255), 0) for x in raw_signals]  # Clamp to 8-bit
    
    # Spurious intermediate check (dead logic)
    if len(processed_signals) >= 4:
        subset_avg = sum(processed_signals[:4]) / 4
        if subset_avg > 200:
            processed_signals[0] *= 0.9
    
    # Core analysis
    final_diagnostic = analyze_readings(processed_signals)
    
    # Output target result
    print(f"Target result: {final_diagnostic}")