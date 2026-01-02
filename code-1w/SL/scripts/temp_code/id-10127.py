import math

# Simulated sensor array data processing with diagnostic evaluation
def collect_sensor_readings():
    raw_samples = [127, 255, 64, 192, 32, 180, 95, 220]
    scaling_factor = 0.75
    adjusted = [x * scaling_factor for x in raw_samples]
    return adjusted

# Irrelevant auxiliary function - dead code path
def legacy_compatibility_mode():
    checksum = 0
    for i in range(100):
        checksum += (i * 2) % 7
    return checksum  # Never used

# Signal preprocessing with noise filtering
def preprocess(signal_chunk, mode='standard'):
    filtered = []
    noise_floor = 45.0
    for val in signal_chunk:
        if val > noise_floor:
            normalized = val / (1 + math.log(val))
            if 'high' in mode:
                normalized *= 1.2
            filtered.append(round(normalized, 3))
    return filtered

# Misleading intermediate transformation
def compute_legacy_metrics(data_stream):
    stats = {}
    total = sum(data_stream)
    stats['peak'] = max(data_stream) if data_stream else 0
    stats['entropy'] = len(data_stream) * 0.693
    stats['phantom_index'] = (total * 17) % 997
    return stats  # Computed but not used in final logic

# Core analysis logic
def generate_threshold_map(config_level):
    base_levels = {'low': 30, 'medium': 45, 'high': 60}
    extra_offsets = [5, -2, 8, 0, 3]
    offset_sum = sum([x for x in extra_offsets if x > 0]) - config_level
    dynamic_map = {}
    for k, v in base_levels.items():
        dynamic_map[k] = v + offset_sum
    return dynamic_map

# Data integrity verification - red herring
def validate_checksum(structure):
    if isinstance(structure, list):
        check = 0
        for i, x in enumerate(structure):
            check ^= int(x) ^ i
        return check == 127  # Unrelated to main result
    return False

# Main diagnostic engine
def analyze_signal(dataset, thresholds):
    if not dataset:
        return -1
    
    # Complex conditional aggregation
    high_activity = 0
    medium_activity = 0
    for reading in dataset:
        if reading > thresholds['high']:
            high_activity += 1
        elif reading > thresholds['medium']:
            medium_activity += 1

    # Bit manipulation for status encoding
    activity_code = (high_activity << 3) | (medium_activity & 0b111)
    
    # Secondary validation chain
    if len(dataset) >= 5:
        avg = sum(dataset) / len(dataset)
        variation = abs(avg - thresholds['medium'])
        if variation < 10:
            activity_code += 5
        elif variation > 25:
            activity_code -= 3

    # Final adjustment using string-based key (distractor usage)
    key_seed = "diagnostic_5"
    digit = int(key_seed[-1])
    final_score = activity_code * digit
    
    # Additional decoy logic
    temp_buffer = []
    for i in range(5):
        temp_buffer.append((final_score + i) % 25)
    buffer_checksum = sum(temp_buffer) % 100
    
    # Critical execution point
    final_diagnostic = final_score + buffer_checksum // 10
    
    return final_diagnostic

# Orphaned utility function (unused)
def debug_dump_structure(obj):
    if hasattr(obj, '__dict__'):
        return str(obj.__dict__)
    else:
        return str(type(obj))

# Execution flow
if __name__ == "__main__":
    readings = collect_sensor_readings()
    processed_data = preprocess(readings, mode='standard_high')
    
    # Dead computation - irrelevant statistics
    unused_metrics = compute_legacy_metrics(processed_data)
    
    # Generate actual required threshold map
    threshold_map = generate_threshold_map(config_level=2)
    
    # Validate structure (result ignored)
    is_valid = validate_checksum(processed_data)
    
    # Key statement
    final_diagnostic = analyze_signal(processed_data, threshold_map)
    
    # Print target result
    print(f"Target result: {final_diagnostic}")