import math

# Simulated sensor network diagnostic system
def analyze_signal_strength(raw_readings):
    normalized = {}
    total_power = 0
    for k, v in raw_readings.items():
        if len(k) % 2 == 0:
            normalized[k] = v ** 1.5
        else:
            normalized[k] = v ** 0.8
        total_power += normalized[k]
    average_power = total_power / len(normalized)
    return normalized, average_power

def generate_signature(data_dict):
    # Irrelevant function: generates a string signature (not used in final result)
    keys = ''.join(sorted(data_dict.keys()))
    values = [round(v) for v in data_dict.values()]
    checksum = sum(ord(ch) * i for i, ch in enumerate(keys)) % 1000
    return f'{keys[:5]}-{checksum}-{len(values)}'

def validate_channel_integrity(signal_map, tolerance=0.15):
    # Misleading intermediate validation (unused)
    valid_channels = []
    for channel, power in signal_map.items():
        expected = math.sin(len(channel)) * 100 + 50
        if abs(power - expected) <= tolerance * expected:
            valid_channels.append(channel)
    return valid_channels

def filter_outliers(data, limit=3.0):
    # Computes statistical z-scores and filters extreme values
    values = list(data.values())
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    std_dev = math.sqrt(variance)
    filtered = {k: v for k, v in data.items() if abs((v - mean_val) / (std_dev + 1e-9)) < limit}
    return filtered

def compute_entropy_profile(data):
    # Dead code path: computes entropy but never used
    probabilities = [v / sum(data.values()) for v in data.values()]
    entropy = -sum(p * math.log(p + 1e-9) for p in probabilities)
    category = 'HIGH' if entropy > 1.0 else 'LOW'
    return round(entropy, 4), category

def build_priority_queue(items):
    # Unused priority structure builder (distractor)
    queue = []
    for item in items:
        priority = len(item[0]) * item[1]
        queue.append((priority, item[0]))
    queue.sort(reverse=True)
    return [q[1] for q in queue]

def merge_thresholds(base, override):
    # Complex dictionary merging with precedence rules (actually used)
    merged = base.copy()
    for k, v in override.items():
        if k.endswith('_crit') or v > 75.0:
            merged[k.replace('_crit', '')] = v
    return merged

def decode_transmission_key(token_list):
    # String processing red herring
    joined = ''.join(token_list)
    segments = [joined[i:i+3] for i in range(0, len(joined), 3)]
    rotated = [seg[-1] + seg[:-1] for seg in segments if len(seg) == 3]
    return ''.join(rotated)

def extract_features(config_str):
    # Bit manipulation decoy
    parts = config_str.split('|')
    feature_bits = 0
    for i, part in enumerate(parts):
        if 'ENABLE' in part:
            feature_bits |= (1 << i)
    return feature_bits

def process_readings(clean_data, thresholds):
    # Core processing logic
    results = []
    for sensor_id, reading in clean_data.items():
        base_key = sensor_id.split('_')[0]
        dyn_thresh = thresholds.get(base_key, 40.0)
        if reading > dyn_thresh:
            results.append(reading * 0.75)
        else:
            results.append(reading * 0.2)
    aggregate = sum(results)
    penalty = len([r for r in results if r < 10]) * 2.5
    bonus = len(set([k.split('_')[0] for k in clean_data.keys()])) * 1.75
    return round(aggregate - penalty + bonus, 6)

# Main execution flow
if __name__ == '__main__':
    # Raw input data from sensor grid
    raw_sensor_data = {
        'A1_temp': 68.5, 'B2_humid': 72.3, 'C3_press': 38.9,
        'D4_flow': 85.1, 'E5_vibe': 41.7, 'F6_radar': 29.4,
        'G7_optic': 90.2, 'H8_mag': 33.6
    }

    # Irrelevant configuration token (decoy)
    config_token = ['ENABLE_X|', 'Y|ENABLE_Z', 'ENABLE_W']
    features_enabled = extract_features('|'.join(config_token))

    # Signal analysis with normalization
    processed_readings, avg_power = analyze_signal_strength(raw_sensor_data)

    # Generate unused transmission signature
    sig = generate_signature(processed_readings)

    # Filter outliers based on statistical deviation
    filtered_data = filter_outliers(processed_readings, limit=2.5)

    # Validate channels (result unused - misleading)
    valid_chans = validate_channel_integrity(processed_readings)

    # Entropy profile (dead computation)
    entropy_score, class_label = compute_entropy_profile(filtered_data)

    # Build decoy priority queue
    pairs = list(filtered_data.items())
    prioritized_sensors = build_priority_queue(pairs)

    # Threshold configurations
    default_thresholds = {
        'A1': 45.0, 'B2': 50.0, 'C3': 40.0,
        'D4': 80.0, 'E5': 35.0, 'F6': 30.0,
        'G7': 85.0, 'H8': 35.0
    }
    override_specs = {
        'D4_crit': 78.0, 'G7_crit': 88.0, 'B2_crit': 55.0
    }

    # Merge threshold maps (used in final calculation)
    threshold_map = merge_thresholds(default_thresholds, override_specs)

    # Decode fake transmission key (irrelevant)
    key_fragment = ['abc', 'def', 'ghi']
    tx_key = decode_transmission_key(key_fragment)

    # Critical diagnostic computation
    final_diagnostic = process_readings(filtered_data, threshold_map)

    # Output target result
    print(f"Target result: {final_diagnostic}")