import math

# Simulated sensor data processing system for environmental monitoring
# Contains relevant logic mixed with extensive distractors

def analyze_pattern(sequence):
    # Irrelevant function - dead code path
    return sum([x ** 2 for x in sequence if x % 3 == 0])

def validate_checksum(data):
    # Misleading function - looks important but unused in critical path
    return (sum(data) * 7) % 13

def transform_signal(signal_data):
    # Distractor transformation - used to generate noise variables
    transformed = []
    for val in signal_data:
        if val < 0:
            transformed.append(abs(val) * 0.5)
        else:
            transformed.append(math.sqrt(val) if val > 0 else 0)
    return [round(x, 3) for x in transformed]

def compute_entropy(values):
    # Seemingly sophisticated but irrelevant computation
    total = sum(values)
    if total == 0:
        return 0
    probs = [v / total for v in values]
    entropy = -sum(p * math.log2(p) for p in probs if p > 0)
    return round(entropy, 4)

def decode_sequence(seq_str):
    # String manipulation red herring
    reversed_chunks = [chunk[::-1] for chunk in seq_str.split('-')]
    flattened = ''.join(reversed_chunks)
    try:
        return [int(flattened[i:i+2]) for i in range(0, len(flattened), 2)]
    except:
        return [0]

def filter_outliers(data, threshold=1.5):
    # Real but non-critical preprocessing
    if len(data) < 3:
        return data
    q1 = sorted(data)[len(data)//4]
    q3 = sorted(data)[3*len(data)//4]
    iqr = q3 - q1
    low = q1 - threshold * iqr
    high = q3 + threshold * iqr
    return [x for x in data if low <= x <= high]

def aggregate_readings(raw_readings):
    # Relevant but indirect - used in final pipeline
    filtered = filter_outliers(raw_readings)
    base_score = sum(filtered) / len(filtered) if filtered else 0
    adjustment = len([x for x in filtered if x > 50]) * 0.3
    return base_score + adjustment

def extract_flags(metadata_list):
    # Bit manipulation decoy
    flag_value = 0
    for meta in metadata_list:
        flag_value ^= int(meta[-1]) << (int(meta[0]) % 4)
    return flag_value & 255

def evaluate_stability(readings):
    # Another distraction - not used in final result
    diffs = [abs(readings[i+1] - readings[i]) for i in range(len(readings)-1)]
    return max(diffs) < 15 and len([d for d in diffs if d > 10]) < 3

def process_metrics(diag, readings):
    # CORE FUNCTION: This is where the answer is determined
    reading_avg = sum(readings) / len(readings)
    
    # Dictionary-based mapping - relevant concept
    level_map = {
        'critical': 90,
        'elevated': 75,
        'normal': 60,
        'optimal': 45
    }
    
    # Extract status from diagnostic string using string methods
    status_line = diag['status'].strip().lower()
    confidence = diag['confidence']
    
    # Key extraction using string operations
    if 'optimal' in status_line:
        base_level = level_map['optimal']
    elif 'normal' in status_line:
        base_level = level_map['normal']
    elif 'elevated' in status_line:
        base_level = level_map['elevated']
    else:
        base_level = level_map['critical']
    
    # Critical calculation step
    variation = max(readings) - min(readings)
    stability_factor = 1.0 - (variation / 100.0)
    
    # Incorporate confidence weighting
    adjusted_base = base_level * (0.8 + (confidence * 0.2))
    
    # Final composite metric
    final_score = adjusted_base * stability_factor
    
    # Additional transformation that affects result
    if final_score < 50:
        final_score = final_score * 1.15
    else:
        final_score = final_score * 0.95
    
    # Round to nearest integer - this becomes the answer
    return int(round(final_score))

# MAIN EXECUTION WITH DISTRACTORS
if __name__ == '__main__':
    # === REAL INPUT DATA (mixed with irrelevant variables) ===
    sensor_ids = ['S10X', 'S11Y', 'S12Z', 'S13W']  # Unused list
    calibration_key = "7B2-F9A-1C3"  # Looks important but unused
    
    # Core diagnostics dictionary - USED
    diagnostics = {
        'device': 'ENV-PROBE-X9',
        'timestamp': '2023-11-05T14:32:10Z',
        'status': '  Optimal Range Detected  ',
        'confidence': 0.92,
        'version': '2.1.5'
    }
    
    # Raw sensor readings - USED
    raw_sensor_data = [42, 45, 48, 44, 46, 43, 47, 45, 46, 44]
    
    # Multiple irrelevant data structures
    historical_patterns = {
        'week_1': [67, 65, 68],
        'week_2': [70, 72, 69],
        'week_3': [75, 73, 74]
    }
    
    security_tokens = [0xAB, 0xCD, 0xEF, 0x12]  # Bitwise decoy
    access_level = security_tokens[0] | 0x54  # Dead-end computation
    
    # String-based configuration that seems important
    config_header = "HDR|VER=3.2|MODE=ACTIVE|CHK=8F"
    header_parts = config_header.split('|')
    mode_flag = header_parts[2].split('=')[1]  # 'ACTIVE' - unused
    
    # Transform data through multiple functions (some irrelevant)
    processed_signal = transform_signal(raw_sensor_data)
    pattern_analysis = analyze_pattern(raw_sensor_data)
    data_entropy = compute_entropy(raw_sensor_data)
    
    # Decoy sequence decoding
    sequence_code = "12-34-56-78"
    decoded_values = decode_sequence(sequence_code)
    
    # Metadata for flags (distraction)
    meta_tags = ['3a', '7b', '2c', '9d']
    system_flags = extract_flags(meta_tags)
    
    # Filtered readings (used indirectly)
    cleaned_readings = filter_outliers(raw_sensor_data, threshold=1.2)
    
    # Aggregate score (misleading intermediate result)
    aggregate_result = aggregate_readings(raw_sensor_data)
    
    # Stability evaluation (looks important but not used in final)
    is_stable = evaluate_stability(raw_sensor_data)
    
    # CHECKSUM validation (red herring)
    checksum = validate_checksum(raw_sensor_data)
    
    # === CRITICAL EXECUTION POINT ===
    final_diagnostic = process_metrics(diagnostics, raw_sensor_data)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")