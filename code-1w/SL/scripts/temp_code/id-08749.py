def transform_sequence(seq, factor):
    # Irrelevant transformation function (dead code path)
    return [x * factor + 2 for x in seq if x % 2 == 0]

import math

def extract_features(signal):
    # Distractor: advanced signal processing that isn't actually used
    magnitude = sum([abs(x) for x in signal])
    norm = math.sqrt(sum([x**2 for x in signal]))
    phase = [math.atan2(x, 1) for x in signal][:3]
    return {'mag': magnitude, 'norm': norm, 'phase': phase}

def filter_outliers(data, limit=100):
    # This function is called but its result is not used
    cleaned = [x for x in data if abs(x) < limit]
    return cleaned

def parse_sensor_string(raw):
    # Uses string methods – required language feature
    raw = raw.strip().lower()
    parts = raw.split(',')
    codes = [p.strip().replace('-', '').zfill(3) for p in parts]
    return [int(c) for c in codes if c.isdigit()]

def validate_checksum(values):
    # Bit manipulation red herring
    checksum = 0
    for v in values:
        checksum ^= v
        checksum = (checksum << 1) % 256
    return checksum % 16 == 0

def normalize_readings(arr):
    min_val, max_val = min(arr), max(arr)
    if max_val == min_val:
        return [0.5 for _ in arr]
    return [(x - min_val) / (max_val - min_val) for x in arr]

def aggregate_windows(data, size=3):
    # Unused data transformation (distractor)
    aggregated = []
    for i in range(0, len(data) - size + 1):
        window = data[i:i+size]
        aggregated.append(sum(window) / len(window))
    return aggregated

def decode_thresholds(flag_str):
    # Processes string to produce threshold map (used later)
    chars = list(flag_str.replace(' ', '').encode('ascii'))
    # Only uses even-positioned characters
    filtered = [c for i, c in enumerate(chars) if i % 2 == 0]
    # Thresholds derived from character values
    t_map = {
        't1': sum(filtered[::3]) % 15 + 5,
        't2': sum(filtered[1::3]) % 20 + 10,
        't3': sum(filtered[2::3]) % 25 + 15
    }
    return t_map

def process_raw_input(raw_data, config):
    # Main processing chain with relevant logic buried in distractions
    stage1 = [x * config['gain'] for x in raw_data]
    
    # Apply non-linear correction (relevant)
    stage2 = [math.log(abs(x) + 1) * 10 for x in stage1]
    
    # Normalize between 0 and 1 (relevant)
    normalized = normalize_readings(stage2)
    
    # Simulate quantization (relevant)
    quantized = [int(x * 1000) / 1000 for x in normalized]
    
    # Introduce irrelevant intermediate variables
    stats = {
        'avg': sum(quantized) / len(quantized),
        'peak': max(quantized),
        'variance': sum((x - quantized[0])**2 for x in quantized[:5])
    }
    
    # Add decoy operation on strings
    tag = "Q9X-2M7-N1P"
    parsed_tag = parse_sensor_string(tag)
    
    # Filter but don't use result — misleading call
    filtered_main = filter_outliers(quantized, limit=0.8)
    
    # Final processed output
    return [x * 100 for x in quantized]  # Amplify for analysis

def analyze_readings(readings, thresholds):
    # Core analysis logic (target)
    count_a = sum(1 for x in readings if x > thresholds['t1'])
    count_b = sum(1 for x in readings if x > thresholds['t2'])
    count_c = sum(1 for x in readings if x > thresholds['t3'])
    
    # Complex weighting scheme
    score = (count_a * 7) + (count_b * 11) + (count_c * 13)
    adjustment = abs(count_a - count_b) * 2
    
    # Final diagnostic calculation
    if count_c > 2:
        adjustment += 15
    else:
        adjustment -= 5
    
    # Decoy bit operation with no impact
    decoy_flag = (score & adjustment) >> 2
    decoy_flag = decoy_flag ^ (decoy_flag << 1)
    
    final_score = score - adjustment + decoy_flag
    
    # Additional red herring: unused set operation
    unique_contributions = set([count_a, count_b, count_c, adjustment])
    if len(unique_contributions) > 3:
        final_score += 1  # Never reached due to logic above
    
    return final_score

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # Raw sensor input (simulated)
    raw_input_stream = [-2.3, 4.7, 6.1, 3.2, 8.9, 1.0, 7.4, 5.6, 9.2, 2.8]
    
    # Configuration with plausible but partially unused fields
    system_config = {
        'gain': 1.8,
        'sampling_rate': 100,
        'mode': 'high_resolution'
    }
    
    # Parse threshold configuration from string
    threshold_source = "k3 m9 p4 z2 x6"
    threshold_map = decode_thresholds(threshold_source)
    
    # Process the raw data
    processed_data = process_raw_input(raw_input_stream, system_config)
    
    # DEAD FUNCTION CALL: transforms but result ignored
    dummy_sequence = transform_sequence([1,2,3,4,5], 7)
    
    # Extract features (computationally heavy but unused)
    unused_features = extract_features(processed_data)
    
    # Aggregate windows (computed but not used)
    window_summary = aggregate_windows(processed_data, size=4)
    
    # Validate checksum on unrelated data (distractor)
    fake_data_ids = [101, 203, 405, 807]
    is_valid = validate_checksum(fake_data_ids)
    
    # Critical statement
    final_diagnostic = analyze_readings(processed_data, threshold_map)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")