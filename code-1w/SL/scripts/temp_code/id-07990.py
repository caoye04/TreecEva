import math

# Sensor simulation and diagnostic analysis system
def generate_signals(baseline, noise_factor, count):
    """Generates synthetic sensor readings (distractor function)"""
    return [baseline + noise_factor * math.sin(i) for i in range(count)]


def validate_checksum(data_list):
    """Calculates a checksum for data integrity (partially relevant)"""
    checksum = 0
    for val in data_list:
        checksum ^= int(val * 100) % 256
    return checksum == 127


def extract_features(raw_sequence):
    """Extracts statistical features from sensor sequence"""
    n = len(raw_sequence)
    mean_val = sum(raw_sequence) / n
    variance = sum((x - mean_val) ** 2 for x in raw_sequence) / n
    peak = max(raw_sequence)
    # Dead code path - never used later
    if variance < 0.1:
        return {'type': 'flat', 'value': mean_val}
    return {'type': 'variable', 'mean': mean_val, 'variance': variance, 'peak': peak}


def transform_scale(x, mode='linear'):
    """Irrelevant scaling function with decoy logic"""
    if mode == 'log':
        return math.log(abs(x) + 1)
    elif mode == 'sqrt':
        return math.sqrt(abs(x))
    else:
        return x * 1.0

# Main diagnostic pipeline
sensor_ids = ['S1', 'S2', 'S3', 'S4']
raw_readings = {
    'S1': [1.2, 1.3, 0.9, 1.5, 1.8],
    'S2': [2.1, 1.8, 2.3, 2.0, 1.9],
    'S3': [0.8, 0.7, 0.6, 0.9, 1.0],
    'S4': [3.1, 3.3, 3.0, 3.2, 3.4]
}

# Irrelevant transformation chain
scaled_readings = {}
for sid in sensor_ids:
    scaled_readings[sid] = [transform_scale(x, 'linear') for x in raw_readings[sid]]

# Feature extraction (some results discarded)
diagnostic_features = {}
for key, values in scaled_readings.items():
    feat = extract_features(values)
    diagnostic_features[key] = feat

# Simulated threshold map from calibration data (used in final step)
threshold_map = {
    'S1': {'mean_low': 1.0, 'mean_high': 1.6, 'var_threshold': 0.1},
    'S2': {'mean_low': 1.7, 'mean_high': 2.4, 'var_threshold': 0.08},
    'S3': {'mean_low': 0.5, 'mean_high': 1.1, 'var_threshold': 0.05},
    'S4': {'mean_low': 3.0, 'mean_high': 3.5, 'var_threshold': 0.03}
}

# Intermediate structure with misleading fields
temp_analysis = {}
for s_id in sensor_ids:
    data = scaled_readings[s_id]
    avg = sum(data) / len(data)
    var = sum((x - avg) ** 2 for x in data) / len(data)
    temp_analysis[s_id] = {
        'avg': avg,
        'variance': var,
        'count': len(data),
        'status_flag': (1 if avg > 1.0 else 0),  # Distractor field
        'checksum_valid': validate_checksum(data)   # Computed but unused
    }

# Real processing begins here - core logic buried in noise
processed_data = []
for s_id in sensor_ids:
    entry = temp_analysis[s_id]
    thresholds = threshold_map[s_id]
    deviation_score = 0
    
    # Mean check
    if entry['avg'] < thresholds['mean_low']:
        deviation_score += 1
    elif entry['avg'] > thresholds['mean_high']:
        deviation_score += 2
    
    # Variance check
    if entry['variance'] > thresholds['var_threshold']:
        deviation_score += 3
    
    # Hidden combinatoric weight based on ID length (subtle pattern)
    weight = len(s_id) % 2 + 1  # S1,S3 -> 2; S2,S4 -> 1
    weighted_deviation = deviation_score * weight
    
    processed_data.append({
        'id': s_id,
        'score': deviation_score,
        'weighted': weighted_deviation,
        'meta': f"D{len(s_id)}"  # Red herring
    })

# Critical function: computes final diagnostic index
def analyze_readings(readings_list, limits):
    total_index = 0
    severity_map = {}  # Unused tracking
    
    for item in readings_list:
        raw_score = item['score']
        w_score = item['weighted']
        
        # Complex conditional scoring
        if raw_score == 0:
            category = 'normal'
            contribution = 5
        elif raw_score <= 2:
            category = 'warning'
            contribution = 15
        else:
            category = 'critical'
            contribution = 40
        
        # Additional penalty if weighted score exceeds threshold
        if w_score >= 3:
            contribution *= 2
        
        # Decoy dictionary update
        severity_map[item['id']] = {
            'cat': category,
            'base': contribution // (2 if w_score >= 3 else 1)
        }
        
        total_index += contribution
    
    # Final nonlinear transformation
    if total_index > 0:
        total_index = int(math.sqrt(total_index ** 2 / (len(readings_list) or 1)))
    
    # Apply hidden correction factor based on initial checksums (only some valid)
    correction = 0
    for r_id in ['S1', 'S2', 'S3', 'S4']:
        chk_data = [transform_scale(x) for x in raw_readings[r_id]]
        if validate_checksum(chk_data):  # All false in this case
            correction += 5
    
    return total_index - correction

# Execute main analysis
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Output result as required
print(f"Result: {final_diagnostic}")