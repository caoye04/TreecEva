import math

# Sensor simulation and diagnostic analysis system
def generate_signals(baseline, noise_factor, count):
    """Generate synthetic sensor signals with controlled noise (irrelevant function)"""
    return [baseline + noise_factor * math.sin(i) for i in range(count)]


def normalize_readings(readings):
    """Normalize readings using min-max scaling"""
    if not readings:
        return []
    min_val, max_val = min(readings), max(readings)
    if min_val == max_val:
        return [0.5] * len(readings)
    return [(x - min_val) / (max_val - min_val) for x in readings]


def filter_outliers(data, limit=3.0):
    """Remove outliers based on z-score (partially relevant but overkill)"""
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    if std_dev == 0:
        return data
    return [x for x in data if abs((x - mean_val) / std_dev) <= limit]


def compute_entropy(values):
    """Compute Shannon entropy of a distribution (red herring)"""
    from collections import Counter
    counts = Counter(values)
    total = len(values)
    probabilities = [count / total for count in counts.values()]
    return -sum(p * math.log2(p) for p in probabilities if p > 0)


def extract_features(signal_stream):
    """Extract various statistical features (mostly irrelevant)"""
    features = {}
    features['mean'] = sum(signal_stream) / len(signal_stream)
    features['variance'] = sum((x - features['mean'])**2 for x in signal_stream) / len(signal_stream)
    features['skew'] = sum(((x - features['mean'])/features['variance']**0.5)**3 for x in signal_stream) / len(signal_stream)
    features['kurtosis'] = sum(((x - features['mean'])/features['variance']**0.5)**4 for x in signal_stream) / len(signal_stream) - 3
    features['peak_to_peak'] = max(signal_stream) - min(signal_stream)
    return features


def map_severity(code):
    """Map numeric code to severity level (decoy logic)"""
    severity_map = {1: 'Critical', 2: 'High', 3: 'Medium', 4: 'Low'}
    return severity_map.get(code, 'Unknown')


def detect_anomalies(windowed_data, sensitivity=0.1):
    """Detect anomalies using rolling standard deviation (distractor path)"""
    anomalies = []
    window_size = 5
    for i in range(len(windowed_data) - window_size + 1):
        window = windowed_data[i:i+window_size]
        mean_win = sum(window) / window_size
        std_win = (sum((x - mean_win)**2 for x in window) / window_size)**0.5
        if std_win > sensitivity * mean_win and mean_win > 0:
            anomalies.append(i + window_size // 2)
    return list(set(anomalies))


def process_readings(raw_sequence, calibration_offset=0.05):
    """Main processing pipeline for sensor data"""
    # Step 1: Apply calibration offset
    calibrated = [x - calibration_offset for x in raw_sequence]
    
    # Step 2: Normalize the data
    normalized = normalize_readings(calibrated)
    
    # Step 3: Filter weak signals below threshold
    filtered = [x for x in normalized if x > 0.15]
    
    # Step 4: Apply logarithmic compression for dynamic range
    compressed = [math.log(x + 1) for x in filtered]
    
    # Step 5: Bucket into discrete levels (key transformation)
    binned = [int(x * 10) for x in compressed]
    
    # Irrelevant feature extraction (distraction)
    _ = extract_features(compressed)
    
    # Dead branch: unused conditional
    if len(binned) > 100:
        _ = compute_entropy(binned)
    
    return binned


def analyze_readings(reading_set, thresholds):
    """Final diagnostic engine"""
    # Count occurrences in critical bands
    counts = {}
    for val in reading_set:
        band = val // 3
        counts[band] = counts.get(band, 0) + 1
    
    # Apply threshold logic
    triggered = 0
    for band, cnt in counts.items():
        if cnt >= thresholds.get(band, 100):
            triggered += 1
    
    # Compute final score using modular arithmetic
    base_score = sum(counts.values())
    bonus = triggered * 7
    penalty = len([b for b in counts.keys() if b % 2 == 1]) * 3
    
    # Critical computation step
    raw_diagnostic = (base_score + bonus - penalty) * 13
    
    # Misleading secondary calculation (never used)
    _ = (base_score ** 2) % 97
    
    # Final clamping and scaling
    final_value = max(50, min(raw_diagnostic, 500))
    
    # Decoy mapping
    _ = map_severity(triggered if triggered > 0 else 4)
    
    return int(final_value)

# === MAIN EXECUTION ===
if __name__ == '__main__':
    # Simulated raw input data (sensor readings)
    raw_sensor_data = [
        0.88, 0.91, 0.85, 0.94, 0.87, 0.93, 0.82, 0.96, 0.89, 0.95,
        0.84, 0.92, 0.86, 0.97, 0.83, 0.90, 0.88, 0.91, 0.85, 0.94,
        0.87, 0.93, 0.82, 0.96, 0.89, 0.95, 0.84, 0.92, 0.86, 0.97,
        0.83, 0.90, 0.88, 0.91, 0.85, 0.94, 0.87, 0.93, 0.82, 0.96
    ]

    # Threshold configuration map (critical)
    threshold_map = {
        0: 12, 1: 8, 2: 6, 3: 5, 4: 3
    }

    # Generate irrelevant signal data (distraction)
    _ = generate_signals(baseline=0.5, noise_factor=0.2, count=50)

    # Process the actual data
    processed_data = process_readings(raw_sensor_data, calibration_offset=0.05)

    # Analyze with thresholds (target execution point)
    final_diagnostic = analyze_readings(processed_data, threshold_map)

    # Output result
    print(f"Target result: {final_diagnostic}")