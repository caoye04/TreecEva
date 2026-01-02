import math

# Simulated sensor data processing with red herrings and distractions
def preprocess_signal(raw_signal):
    filtered = [x for x in raw_signal if x > -50 and x < 50]
    normalized = [x / max(filtered) for x in filtered if max(filtered) != 0 else [1]]
    smoothed = []
    for i in range(len(normalized)):
        window = normalized[max(0, i-2):min(i+3, len(normalized))]
        smoothed.append(sum(window) / len(window))
    return smoothed

# Irrelevant transformation: frequency domain mock (not used in final result)
def compute_fourier(signal_part):
    real = [sum(math.cos(2 * math.pi * k * n / len(signal_part)) * signal_part[k] 
                for k in range(len(signal_part))) for n in range(len(signal_part))]
    imag = [sum(math.sin(2 * math.pi * k * n / len(signal_part)) * signal_part[k] 
                for k in range(len(signal_part))) for n in range(len(signal_part))]
    return [(r*r + i*i)**0.5 for r, i in zip(real, imag)]

# Distractor function: dead code path
def legacy_calibrate(x):
    return [val * 0.92 for val in x if val > 1]  # Unused

# Core logic disguised among noise
def extract_features(series):
    peaks = []
    for i in range(1, len(series)-1):
        if series[i] > series[i-1] and series[i] > series[i+1]:
            peaks.append(i)
    troughs = []
    for i in range(1, len(series)-1):
        if series[i] < series[i-1] and series[i] < series[i+1]:
            troughs.append(i)
    return peaks, troughs

# Decoy statistical summary (misleading intermediate)
def get_summary_stats(data_slice):
    mean_val = sum(data_slice) / len(data_slice)
    variance = sum((x - mean_val) ** 2 for x in data_slice) / len(data_slice)
    skewness = sum((x - mean_val) ** 3 for x in data_slice) / (len(data_slice) * variance ** 1.5) if variance > 0 else 0
    return {'mean': mean_val, 'var': variance, 'skew': skewness}

# Real but obscured processing path
def transform_sequence(seq):
    shifted = seq[3:] + seq[:3]  # Rotate left by 3
    reversed_chunk = shifted[::-1]
    doubled = [x * 2 for x in reversed_chunk]
    halved = [x / 2 for x in doubled][:len(seq)]
    return halved

# Key analysis function buried in complexity
def analyze_pattern(dynamic_buffer, limit):
    segment = dynamic_buffer[::2]  # Every other element
    cumulative = 0
    trend_flags = []
    for val in segment:
        if abs(val) > limit:
            cumulative += int(val ** 2 % 7)  # Nonlinear accumulation
        else:
            cumulative -= 1
        trend_flags.append(cumulative > 0)
    
    # Actual answer derived here
    decision_metric = cumulative * len(trend_flags)
    
    # More distractions below
    secondary_check = sum(1 for f in trend_flags if f) * 0.7
    penalty = len([f for f in trend_flags if not f]) * 0.3
    final_score = (secondary_check - penalty) * decision_metric  # Not used
    
    return decision_metric  # This is the real output

# Main execution with layered setup and decoys
if __name__ == "__main__":
    # Initial dataset
    base_readings = [1.2, -3.4, 5.6, 2.1, -4.3, 6.7, 0.5, -1.8, 3.9, 2.2]
    
    # Red herring variables
    calibration_offset = 0.87
    system_gain = 1.04
    timestamp_log = [1680000000 + i*60 for i in range(len(base_readings))]
    validity_mask = [True if x % 2 == 0 else False for x in range(len(timestamp_log))]
    
    # First layer of processing (partially relevant)
    processed = preprocess_signal(base_readings)
    
    # Dead branch: looks important but unused
    if len(processed) > 5:
        spectral_analysis = compute_fourier(processed[:4])
        config_profile = {"mode": "high_res", "gain": system_gain}
    else:
        spectral_analysis = []
        config_profile = {"mode": "low_power"}
    
    # Feature extraction (distractor results)
    peak_indices, valley_indices = extract_features(processed)
    feature_summary = {
        "peaks": len(peak_indices),
        "troughs": len(valley_indices),
        "ratio": len(peak_indices) / len(valley_indices) if len(valley_indices) > 0 else 0
    }
    
    # Another irrelevant stat block
    stats_snapshot = get_summary_stats(processed[1:6])
    
    # Core transformation chain begins
    transformed_data = transform_sequence(processed)
    
    # Control flow misdirection
    mode_selector = "A"
    if sum(transformed_data) > 5:
        mode_selector = "B"
    elif any(x < -2 for x in transformed_data):
        mode_selector = "C"
    else:
        mode_selector = "D"
    
    # Hidden threshold determination
    threshold = 1.5  # Hardcoded but non-obvious
    if mode_selector == "X":  # Never true
        threshold = 2.0
    else:
        temp_ref = [x for x in transformed_data if x > 0]
        if temp_ref:
            threshold = min(temp_ref)  # Would change it, but doesn't matter due to logic
    
    # Critical statement
    final_diagnostic = analyze_pattern(transformed_data, threshold)
    
    # Print required result
    print(f"Result: {final_diagnostic}")