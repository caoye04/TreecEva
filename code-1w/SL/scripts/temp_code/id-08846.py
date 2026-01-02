import math

# Simulated sensor data and calibration parameters
def load_sensor_readings():
    raw_values = [2.1, 3.5, -1.2, 4.8, 0.0, -3.3, 6.7, 1.4]
    offsets = {'sensor_a': 0.1, 'sensor_b': -0.2, 'sensor_c': 0.3}
    scale_factor = 1.05
    adjusted = [round((v + offsets['sensor_a']) * scale_factor, 2) for v in raw_values]
    return adjusted

# Irrelevant preprocessing: spectral decomposition (unused)
def decompose_frequency(signal):
    freq_components = []
    for i in range(len(signal)):
        component = sum(math.sin(x * i) for x in signal[:4])
        freq_components.append(round(component, 3))
    return freq_components  # Never used

# Data masking based on dynamic thresholds
def apply_mask(data, config):
    masked = []
    for val in data:
        if abs(val) < config.get('noise_floor', 1.0):
            masked.append(0.0)
        else:
            masked.append(val * config.get('gain', 1.2))
    return masked

# Signal feature extraction with distractor logic
def extract_features(signal_stream):
    stats = {
        'peak': max(signal_stream, default=0),
        'trough': min(signal_stream, default=0),
        'range': 0,
        'clipped': False
    }
    stats['range'] = stats['peak'] - stats['trough']
    
    # Distractor: complex edge detection (not used in final path)
    edges = []
    for i in range(1, len(signal_stream)):
        diff = abs(signal_stream[i] - signal_stream[i-1])
        if diff > 2.0:
            edges.append((i-1, i))
    edge_density = len(edges) / len(signal_stream) if signal_stream else 0
    
    # Another red herring: transform to frequency domain (computed but unused)
    transformed = [math.cos(x) * math.exp(-x/10) for x in signal_stream]
    avg_transform = sum(transformed) / len(transformed)
    
    return stats  # Only 'stats' is passed forward

# Core analysis function with conditional logic and dictionary operations
def analyze_signal(data_chunk, thresholds):
    result_map = {}
    for key, thresh in thresholds.items():
        count_above = sum(1 for x in data_chunk if x > thresh)
        result_map[key] = count_above
    
    # Conditional expression determining mode
    mode = 'critical' if result_map['high_risk'] > 2 else 'stable'
    
    # Slicing operation with relevance
    segment = data_chunk[1:-1]  # Exclude first and last
    mid_avg = sum(segment) / len(segment) if segment else 0
    
    # Key branching logic
    if mode == 'critical':
        base_score = mid_avg * 150
    else:
        base_score = mid_avg * 50
    
    # Bit manipulation red herring (irrelevant computation)
    encoded_flag = 0
    for val in data_chunk[:3]:
        shifted = int(abs(val) * 10) << 2
        encoded_flag ^= shifted
    
    # Decoy dictionary update (no effect)
    result_map['diagnostic_flag'] = encoded_flag
    result_map['status'] = mode
    
    # Final calculation using only a subset of logic
    adjustment = 0.8 if 'mid_range' in result_map and result_map['mid_range'] == 0 else 1.0
    final_score = base_score * adjustment
    
    return final_score

# Unused recursive validation (dead code path)
def validate_consistency(arr, idx=0):
    if idx >= len(arr) - 1:
        return True
    if abs(arr[idx+1] - arr[idx]) > 5.0:
        return False
    return validate_consistency(arr, idx + 1)

# Main execution flow
if __name__ == "__main__":
    # Load and preprocess data
    readings = load_sensor_readings()  # [2.31, 3.68, -1.09, 5.04, 0.11, -3.36, 7.04, 1.57]
    
    # Apply masking (used)
    config = {'noise_floor': 1.0, 'gain': 1.2}
    filtered_data = apply_mask(readings, config)
    
    # Extract features (only returns stats, others discarded)
    features = extract_features(filtered_data)
    
    # Prepare threshold map (critical for final result)
    threshold_map = {
        'high_risk': 4.0,
        'moderate_risk': 2.0,
        'low_risk': 0.5,
        'mid_range': 3.0
    }
    
    # Simulate unused set-based filtering
    unique_values = set(round(x, 1) for x in filtered_data)
    reference_set = {1.2, 2.4, 3.6, 4.8}
    overlap_count = len(unique_values & reference_set)  # Computed but unused
    
    # Processed data used in analysis
    processed_data = [round(x, 2) for x in filtered_data if x != 0.0]
    
    # Dead code: slice reversal check (never called)
    reversed_check = lambda seq: seq == seq[::-1]
    
    # Critical statement
    final_diagnostic = analyze_signal(processed_data, threshold_map)
    
    # Print result
    print(f"Result: {final_diagnostic}")