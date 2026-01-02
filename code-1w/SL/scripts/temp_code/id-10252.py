import itertools

# Simulated sensor data preprocessing with red herrings
def preprocess_signals(raw_samples):
    filtered = [x for x in raw_samples if x > -50 and x < 300]
    offset = sum(filtered) // len(filtered) if filtered else 0
    adjusted = [x + offset for x in filtered]
    return adjusted

# Irrelevant transformation - decoy function
def spectral_decompose(data):
    result = []
    for i in range(len(data)):
        val = 0
        for j in range(min(i+1, 5)):
            val += data[i] * (0.5 ** j)
        result.append(val % 100)
    return result  # Never used in final computation

# Core pattern transformation with distractors
def transform_sequence(signal, mode='advanced'):
    if mode == 'basic':
        return [x * 2 for x in signal]
    elif mode == 'advanced':
        # Real transformation path
        doubled = [x * 2 for x in signal]
        shifted = [x >> 1 for x in doubled]  # Bit manipulation red herring
        modded = [x % 97 for x in shifted]
        return modded
    else:
        return signal

# Misleading accumulation function - looks important but unused
def compute_rolling_moment(data, window=3):
    moments = []
    for i in range(len(data) - window + 1):
        window_data = data[i:i+window]
        mean_val = sum(window_data) / len(window_data)
        moment = sum((x - mean_val) ** 3 for x in window_data)
        moments.append(moment)
    return moments

# Real analysis logic buried among distractions
def analyze_pattern(seq, threshold):
    count = 0
    total = 0
    for i, val in enumerate(seq):
        if i % 2 == 0 and val > threshold:
            count += 1
            total += val
    # Critical calculation: harmonic balance index
    if count > 0:
        hbi = total / (count * threshold)
    else:
        hbi = 0
    # Final diagnostic is derived from harmonic balance
    diagnostic_score = int(hbi * 100) & 0xFFFF  # Mask to 16 bits
    return diagnostic_score

# --- Main execution with extensive distractions ---
if __name__ == '__main__':
    # Raw sensor inputs (real data source)
    raw_input_stream = [12, 45, 67, 23, 89, 34, 77, 56, 88, 29]
    
    # Distractor variables - look like calibration constants
    baseline_correction = 0.87
    gain_factor = 2.1
    noise_floor = -45
    calibration_matrix = [[1, 0], [0, 1]]
    temporal_weights = [0.1, 0.3, 0.5, 0.7, 0.9]
    
    # Real processing begins here
    cleaned = preprocess_signals(raw_input_stream)
    
    # Multiple transformations - only one matters
    candidate_a = transform_sequence(cleaned, mode='basic')
    candidate_b = transform_sequence(cleaned, mode='advanced')  # This one is used
    candidate_c = transform_sequence(cleaned, mode='legacy')
    
    # Dead code path - looks like it might be used
    if len(candidate_a) > 100:
        active_branch = candidate_a
    elif len(candidate_b) > 5:
        active_branch = candidate_b  # Correct branch taken
    else:
        active_branch = candidate_c
    
    # More distractions
    snapshot_log = {}
    for idx, val in enumerate(active_branch):
        hex_key = f"pos_{idx:02x}"
        snapshot_log[hex_key] = val * baseline_correction  # Unused log
    
    # Key threshold derived from irrelevant formula
    dummy_ratio = gain_factor / baseline_correction
    key_threshold = 50 + int(dummy_ratio * 2)  # Evaluates to 52
    
    # Actual critical transformation
    transformed_data = [x ^ (x % 13) for x in active_branch]  # XOR obfuscation
    
    # Decoy analysis on wrong data
    fake_analysis = compute_rolling_moment(candidate_a)
    power_spectrum = spectral_decompose(candidate_c)
    
    # Final determination - the real answer
    final_diagnostic = analyze_pattern(transformed_data, key_threshold)
    
    # Print required result
    print(f"Target result: {final_diagnostic}")