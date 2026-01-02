import math

# Simulated sensor data processing with diagnostic analysis
def collect_signals():
    raw_samples = [i * 0.5 for i in range(20)]
    noise_floor = 0.23
    filtered = []
    for x in raw_samples:
        if x > 5.0:
            adjusted = x * math.sin(x) + noise_floor
        else:
            adjusted = x * 0.9 + noise_floor
        filtered.append(round(adjusted, 4))
    return filtered

# Irrelevant helper - looks useful but not part of main logic
def deprecated_normalizer(data):
    max_val = max(data)
    return [x / max_val for x in data] if max_val != 0 else data

# Core transformation pipeline
def preprocess(signal_list):
    squared = [x ** 2 for x in signal_list]
    shifted = [s - 1.5 for s in squared]
    rectified = [abs(s) for s in shifted]
    return rectified

# Frequency domain approximation (distractor)
def compute_harmonics(samples, base_freq=2.0):
    harmonics = []
    for i, s in enumerate(samples):
        phase = base_freq * i * 0.1
        harmonic = s * math.cos(phase)
        harmonics.append(harmonic)
    return harmonics  # Never used in final result

# Bitmask-based feature extraction (mixed relevance)
def extract_features(dataset):
    features = []
    for val in dataset:
        int_rep = int(abs(val) * 10) & 0xFF  # Scale and mask to 8 bits
        bit_count = bin(int_rep).count('1')
        parity_flag = int_rep ^ 0xAA  # XOR with magic number
        features.append({'value': val, 'bits': bit_count, 'flag': parity_flag})
    return features

# Threshold logic with set-based condition filtering
threshold_config = {
    'low': 3.0,
    'medium': 7.5,
    'high': 12.0
}

# Unused legacy thresholds (red herring)
legacy_bounds = {k: v * 1.1 for k, v in threshold_config.items()}

# Main analysis engine
def analyze_signal(clean_data, thresholds):
    # Compute statistical baseline
    mean_val = sum(clean_data) / len(clean_data)
    deviances = [abs(x - mean_val) for x in clean_data]
    avg_deviance = sum(deviances) / len(deviances)
    
    # Set operations to identify critical ranges
    high_outliers = {i for i, x in enumerate(clean_data) if x > thresholds['high']}
    medium_range = {i for i, x in enumerate(clean_data) if thresholds['medium'] <= x <= thresholds['high']}
    active_indices = high_outliers | medium_range
    
    # Destructuring assignment - unpack first three deviations
    try:
        d1, d2, d3 = deviances[:3]
    except ValueError:
        d1 = d2 = d3 = avg_deviance
        
    # Complex conditional integration
    score_basis = 0.0
    if len(high_outliers) > 0:
        score_basis += 25.7
    if avg_deviance > mean_val * 0.4:
        score_basis += 18.3
    
    # Bit manipulation disguised as calibration
    calibration_key = 0x1F
    for idx in active_indices:
        calibration_key ^= (idx & 0x0F)
    
    # Final computation path
    adjustment_factor = len(active_indices) * 0.65
    if calibration_key % 2 == 0:
        adjustment_factor += 1.5
    
    # Critical line: this determines the answer
    final_diagnostic = (score_basis + adjustment_factor) * (1 + math.log(1 + avg_deviance))
    
    # Dead code branch - looks like post-processing
    if final_diagnostic < 0:
        final_diagnostic = 0.0
    
    return round(final_diagnostic, 6)

# Orchestration sequence
if __name__ == "__main__":
    # Step 1: Collect raw signals
    sensor_input = collect_signals()
    
    # Step 2: Preprocess data
    processed_data = preprocess(sensor_input)
    
    # Step 3: Extract features (partially relevant)
    feature_set = extract_features(processed_data)
    
    # Step 4: Compute harmonics (completely irrelevant - red herring)
    spectral_analysis = compute_harmonics(sensor_input)
    
    # Step 5: Build threshold map
    threshold_map = {**threshold_config}
    
    # Step 6: Run final analysis
    final_diagnostic = analyze_signal(processed_data, threshold_map)
    
    # Output result
    print(f"Result: {final_diagnostic}")