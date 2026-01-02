import math

# Sensor simulation and diagnostic analysis system
def generate_raw_readings():
    return [i * 1.5 + math.sin(i) for i in range(15)]

def filter_outliers(data, limit=100):
    # Irrelevant filtering (never actually applied)
    return [x for x in data if abs(x) < limit]

def normalize readings(data):
    max_val = max(data)
    return [round(x / max_val, 4) for x in data]

def calculate_entropy(data):
    # Dead function - not used in main logic
    total = sum(data)
    probs = [x / total for x in data if x > 0]
    return -sum(p * math.log2(p) for p in probs)

def rolling_window(data, size=3):
    windows = []
    for i in range(len(data) - size + 1):
        windows.append(data[i:i+size])
    return windows

def detect_anomalies(series):
    anomalies = []
    for i in range(1, len(series)):
        if abs(series[i] - series[i-1]) > 0.8:
            anomalies.append(i)
    return anomalies if anomalies else [0]

def transform_data(seq, key=lambda x: x ** 2):
    # Misleading transformation path
    return [key(x) + 0.1 for x in seq]

def evaluate_stability(metric):
    # Unused stability check
    return "stable" if metric < 0.5 else "unstable"

def build_lookup_table(keys, values):
    # Distractor: builds unused mapping
    return dict(zip(keys, values))

def main_processing_pipeline(raw):
    # Step 1: Normalize raw sensor input
    normalized = normalize_readings(raw)
    
    # Step 2: Apply sliding window analysis (relevant)
    windows = rolling_window(normalized, 3)
    
    # Step 3: Compute moving averages (red herring)
    moving_averages = [sum(window)/len(window) for window in windows]
    
    # Step 4: Detect jumps in signal (used later)
    anomaly_indices = detect_anomalies(normalized)
    
    # Step 5: Create masked sequence using anomaly positions (critical)
    masked_data = []
    for i, val in enumerate(normalized):
        if i in anomaly_indices:
            masked_data.append(val * 1.2)
        else:
            masked_data.append(val * 0.95)
    
    # Step 6: Compute weighted integral (relevant calculation)
    weights = [math.exp(-i*0.1) for i in range(len(masked_data))]
    weighted_sum = sum(masked_data[i] * weights[i] for i in range(len(masked_data)))
    
    # Step 7: Simulate calibration offset (distractor)
    baseline_offset = sum(normalized[:5]) / 5
    adjusted_sum = weighted_sum - baseline_offset
    
    # Step 8: Generate feature vector with tuple packing (intermediate)
    features = [(i, masked_data[i], weights[i]) for i in range(0, len(masked_data), 2)]
    feature_magnitudes = [math.sqrt(idx**2 + val**2) for idx, val, _ in features]
    
    # Step 9: Compute final processed score (ACTUALLY USED)
    processed_score = sum(feature_magnitudes) / (weighted_sum + 1e-8)
    
    return {
        'data': masked_data,
        'score': processed_score,
        'anomalies': anomaly_indices,
        'weights': weights,
        'features': features
    }

def analyze_readings(diagnostic_set, threshold_fn):
    score = diagnostic_set['score']
    data_len = len(diagnostic_set['data'])
    anomaly_count = len(diagnostic_set['anomalies'])
    
    # Complex conditional logic with short-circuiting
    if data_len == 0:
        return -1
    elif threshold_fn(score) and anomaly_count > 0:
        adjustment = (anomaly_count / data_len) * 100
        if adjustment > 50:
            return int(score * 1234)
        else:
            return int(score * 2468)
    else:
        fallback = 0
        for x in diagnostic_set['weights']:
            if x > 0.5:
                fallback += int(x * 100)
        return fallback % 999

def main():
    # Generate initial sensor data
    raw_sensor_data = generate_raw_readings()
    
    # Unused entropy calculation (misleading)
    entropy_metric = calculate_entropy(raw_sensor_data)
    stability_status = evaluate_stability(entropy_metric)
    
    # Build irrelevant lookup table
    indices = list(range(len(raw_sensor_data)))
    labels = [f"sensor_{i}" for i in range(len(raw_sensor_data))]
    lookup = build_lookup_table(indices, labels)
    
    # Transform through unused path
    dummy_transform = transform_data(raw_sensor_data, lambda x: x ** 0.5)
    
    # Core processing pipeline
    processed_data = main_processing_pipeline(raw_sensor_data)
    
    # Define dynamic threshold function (critical)
    threshold_func = lambda s: s > 3.14
    
    # Final diagnostic decision point
    final_diagnostic = analyze_readings(processed_data, threshold_func)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()