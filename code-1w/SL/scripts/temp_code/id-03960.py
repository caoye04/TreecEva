import math

# Simulated sensor data processing with diagnostic analysis
def preprocess_sensor(stream, gain=1.5):
    amplified = [x * gain for x in stream]
    filtered = [val for val in amplified if abs(val) > 0.1]
    normalized = [round(x / max(filtered), 3) for x in filtered]
    return normalized

# Irrelevant helper - decoy function (dead path)
def legacy_compatibility(data):
    return [d * 2 for d in data if d > 1]

# Signal feature extraction
def extract_features(signal):
    length = len(signal)
    peaks = sum(1 for i in range(1, length-1) if signal[i-1] < signal[i] > signal[i+1])
    avg_magnitude = sum(abs(x) for x in signal) / length
    zero_crossings = sum(1 for i in range(1, length) if signal[i-1] * signal[i] < 0)
    energy = sum(x**2 for x in signal)
    return {
        'peaks': peaks,
        'avg_mag': avg_mag,
        'zero_cross': zero_crossings,
        'energy': energy,
        'length': length
    }

# Misleading transformation chain (partially unused)
def transform_coordinates(data_points):
    theta = math.pi / 4
    rotated = [(x * math.cos(theta) - y * math.sin(theta),
               x * math.sin(theta) + y * math.cos(theta)) for x, y in data_points]
    scaled = [(p[0]*2, p[1]*1.5) for p in rotated]
    return scaled

# Core analysis logic
def analyze_signal(data, thresholds):
    features = extract_features(data)
    
    # Distractor variables
    temp_cache = {}
    debug_trace = []
    accumulator = 0
    
    for key in ['avg_mag', 'peaks', 'energy']:
        if key in temp_cache:
            continue
        temp_cache[key] = features[key] * 1.1
    
    # Real logic begins
    base_score = features['avg_mag'] * 100
    if features['peaks'] > thresholds['peak_min']:
        base_score += 25
    if features['zero_cross'] > thresholds['cross_threshold']:
        base_score += 15
    
    # Conditional mutation using lambda
    modifier = lambda x: x * 1.2 if x > 50 else x * 0.8
    adjusted_score = modifier(base_score)
    
    # Bit manipulation red herring (irrelevant to final result)
    binary_flag = 0b101010
    masked = binary_flag & 0b111100
    shifted = masked << 2
    
    # Slicing distraction on fake dataset
    history_log = list(range(100, 200, 2))
    recent = history_log[-10:]
    outliers = recent[::3]
    
    # Actual decision path
    if adjusted_score >= thresholds['critical_level']:
        level = 3
    elif adjusted_score >= thresholds['warning_level']:
        level = 2
    else:
        level = 1
    
    # Final computation
    diagnostic_code = int(adjusted_score) + (level * 1000)
    
    # Dead code branch - never executed due to logic above
    if diagnostic_code < 0:
        fallback = math.log(abs(diagnostic_code))
        diagnostic_code = int(fallback)
    
    return diagnostic_code

# Unused complex data structure
system_state = {
    'sensors': {
        'active': [True, False, True],
        'calibration': {'x': 0.98, 'y': 1.02, 'z': 0.99}
    },
    'history': [
        {'time': t, 'val': math.sin(t)} for t in [0.1*i for i in range(50)]
    ]
}

# Main execution
raw_signal = [0.12, -0.34, 0.56, 0.23, -0.67, 0.45, 0.33, -0.22, 0.78, -0.89, 0.11]
processed_data = preprocess_sensor(raw_signal)

# Threshold configuration (only some values are used)
threshold_map = {
    'peak_min': 2,
    'cross_threshold': 3,
    'warning_level': 65.0,
    'critical_level': 85.0,
    'legacy_mode': False,
    'buffer_size': 1024
}

# Fake coordinate transformation (unused)
data_coords = [(1,2), (3,4), (5,6), (7,8)]
transformed_coords = transform_coordinates(data_coords)

# Critical statement
final_diagnostic = analyze_signal(processed_data, threshold_map)

# Print result
print(f"Result: {final_diagnostic}")