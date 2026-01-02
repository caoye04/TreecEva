import itertools

# Simulated sensor array data from a distributed monitoring system
def generate_sensor_stream(baseline, noise_factor, length):
    return [baseline + (i % 7) * noise_factor for i in range(length)]

# Irrelevant helper: generates dummy timestamps (not used in final result)
def generate_timestamps(count, step_ms=500):
    return [(1623456000 + i * step_ms) for i in range(count)]

# Secondary transformation chain: applies moving average filter
def smooth_signal(signal, window_size=3):
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - window_size + 1)
        smoothed.append(sum(signal[start:i+1]) / (i - start + 1))
    return smoothed

# Bitmask-based feature extraction (only some outputs are relevant)
def extract_features(raw_data):
    magnitude = sum(abs(x) for x in raw_data[:10])
    fluctuation_score = max(raw_data) - min(raw_data)
    parity_flag = int((magnitude % 2) == (fluctuation_score % 2))
    # Distractor computation
    entropy_proxy = 0
    for x in raw_data:
        if x != 0:
            entropy_proxy += abs(x) * abs(x).bit_length()
    return {
        'mag': magnitude,
        'fluct': fluctuation_score,
        'flag': parity_flag,
        'entropy': entropy_proxy  # Dead end
    }

# Core diagnostic processor
def compute_stability_index(features, config):
    base = features['mag'] * config.get('weight_a', 0.8)
    penalty = features['fluct'] * config.get('penalty_b', 0.1)
    adjusted = base - penalty
    
    # Conditional boost (rarely triggered)
    if features['flag'] and features['fluct'] < 50:
        adjusted *= 1.15
    
    # Red herring path
    temp_debug = []
    for i in range(5):
        temp_debug.append((adjusted * i) % 97)
    
    return round(adjusted, 4)

# Complex multi-stage pipeline with decoy branches
def analyze_health_pattern(time_series):
    # Stage 1: Preprocess
    filtered = smooth_signal(time_series, window_size=4)
    truncated = filtered[:12]  # Use only first 12
    
    # Stage 2: Feature extraction
    extracted = extract_features(truncated)
    
    # Stage 3: Stability calculation
    params = {'weight_a': 0.83, 'penalty_b': 0.12}
    index = compute_stability_index(extracted, params)
    
    # Distractor block: unused branch prediction logic
    def predict_failure_risk(seq):
        trend = sum(seq[i] - seq[i-1] for i in range(1, len(seq)))
        risk_level = 'low'
        if trend > 10:
            risk_level = 'high'
        elif trend > 5:
            risk_level = 'medium'
        return {'trend_val': trend, 'level': risk_level}  # Never used
    
    _ = predict_failure_risk(filtered)  # Dead call
    
    # Final normalization
    normalized_score = max(10.0, min(95.0, index))  # Clamp to range
    return normalized_score

# Higher-order orchestrator with tuple unpacking and lambda transforms
def process_metrics(signature, thresholds):
    # Unpack complex structure
    raw_values, mode = signature
    low_th, high_th = thresholds['bounds']
    
    # Apply nonlinear transformation using lambda
    transform = lambda x: x ** 0.5 if x > 0 else 0
    processed = [round(transform(val), 3) for val in raw_values]
    
    # Decoy statistical analysis
    mean_val = sum(processed) / len(processed) if processed else 0
    variance_proxy = sum((x - mean_val) ** 2 for x in processed) / len(processed) if processed else 0
    
    # Real work: conditional accumulation
    accumulator = 18.0
    for i, p in enumerate(processed):
        if p > high_th:
            accumulator += p * 0.7
        elif p < low_th:
            accumulator -= p * 0.3
        else:
            # Key update rule
            accumulator += (p * 0.1) * ((i+1) % 4)
    
    # Dead code path: unreachable due to prior logic
    legacy_modes = {"A": 1, "B": 2}
    if mode in legacy_modes and False:  # Always skipped
        fallback = list(itertools.accumulate(processed, lambda a,b: a + b*0.9))
        accumulator = sum(fallback) % 100
    
    # Final masking operation (bit manipulation red herring)
    bitmasked = int(accumulator) ^ 0xAA  # Distractor
    inverted = bitmasked ^ 0xFF  # More misdirection
    
    # Actual output is untouched by above
    return round(accumulator, 4)

# === MAIN EXECUTION ===
if __name__ == "__main__":
    # Generate realistic input data
    sensor_data = generate_sensor_stream(baseline=23.5, noise_factor=1.8, length=15)
    
    # Unused timestamp array (distractor)
    timestamps = generate_timestamps(len(sensor_data), 250)
    
    # Extract health signature through analysis pipeline
    primary_score = analyze_health_pattern(sensor_data)
    secondary_score = sum(x for x in sensor_data if x > 25) * 0.15
    
    # Build signature tuple (data, mode)
    health_signature = ([primary_score, secondary_score, 42.0, 38.2], "OPERATIONAL")
    
    # Threshold configuration (only bounds are used)
    threshold_map = {
        'version': '2.1',
        'bounds': (15.0, 30.0),
        'calibration': [0.88, 0.92, 0.85]  # Unused
    }
    
    # Critical statement
    final_diagnostic = process_metrics(health_signature, threshold_map)
    
    # Output result as required
    print(f"Target result: {final_diagnostic}")