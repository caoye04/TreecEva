import math

# Simulated sensor data and configuration
def generate_signals():
    base_frequency = 17.3
    time_points = [t / 100.0 for t in range(200)]
    signal_a = [math.sin(base_frequency * t) for t in time_points]
    signal_b = [math.cos(base_frequency * t + 0.5) for t in time_points]
    return {'A': signal_a, 'B': signal_b}

# Irrelevant helper - distractor
def smooth_signal(data, passes=1):
    temp = data[:]
    for _ in range(passes):
        temp = [(temp[i-1] + temp[i] + temp[(i+1) % len(temp)]) / 3 for i in range(len(temp))]
    return temp

# Data normalization - partially relevant but overcomplicated
def normalize_chunk(chunk):
    mean_val = sum(chunk) / len(chunk)
    variance = sum((x - mean_val) ** 2 for x in chunk) / len(chunk)
    std_dev = math.sqrt(variance) if variance > 0 else 1
    return [(x - mean_val) / std_dev for x in chunk], mean_val, std_dev

# Feature extraction with red herring features
def extract_features(trace):
    length = len(trace)
    peaks = sum(1 for i in range(1, length-1) if trace[i] > trace[i-1] and trace[i] > trace[i+1])
    zero_crossings = sum(1 for i in range(1, length) if trace[i-1] * trace[i] < 0)
    avg_abs = sum(abs(x) for x in trace) / length
    rms = math.sqrt(sum(x*x for x in trace) / length)
    # Distractor: unused complex calculation
    spectral_centroid = sum(i * abs(trace[i]) for i in range(length)) / sum(abs(trace[i]) for i in range(length)) if sum(abs(trace[i]) for i in range(length)) != 0 else 0
    return {
        'peaks': peaks,
        'zero_crossings': zero_crossings,
        'avg_abs': avg_abs,
        'rms': rms,
        'length': length
    }

# Threshold logic with decoy structure
threshold_map = {
    'normal': {'rms': 0.8, 'avg_abs': 0.6},
    'elevated': {'rms': 1.2, 'avg_abs': 0.9},
    'critical': {'rms': 1.8, 'avg_abs': 1.4}
}

# Misleading state tracker (unused)
current_state_flags = [False] * 5
state_transition_log = []

# Core processing pipeline
def process_signal_chain(raw_signals):
    processed = {}
    for key, signal in raw_signals.items():
        # Slice to central segment
        center_start = len(signal) // 4
        center_end = 3 * len(signal) // 4
        centered = signal[center_start:center_end]
        
        # Normalize
        normalized_chunk, mean_norm, std_norm = normalize_chunk(centered)
        
        # Filter extremes (distractor operation with no impact)
        filtered = [x for x in normalized_chunk if -2.5 <= x <= 2.5]
        if len(filtered) < len(normalized_chunk) * 0.7:
            filtered = normalized_chunk  # fallback
        
        # Extract features from normalized data
        features = extract_features(normalized_chunk)  # use original norm, not filtered
        processed[key] = features
    
    return processed, std_norm  # std_norm leaked for distraction

# Diagnostic engine with conditional logic
def evaluate_risk_level(features, thresholds):
    rms_ratio = features['rms'] / thresholds['critical']['rms']
    stress_index = features['peaks'] * features['avg_abs']
    
    # Complex branching with dead paths
    if rms_ratio < 0.5:
        if stress_index < 0.3:
            return 'low'
        elif stress_index < 0.7:
            return 'moderate'
        else:
            return 'high'
    elif rms_ratio < 1.0:
        return 'high'
    else:
        # Only this path matters
        magnitude_score = features['rms'] * 1.5 + features['avg_abs'] * 0.5
        return 'critical' if magnitude_score > 1.6 else 'high'

# Main analysis with tuple unpacking and conditional expression
def analyze_signal(data_dict, thresh):
    all_diagnostics = []
    for label, feats in data_dict.items():
        level = evaluate_risk_level(feats, thresh)
        # Critical conditional expression determining result
        score = (feats['rms'] * 1000 + feats['peaks'] * 10) if level == 'critical' else (feats['avg_abs'] * 500)
        all_diagnostics.append(score)
    
    # Final aggregation with distraction
    raw_total = sum(all_diagnostics)
    adjustment_factor = len(all_diagnostics) if raw_total > 100 else 1
    final_score = raw_total / adjustment_factor
    
    # Decoy transformation
    inverted = [1.0 / (1 + abs(x)) for x in all_diagnostics]
    pseudo_entropy = -sum(p * math.log(p + 1e-8) for p in inverted) if sum(inverted) > 0 else 0
    
    # Actual answer derivation
    baseline = 42.5
    multiplier = 3 if any(d > 900 for d in all_diagnostics) else 1
    final_diagnostic = baseline + final_score * multiplier
    
    # Dead code branch - never executed due to logic above
    if False and pseudo_entropy > 5:
        final_diagnostic -= 100
    
    return final_diagnostic

# Orchestration with irrelevant setup
if __name__ == '__main__':
    # Unused calibration data
    calibration_matrix = [[0.98, 0.02], [0.05, 0.95]]
    alignment_offset = sum(sum(row) for row in calibration_matrix) / 4
    
    signals = generate_signals()
    processed_data, leakage_var = process_signal_chain(signals)  # leakage_var ignored
    
    # Key execution point
    final_diagnostic = analyze_signal(processed_data, threshold_map)
    
    # Output required result
    print(f"Result: {final_diagnostic}")