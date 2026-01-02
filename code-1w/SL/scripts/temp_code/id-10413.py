def transform_signal(raw_values, factor):
    """Irrelevant transformation function (dead code path)."""
    return [x * factor + 10 for x in raw_values]


def accumulate_diagnostics(logs):
    """Accumulates log values but not used in main flow."""
    total = 0
    for entry in logs:
        if entry.get('valid'):
            total += entry['value'] * 2
    return total


def extract_features(data_stream):
    """Extract frequency-based features from signal data."""
    features = []
    offset = len(data_stream) // 2
    for i, val in enumerate(data_stream):
        if i % 2 == 0:
            features.append(val ** 2 - offset)
        else:
            features.append(val + offset)
    return features


def validate_readings(readings):
    """Validate sensor readings using dynamic thresholds."""
    results = []
    for i, r in enumerate(readings):
        if i == 0:
            results.append(r > 5)
        elif i == 1:
            results.append(r < 20)
        else:
            results.append(10 <= r <= 15)
    return results


def process_chain(input_seq, mode='strict'):
    """Main processing pipeline with nested logic and distractors."""
    temp_buffer = [x + 3 for x in input_seq if x % 2 != 0]  # Only odd numbers processed
    shift_val = sum(temp_buffer) % 7
    
    # Distractor block: unused intermediate calculation
    dummy_stats = {
        'peak': max(input_seq, default=0),
        'base': min(input_seq, default=0) * 2,
        'ratio': (max(input_seq, default=1) / (min(input_seq, default=1) or 1))
    }
    
    adjusted = []
    for idx, val in enumerate(temp_buffer):
        if idx % 3 == 0:
            adjusted.append(val - shift_val)
        elif idx % 3 == 1:
            adjusted.append(val + shift_val)
        else:
            adjusted.append(val * (shift_val or 1))
    
    # Real processing continues
    secondary = extract_features(adjusted)
    mask = validate_readings(secondary)
    
    filtered = []
    for i, (val, flag) in enumerate(zip(secondary, mask)):
        if flag:
            filtered.append(val * (i + 1))
    
    return filtered if filtered else [0]


def build_threshold_map(keys, base):
    """Build map of thresholds (partially used)."""
    mapping = {}
    for k, b in zip(keys, range(len(keys))):
        mapping[k] = base - b * 2
    return mapping


def analyze_readings(data_points, config):
    """Final analysis using both data and configuration map."""
    score = 0
    key_indices = [1, 3, 4]
    
    # Misleading loop over unused keys
    debug_weights = {'a': 1, 'b': -1, 'c': 2, 'd': 0, 'e': -2}
    for dk in debug_weights:
        score += 1  # Red herring operation
    
    # Actual logic
    for i, pt in enumerate(data_points):
        if i in key_indices and i < len(config.values()):
            conf_val = list(config.values())[i]
            score += pt - conf_val
        elif i % 2 == 0:
            score += pt // (i + 2)

    # Final adjustment based on length
    length_factor = len(data_points) - len(config)
    final_score = score * (length_factor or 1)
    
    return final_score

# Primary execution sequence
sensor_input = [4, 7, 6, 9, 5, 8]

# Unused transformations (distractors)
data_log = [{'id': j, 'value': v*2, 'valid': (v%2==0)} for j, v in enumerate(sensor_input)]
scaled_signal = transform_signal(sensor_input, 1.5)

# Real processing begins
processed_data = process_chain(sensor_input, mode='strict')

keys_used = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
threshold_base = 12
threshold_map = build_threshold_map(keys_used, threshold_base)

# Critical statement
final_diagnostic = analyze_readings(processed_data, threshold_map)

print(f"Target result: {final_diagnostic}")