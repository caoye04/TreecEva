def preprocess_inputs(raw_values):
    # Irrelevant preprocessing step
    normalized = [x * 0.95 for x in raw_values if x > 0]
    adjusted = [x + 10 for x in normalized if x < 50]
    return adjusted if adjusted else [0]


def validate_entry(key, value):
    # Misleading validation that isn't actually used
    if not isinstance(key, str) or len(key) == 0:
        return False
    if value < -100 or value > 1000:
        return False
    return True


def transform_sequence(seq):
    # Distractor function: transforms but result unused
    shifted = []
    for i, val in enumerate(seq):
        if i % 2 == 0:
            shifted.append(val << 2)
        else:
            shifted.append(val >> 1)
    return shifted


def calculate_metrics(cache_dict):
    # Partially relevant computation with red herrings
    temp_results = []
    running_total = 0
    bonus_flag = False

    for k, v in cache_dict.items():
        if k.startswith('tmp'):
            continue  # Skip irrelevant keys
        if 'offset' in k:
            running_total -= v
        elif 'factor' in k:
            running_total += v * 2
        elif k == 'base':
            running_total += v
        elif k == 'flag' and v == 1:
            bonus_flag = True

    if bonus_flag:
        running_total += 100  # Unused bonus logic

    temp_results.append(running_total)
    temp_results.append(len(cache_dict))
    return temp_results


def calculate_final_score(data_map):
    score = 0
    
    # Core logic embedded in noise
    config_weights = {'w1': 3, 'w2': 7, 'w3': 2}
    default_offsets = [5, -3, 8]
    
    # Real computation begins
    base_value = data_map.get('base', 0)
    multiplier = data_map.get('multiplier', 1)
    score += base_value * multiplier
    
    factors = data_map.get('factors', [])
    if len(factors) >= 2:
        score += factors[0] * config_weights['w1']
        score -= factors[1] * config_weights['w3']

    flags = data_map.get('flags', {})
    if flags.get('enable_boost') and score > 50:
        score *= 1.1
    
    # Critical dictionary operation
    audit_log = {}
    for key, val in data_map.items():
        if isinstance(val, int) and val % 2 == 1:
            audit_log[key] = val * 2
    
    # Only this part affects final output
    correction_factor = 0
    if 'correction' in data_map and data_map['correction'] != 0:
        correction_factor = 100 // abs(data_map['correction'])
        if data_map['correction'] < 0:
            correction_factor = -correction_factor
    
    score += correction_factor
    
    # Dead code path - never reached due to logic above
    if score < 0 and 'invalid' in audit_log:
        reset_token = sum(audit_log.values())
        score = reset_token // 10
    
    # Final adjustment based on key existence
    if 'special_case' in data_map and data_map['special_case'] is True:
        score += 5

    return score

# Main execution
raw_data = [10, -5, 100]
unused_transformation = transform_sequence([4, 8, 15, 16])
dummy_validation = validate_entry('test_key', 42)

# Build input map with multiple distractions
input_map = {
    'base': 42,
    'multiplier': 3,
    'factors': [5, 4],
    'flags': {'enable_boost': True},
    'tmp_ignored': 999,
    'offset_x': 10,
    'offset_y': 5,
    'factor_alpha': 7,
    'factor_beta': 14,
    'correction': 25,
    'special_case': True,
    'meta_info': {'version': '2.1', 'debug': False},
    'flag': 1
}

# Preprocessing (unused)
data_buffer = preprocess_inputs(raw_data)

# Actual target computation
interim_metrics = calculate_metrics(input_map)
final_score = calculate_final_score(input_map)

print(f"Result: {final_score}")