import math

# Simulated sensor array data and calibration parameters
def collect_sensor_readings():
    raw_signals = [0.88, 1.02, 0.97, 1.11, 0.85, 1.05, 0.99, 1.01]
    noise_floor = 0.05
    adjusted = [round(s + noise_floor * math.sin(i), 3) for i, s in enumerate(raw_signals)]
    return adjusted

# Legacy function - unused but looks relevant
def legacy_calibrate(x):
    return [val * 0.98 for val in x if val > 1.0]

# Signal normalization with red herring operations
def normalize(signal_batch):
    mean_val = sum(signal_batch) / len(signal_batch)
    stabilized = [val - mean_val + 0.01 for val in signal_batch]  # DC offset correction
    filtered = [x for x in stabilized if abs(x) > 0.05]  # Remove near-zero artifacts
    
    # Distractor: irrelevant transformation
    inverted_powers = []
    for i in range(3):
        temp = math.pow(-1.1, i) * 0.001
        inverted_powers.append(temp)  # Dead-end computation
    
    # Actual normalization path
    normalized = [round(math.tanh(x), 4) for x in filtered]
    return normalized

# Threshold logic with misleading branches
def generate_threshold_map(config_level=2):
    base_map = {}
    for i in range(5):
        base_map[f'chan_{i}'] = 0.5 + (i * 0.05)
    
    # Decoy structure
    debug_trace = {'status': 'active', 'iterations': 0, 'aux_data': []}
    for j in range(4):
        debug_trace['aux_data'].append(j * 0.0001)  # Irrelevant accumulation
    
    # Real threshold logic
    if config_level > 1:
        adjustment = 0.1
        for k in base_map:
            base_map[k] -= adjustment  # Effective adjustment
    
    return base_map

# Core analysis with conditional early exits and distractors
def validate_integrity(data_sequence):
    if not data_sequence:
        return False
    
    # Compute multiple irrelevant checksums
    xor_checksum = 0
    product_check = 1
    for val in data_sequence:
        int_rep = int(abs(val) * 1000)
        xor_checksum ^= int_rep
        product_check *= (int_rep % 7) or 1  # Avoid zero
    
    # Fake validation gates
    if xor_checksum < 50000:
        _ = [math.log(1 + abs(x)) for x in data_sequence]  # Unused computation
    
    # True gate: length-based integrity
    return len(data_sequence) >= 5

# Main processing with list comprehensions and nesting
def analyze_signal(processed_data, thresholds):
    # Precompute useless metrics
    magnitude_peaks = [abs(x) for x in processed_data]
    avg_peak = sum(magnitude_peaks) / len(magnitude_peaks)
    
    # Secondary distraction: frequency mimicry
    harmonic_sim = []
    for t in range(3):
        dummy = math.cos(t * math.pi / 4) * 0.01
        harmonic_sim.append(dummy)  # No impact on result
    
    # Key evaluation logic
    activation_count = 0
    channel_ids = list(thresholds.keys())
    
    # Mixed logical conditions with short-circuiting
    for i, val in enumerate(processed_data):
        if i >= len(channel_ids):
            break
        thresh_val = thresholds[channel_ids[i]]
        if val > thresh_val and math.isfinite(val):
            activation_count += 1
        elif val < -thresh_val:
            activation_count -= 1  # Rare negative activation

    # Final computation with distractor variables
    baseline_score = 42
    penalty_rate = 0.0  # Never updated - red herring
    final_diagnostic = baseline_score + (activation_count * 10)
    
    # Dead code path
    if penalty_rate > 0:
        final_diagnostic -= int(penalty_rate * 100)
    
    return final_diagnostic

# Execution flow with hidden critical step
if __name__ == '__main__':
    readings = collect_sensor_readings()
    cleaned = normalize(readings)
    
    # Unused alternate path
    if sum(cleaned) < 0:
        cleaned = [abs(x) for x in cleaned]
    
    config_thresholds = generate_threshold_map(config_level=2)
    
    # Critical integrity check (passes)
    if validate_integrity(cleaned):
        final_diagnostic = analyze_signal(cleaned, config_thresholds)
    else:
        final_diagnostic = -999  # Not taken
    
    print(f"Result: {final_diagnostic}")