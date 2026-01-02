def transform_signal(raw_values, factor):
    """ Apply non-linear transformation to signal data (distractor) """
    return [int((x ** 1.5) / factor) + 2 for x in raw_values if x > 0]


def validate_checksum(entry):
    """ Validate data entry checksum (dead code path) """
    total = 0
    for i, c in enumerate(entry['id']):
        total += ord(c) * (i + 1)
    return total % 17 == entry['meta']['checksum']


def accumulate_metrics(data_stream):
    """ Accumulate statistical metrics across sensor array (irrelevant) """
    stats = {'mean': 0, 'peak': 0, 'fluctuations': 0}
    values = []
    for item in data_stream:
        val = item.get('reading', 0)
        values.append(val)
        if len(values) > 1 and abs(val - values[-2]) > 3:
            stats['fluctuations'] += 1
    if values:
        stats['mean'] = round(sum(values) / len(values), 2)
        stats['peak'] = max(values)
    return stats


def decode_segments(token_list):
    """ Decode encoded segments using XOR shift (distractor logic) """
    result = []
    for token in token_list:
        decoded = ''
        for i, c in enumerate(token):
            decoded += chr(ord(c) ^ (i % 5 + 3))
        result.append(decoded)
    return result


def extract_features(signal_sequence):
    """ Extract key waveform features using bit analysis """
    feature_set = {}
    for i, val in enumerate(signal_sequence):
        if i % 4 == 0:
            # Use bitwise manipulation to detect harmonic pattern
            shifted = (val << 2) & 0xFF
            toggled = shifted ^ 0b10101010
            parity = bin(toggled).count('1') % 2
            feature_set[f'f_{i}'] = (toggled % 19) + parity
    return feature_set


def normalize_readings(raw_seq, baseline=5):
    """ Normalize sensor readings against dynamic baseline """
    adjusted = []
    for x in raw_seq:
        diff = x - baseline
        if diff > 10:
            adjusted.append(diff // 2)
        elif diff < -10:
            adjusted.append(diff // 3)
        else:
            adjusted.append(diff)
    return adjusted


def filter_anomalies(mapped_data, rules):
    """ Filter out anomalous entries based on rule thresholds """
    cleaned = []
    for k, v in mapped_data.items():
        if k.startswith('sensor'):
            if 'high' in rules and v > rules['high']:
                continue
            if 'low' in rules and v < rules['low']:
                continue
        cleaned.append(v)
    return cleaned


def analyze_readings(features_dict, config_map):
    """ Analyze processed features to generate diagnostic score """
    aggregate = 0
    weight_map = {**config_map, 'f_8': 3, 'f_12': 5}
    for key, value in features_dict.items():
        if key in weight_map:
            aggregate += value * weight_map[key]
        else:
            aggregate -= value
    # Final adjustment using integer division and modulo interaction
    modifier = len(features_dict) // 4
    if aggregate > 0:
        aggregate = (aggregate // (modifier + 1)) + (aggregate % 7)
    return aggregate

# Main execution sequence
if __name__ == '__main__':
    # Simulated raw sensor input (real data chain)
    raw_input = [3, 7, 4, 8, 12, 6, 13, 9, 11, 5]

    # Irrelevant token stream (distractor)
    security_tokens = ['aB3!', 'xZ9@', 'mN2#']
    decoded_parts = decode_segments(security_tokens)

    # Transform signal using non-linear function (red herring)
    transformed = transform_signal(raw_input, 2.0)

    # Normalize readings — this is the actual relevant preprocessing
    normalized = normalize_readings(raw_input, baseline=6)

    # Build intermediate data structure
    temp_mapping = {}
    for idx, val in enumerate(normalized):
        if idx % 2 == 0:
            temp_mapping[f'sensor_{idx}'] = abs(val)
        else:
            temp_mapping[f'aux_{idx}'] = val * 2

    # Extract waveform features using bit operations — critical path
    extracted_features = extract_features(normalized)

    # Define threshold configuration (used later)
    threshold_map = {
        'f_0': 2,
        'f_4': 4,
        'f_8': 3,
        'f_12': 5
    }

    # Additional irrelevant processing (dead metric accumulation)
    telemetry_stream = [{'reading': x, 'ts': i} for i, x in enumerate(raw_input)]
    system_stats = accumulate_metrics(telemetry_stream)

    # Filter valid sensors based on thresholds (partially relevant)
    filtered_vals = filter_anomalies(temp_mapping, {'high': 8, 'low': 1})

    # Final diagnostic depends only on extracted_features and threshold_map
    final_diagnostic = analyze_readings(extracted_features, threshold_map)

    # Print result for evaluation
    print(f"Result: {final_diagnostic}")