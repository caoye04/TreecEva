def analyze_pattern(sequence):
    if len(sequence) < 3:
        return 0
    return sum(1 for i in range(len(sequence)-2) if sequence[i] < sequence[i+1] > sequence[i+2])

# Irrelevant helper function (decoy)
def validate_input(data):
    if not isinstance(data, list) or any(not isinstance(x, (int, float)) for x in data):
        raise ValueError("Invalid input")
    return True

# Unused transformation (dead code path)
def transform_scale(values, exponent=2):
    return [x ** exponent for x in values if x > 0]

# Red herring computation with no downstream use
temp_offset = 4.75
adjustment_log = []
for i in range(5):
    temp_offset *= 0.9
    adjustment_log.append(round(temp_offset, 3))

# Simulated sensor drift compensation (partially irrelevant)
calibration_cache = {}
def apply_drift_correction(raw_value, timestamp):
    base_rate = 0.015
    if timestamp in calibration_cache:
        return calibration_cache[timestamp]
    corrected = raw_value * (1 - base_rate * (timestamp % 10))
    calibration_cache[timestamp] = round(corrected, 4)
    return calibration_cache[timestamp]

# Main processing with key logic embedded
def extract_features(data_slice):
    window_size = 4
    features = []
    for i in range(len(data_slice) - window_size + 1):
        segment = data_slice[i:i+window_size]
        avg = sum(segment) / len(segment)
        peak = max(segment)
        trend = segment[-1] - segment[0]
        # Slicing and string-based tagging
        label = ''.join(['H' if x >= avg else 'L' for x in segment])
        score = abs(trend) * (peak / (avg + 1e-8))
        features.append((score, label))
    return features

# Core function that contains the actual answer derivation
def process_readings(readings, factor):
    # Normalize readings using slicing and scaling
    trimmed = readings[1:-1]  # Remove first and last as outliers
    normalized = [(x - min(trimmed)) / (max(trimmed) - min(trimmed) + 1e-8) * factor for x in trimmed]
    
    # Feature extraction step
    feats = extract_features(normalized)
    
    # Compute diagnostic metric: average of high-variance segments
    high_var_scores = []
    for score, tag in feats:
        if tag.count('H') >= 2 and len(tag) == 4:
            high_var_scores.append(score)
    
    # Secondary filter based on pattern peaks
    pattern_count = analyze_pattern([int(f*10) for f in normalized if f < 0.8])
    
    # Final computation chain
    base_metric = sum(high_var_scores) / (len(high_var_scores) + 1e-8)
    adjustment = max(0.5, min(1.5, 0.1 * pattern_count + 0.9))
    intermediate_result = base_metric * adjustment
    
    # String-based switch for mode selection (distraction)
    mode_flag = "CALIBRATED" if factor > 1.0 else "STANDARD"
    if "CAL" in mode_flag:
        intermediate_result += 0.05
    
    # Actual answer derived here
    final_diagnostic = int(intermediate_result * 1000)  # Critical conversion
    
    # Distractor: unused complex structure
    summary_report = {
        'version': '2.1',
        'readings_processed': len(trimmed),
        'anomalies_detected': sum(1 for x in readings if x < 0),
        'checksum': sum(hash(str(x)) % 1000 for x in readings[:3])
    }
    
    return final_diagnostic

# Simulated sensor data (real input)
sensor_data = [0.12, 0.35, 0.91, 1.24, 0.88, 0.63, 1.05, 1.32, 0.47, 0.21]
calibration_factor = 2.5

# Execution point of interest
final_diagnostic = process_readings(sensor_data, calibration_factor)

# Output result as required
print(f"Result: {final_diagnostic}")