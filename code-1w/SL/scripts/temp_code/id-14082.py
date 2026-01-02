import math

# Simulated sensor data processing system
def acquire_signal(raw=False):
    base_readings = [3.2, 4.1, 2.8, 5.6, 6.3, 4.9, 3.7, 5.1]
    if raw:
        return [int(x * 10) for x in base_readings]  # Irrelevant raw conversion
    normalized = [round(math.log(x) + 0.5, 2) for x in base_readings]
    return normalized

# Irrelevant auxiliary function (dead path)
def compress_data(signal):
    return signal[::2]

# Misleading transformation chain
def filter_noise(signal, level=1):
    result = signal.copy()
    for _ in range(level):
        smoothed = []
        for i in range(len(result)):
            neighbors = result[max(0, i-1):min(i+2, len(result))]
            smoothed.append(round(sum(neighbors) / len(neighbors), 2))
        result = smoothed
    return result  # Used but partially irrelevant

# Distractor: complex frequency analysis (unused)
def compute_harmonics(signal):
    harmonics = {}
    for i in range(1, 5):
        harmonic_value = sum(math.sin(x * i) for x in signal)
        harmonics[f'h_{i}'] = round(harmonic_value, 3)
    return harmonics

# Real preprocessing step mixed with noise
def preprocess_signal(raw_signal):
    # Actual relevant path begins here
    shifted = [x + 0.8 for x in raw_signal]  # Shift for calibration
    squared = [round(x ** 2, 2) for x in shifted]  # Energy approximation
    
    # Distractor: unused conditional branch
    if len(squared) > 10:
        return squared[:10]
        
    # Another red herring: entropy calculation (not used later)
    total = sum(squared)
    if total == 0:
        entropy = 0
    else:
        entropy = -sum((x/total) * math.log(x/total) for x in squared if x > 0)
    
    # Relevant transformation: normalize to unit interval
    max_val = max(squared)
    if max_val != 0:
        normalized = [round(x / max_val, 3) for x in squared]
    else:
        normalized = squared
    
    return normalized

# Threshold mapping with decoy entries
def generate_thresholds():
    thresholds = {
        't_01': 0.31,
        't_05': 0.42,
        't_10': 0.68,  # This one is actually used
        't_15': 0.73,
        'fail_safe': 0.05,
        'debug_mode': 0.99,
        'placeholder': 0.00
    }
    # Remove decoys (but looks like filtering)
    active_keys = [k for k in thresholds.keys() if 't_' in k and k[-2:].isdigit()]
    clean_map = {k: thresholds[k] for k in active_keys}
    return clean_map

# Core analysis logic
def analyze_signal(data, thresholds):
    # Key variable assignment point
    segment_a = data[:4]
    segment_b = data[4:]
    
    # Irrelevant statistical measures
    mean_a = round(sum(segment_a) / len(segment_a), 3)
    mean_b = round(sum(segment_b) / len(segment_b), 3)
    diff = abs(mean_a - mean_b)
    
    # Decoy pattern detection
    pattern_match = False
    if len(data) >= 6:
        trend = [1 if data[i+1] > data[i] else 0 for i in range(len(data)-1)]
        runs = sum(1 for i in range(1, len(trend)) if trend[i] != trend[i-1])
        if runs > 4:
            pattern_match = True
    
    # ACTUAL critical computation
    t_ref = thresholds['t_10']  # Critical threshold
    count_above = sum(1 for x in data if x >= t_ref)
    
    # Final diagnostic score (this is the answer)
    if count_above >= 3:
        score = int((count_above * 100) / len(data))
    else:
        score = int((diff * 50))
    
    # Unused fallback
    if score == 0 and pattern_match:
        score = 10
        
    return score

# Entry point
if __name__ == "__main__":
    raw_input = acquire_signal(raw=False)
    filtered_signal = filter_noise(raw_input, level=1)
    processed_data = preprocess_signal(filtered_signal)
    
    # Generate map with multiple decoy keys
    threshold_map = generate_thresholds()
    
    # UNUSED: compression test
    if len(processed_data) > 8:
        compressed = compress_data(processed_data)
    
    # UNUSED: frequency domain check
    freq_analysis = compute_harmonics(raw_input)
    anomaly_detected = False
    if 'h_3' in freq_analysis and freq_analysis['h_3'] > 1.5:
        anomaly_detected = True
    
    # CRITICAL EXECUTION POINT
    final_diagnostic = analyze_signal(processed_data, threshold_map)
    
    # Output result
    print(f"Result: {final_diagnostic}")