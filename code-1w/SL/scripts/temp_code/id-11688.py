import math

# Simulated sensor data processing with diagnostic evaluation
def preprocess_readings(raw_samples):
    filtered = [x for x in raw_samples if 0 <= x <= 1000]
    normalized = [(x - min(filtered)) / (max(filtered) - min(filtered) + 1e-8) for x in filtered]
    return normalized

# Irrelevant helper: statistical moment calculation (distractor)
def calculate_skewness(data):
    n = len(data)
    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / n
    if variance == 0:
        return 0.0
    std_dev = math.sqrt(variance)
    skew = sum(((x - mean) / std_dev) ** 3 for x in data) / n
    return skew

# Core transformation function
def apply_wavelet_transform(signal):
    transformed = []
    for i in range(len(signal)):
        component = 0.0
        for j in range(1, 5):
            phase = math.sin(i * j * math.pi / 8)
            amplitude = signal[i] * math.exp(-0.1 * j)
            component += amplitude * phase
        transformed.append(abs(component))
    return transformed

# Decoy pattern matcher (dead path)
def detect_anomaly_legacy(pattern):
    critical_flags = set()
    for idx, val in enumerate(pattern):
        if val > 0.8 and idx % 3 == 0:
            critical_flags.add(idx)
    return len(critical_flags) > 5

# Real pattern analyzer
def analyze_pattern(seq, threshold):
    # Apply lambda-based filtering
    relevance_filter = lambda x: x > threshold
    significant = list(filter(relevance_filter, seq))
    
    # Set operations on indices
    high_indices = set(i for i, x in enumerate(seq) if x > threshold * 1.2)
    medium_indices = set(i for i, x in enumerate(seq) if threshold * 0.8 <= x <= threshold * 1.2)
    overlap_check = high_indices & medium_indices  # Always empty, but included for distraction
    
    # String-encoded state transitions (distractor)
    state_log = ''.join('H' if x > threshold else 'L' for x in seq[:20])
    transitions = sum(1 for a, b in zip(state_log, state_log[1:]) if a != b)
    
    # Actual computation path
    base_score = sum(1 for x in significant if x < 0.95)
    penalty = 0
    for i in range(1, len(significant)):
        if significant[i] < significant[i-1]:
            penalty += 1
    
    # Final logic
    adjustment = len(high_indices) // 2
    result = base_score * 3 - penalty + adjustment
    
    # Dead code below (never used)
    debug_snapshot = {
        'moment': calculate_skewness(seq),
        'transitions': transitions,
        'flags': detect_anomaly_legacy(seq)
    }
    
    return result

# Entry point
if __name__ == '__main__':
    # Simulated input (real data source)
    raw_sensor_data = [123, 45, 678, 234, 901, 12, 450, 67, 890, 345, 678, 123, 456, 789, 100]
    
    # Irrelevant preprocessing chain
    stats_summary = {
        'count': len(raw_sensor_data),
        'peak': max(raw_sensor_data),
        'trough': min(raw_sensor_data),
        'median_guess': sorted(raw_sensor_data)[len(raw_sensor_data)//2]
    }
    
    processed = preprocess_readings(raw_sensor_data)
    
    # Unused alternate branch
    if len(processed) > 10:
        temp_analysis = [math.log(x + 1e-5) for x in processed]
        normalized_entropy = -sum(x * math.log(x + 1e-5) for x in processed)
    
    # Key transformation
    transformed_data = apply_wavelet_transform(processed)
    
    # Red herring variables
    noise_floor = sum(math.cos(x) for x in transformed_data[:5])
    spectral_kurtosis = math.pow(sum(x**4 for x in transformed_data)/len(transformed_data), 0.25)
    
    # Critical threshold derived from logic
    key_threshold = 0.4 + math.sin(math.pi / 6)  # Evaluates to 0.4 + 0.5 = 0.9
    
    # Target execution point
    final_diagnostic = analyze_pattern(transformed_data, key_threshold)
    
    # Print required result
    print(f"Result: {final_diagnostic}")