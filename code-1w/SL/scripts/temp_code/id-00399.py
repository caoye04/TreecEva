import math

def analyze_pattern(sequence):
    total = 0
    for i in range(len(sequence)):
        if i % 2 == 0:
            total += ord(sequence[i])
        else:
            total -= ord(sequence[i])
    return total

def normalize_value(val):
    if val < 0:
        return abs(val) * 1.5
    return val / 2

def validate_entry(key, value):
    if len(key) > 3 and value.isdigit():
        return True
    return False

def calculate_entropy(values):
    entropy = 0.0
    for v in values:
        if v > 0:
            entropy -= v * math.log(v)
    return round(entropy, 4)

def transform_data(raw):
    transformed = []
    for item in raw:
        if isinstance(item, str):
            transformed.append(item.upper().replace('X', '0'))
        elif isinstance(item, int):
            transformed.append(item ^ 7)
    return transformed

def process_metrics(log, cfg):
    temp_result = 0
    adjustment = 0
    flag_mode = False

    # Irrelevant string processing (distractor)
    metadata_keys = [k.upper() for k in cfg.keys() if 'mode' in k]
    mode_count = len(metadata_keys)
    if mode_count > 1:
        flag_mode = True
    
    # Real logic begins: count valid entries
    valid_entries = 0
    for k, v in log.items():
        if validate_entry(k, v):
            valid_entries += 1

    # Bit manipulation chain (partially relevant)
    base_shift = valid_entries << 2
    mask = 0b1101
    masked = base_shift & mask

    # String-based interference
    key_string = ''.join([k[0] for k in log.keys()])
    analyzed = analyze_pattern(key_string)

    # Distractor: unused entropy calculation
    dummy_probs = [0.1, 0.2, 0.7]
    entropy_val = calculate_entropy(dummy_probs)  # Not used

    # Core arithmetic path
    intermediate = (masked * 3) + abs(analyzed)
    if intermediate % 2 == 0:
        adjustment = normalize_value(intermediate)
    else:
        adjustment = normalize_value(intermediate + 1)

    # Data transformation side path (distractor)
    raw_mixed = ['abc', 123, 'xyz', 456]
    transformed_list = transform_data(raw_mixed)  # Unused

    # Final computation
    final_score = int(adjustment + valid_entries)

    # Dead code branch (never executed due to flag_mode=False)
    if flag_mode:
        fallback = 0
        for t in transformed_list:
            if isinstance(t, str):
                fallback += len(t)
        final_score += fallback

    return final_score

# Main execution
config = {
    'debug_mode': True,
    'safe_mode': False,
    'timeout': 30
}

data_log = {
    'user_id': '12345',
    'token': 'valid',
    'ref': 'A1',
    'src': 'B2',
    'note': 'temp'
}

final_score = process_metrics(data_log, config)
print(f"Result: {final_score}")