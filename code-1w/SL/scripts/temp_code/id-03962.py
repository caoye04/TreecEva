def analyze_sensor(state_code, readings):
    if len(readings) == 0:
        return 0
    avg = sum(readings) / len(readings)
    normalized = [r / avg for r in readings if r > 0]
    state_flag = state_code.upper() == 'ACTIVE'
    adjustment = 1.5 if 'CALIBRATED' in state_code else 0.8
    temp_result = 0
    for i, val in enumerate(normalized):
        if i % 2 == 0:
            temp_result += val * adjustment
        else:
            temp_result -= val

    # Irrelevant transformation chain (distractor)
    encoded = ''.join([chr(int(abs(v * 10)) % 26 + 97) for v in normalized[:3]])
    reversed_encoded = encoded[::-1]
    case_swapped = reversed_encoded.swapcase()
    length_score = len(case_swapped) * 0.3

    # Dead logic path (never executed due to prior condition)
    if len(normalized) > 100:
        backup = sum(normalized) ** 0.5
        temp_result = max(temp_result, backup)

    return abs(int(temp_result))


def validate_entry(record):
    # Unused validation function (decoy)
    return record.get('status') == 'APPROVED' and record.get('version', 0) >= 2


def merge_diagnostics(a, b, mode='fast'):
    # Misleading intermediate function with unused modes
    if mode == 'deep':
        return (a * b) + (a + b)
    elif mode == 'safe':
        return a if a < b else b
    else:
        return a + (b // 2)

# Complex data setup with red herrings
baseline_offsets = {k: (k**2 % 7) for k in range(1, 10)}
calibration_lookup = {
    'X1': lambda x: x * 1.05,
    'Y2': lambda x: x * 0.98,
    'Z3': lambda x: x + (x * 0.02)
}

# Irrelevant set operations (distractor)
duplicate_filters = set(['ERR', 'NA', 'NULL'])
temp_flags = set(['INIT', 'RUNNING', 'PAUSED'])
active_modes = duplicate_filters.union(temp_flags).difference(['ERR'])
mode_priority = {mode: idx for idx, mode in enumerate(active_modes)}

# Real input data mixed with noise
collected_data = [
    {'sensor_id': 'A1', 'state': 'ACTIVE_CALIBRATED', 'values': [4.2, 3.8, 4.0, 4.5]},
    {'sensor_id': 'B2', 'state': 'STANDBY', 'values': [1.1, 1.3]},
    {'sensor_id': 'C3', 'state': 'ACTIVE', 'values': [5.5, 5.7, 5.3]},
    {'sensor_id': 'D4', 'state': 'CALIBRATED', 'values': [2.0, 2.1, 1.9, 2.2, 2.05]}
]

threshold_map = {
    'high_risk': 4.0,
    'medium_risk': 2.5,
    'low_risk': 1.0
}

# Unused bit manipulation chain (red herring)
config_word = 0b110101
mask = 0b111000
masked_config = config_word & mask
shifted = (masked_config << 3) | (masked_config >> 2)
parity_check = bin(shifted).count('1') % 2

# Real processing function that matters
def process_readings(data_list, thresholds):
    results = []
    high_threshold = thresholds['high_risk']
    for entry in data_list:
        sensor_state = entry['state']
        values = entry['values']
        # Only ACTIVE or CALIBRATED states contribute meaningfully
        relevant = 'ACTIVE' in sensor_state or 'CALIBRATED' in sensor_state
        if not relevant:
            continue
        
        # Compute base diagnostic using analyze_sensor
        base_diag = analyze_sensor(sensor_state, values)
        
        # Apply conditional multiplier based on value thresholds
        over_high = sum(1 for v in values if v > high_threshold)
        multiplier = 1.0
        if over_high >= 2:
            multiplier = 1.75  # significant event
        elif over_high == 1:
            multiplier = 1.25
            
        adjusted_diag = base_diag * multiplier
        results.append(adjusted_diag)
        
        # Early termination if critical pattern found (real early return)
        if len(values) >= 4 and base_diag > 3 and 'CALIBRATED' in sensor_state:
            break
    
    # Final aggregation with logical condition
    if not results:
        return -1
    
    aggregate = sum(results)
    final_bit_shift = int(aggregate) ^ 0b1010  # XOR with constant
    
    # Spurious string operation (distractor)
    hex_rep = format(final_bit_shift, 'x')
    padded_hex = hex_rep.zfill(8)
    inverted_hex = padded_hex[::-1]
    
    # The real answer derivation
    correction_factor = 0.9 if len(results) > 2 else 1.0
    final_diagnostic = int(aggregate * correction_factor)
    
    # Dead code: never reached due to earlier logic
    if final_diagnostic < 0:
        fallback_map = {i: i**3 for i in range(3)}
        final_diagnostic = fallback_map.get(abs(final_diagnostic), 1)
        
    return final_diagnostic

# Execution point of interest
final_diagnostic = process_readings(collected_data, threshold_map)

# Output the target result
print(f"Target result: {final_diagnostic}")