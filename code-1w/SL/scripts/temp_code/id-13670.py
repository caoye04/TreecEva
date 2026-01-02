def sensor_calibration(raw_values):
    calibrated = []
    offset = 0.987
    gain = 1.013
    for v in raw_values:
        corrected = (v * gain) + offset
        if corrected > 100:
            corrected = 98.5  # artificial cap (distractor)
        calibrated.append(corrected)
    return calibrated

raw_sensor_data = [45.2, 67.8, 33.1, 92.4, 76.5]

# Irrelevant transformation chain (dead path)
def transform_legacy(data):
    return [x * 0.89 for x in data if x > 50]

legacy_output = transform_legacy(raw_sensor_data)  # unused

# Another decoy: checksum that looks important but isn't used
def compute_checksum(arr):
    cs = 0
    for i, val in enumerate(arr):
        cs += int(val) * (i + 1)
    return cs % 1024

checksum = compute_checksum(raw_sensor_data)  # computed but irrelevant

# Real processing begins
baseline_adjusted = [x - 32.0 for x in raw_sensor_data]
processed_data = sensor_calibration(baseline_adjusted)

# String-based filtering logic (uses string method)
def get_flag_category(value):
    if value < 40:
        return 'LOW_TEMP'.lower()
    elif value > 80:
        return 'HIGH_TEMP'.upper()
    else:
        return 'NORMAL_RANGE'.strip('GE')  # distractor usage of strip

# Complex control flow with early returns and red herrings
def validate_entry(record, rules):
    if not record:
        return False
    if 'ERR' in str(record):
        return False
    if len(str(record)) == 0:
        return False
    return True  # always true for valid numbers

# Decoy data structure
diagnostic_log = {
    'status': 'pending',
    'errors': [],
    'metadata': {'version': '2.1', 'mode': 'test'},
    'history': []
}

diagnostic_log['history'].append('init_phase_complete')  # misleading side effect

# Core analysis function with nested logic
def analyze_readings(readings, limit):
    count_valid = 0
    temp_sum = 0.0
    flagged = []
    category_map = {}

    for idx, val in enumerate(readings):
        # Distractor: string conversion and manipulation
        str_val = str(val)
        if '.' in str_val:
            decimal_part = str_val.split('.')[1]
            if len(decimal_part) > 2:
                rounded = round(val, 2)
            else:
                rounded = val
        else:
            rounded = val

        # Actual filtering logic hidden among noise
        if rounded >= limit:
            count_valid += 1
            temp_sum += rounded

        # Flagging logic with string comparison
        flag = get_flag_category(rounded)
        if flag.startswith('low') or flag.endswith('range'):
            flagged.append(idx)

        # Meaningless accumulation (red herring)
        key = f"item_{idx % 3}"
        if key not in category_map:
            category_map[key] = 0
        category_map[key] += 1

    # Critical computation buried in distractions
    if count_valid == 0:
        average_valid = 0.0
    else:
        average_valid = temp_sum / count_valid

    # Secondary metric disguised as primary
    pseudo_score = (temp_sum * 1.05) - (len(flagged) * 2.1)  # looks important

    # Real answer derivation
    stability_index = len(readings) - len(flagged)
    final_metric = int(average_valid + stability_index)  # key result

    # Early exit that never triggers (misleading)
    if 'ABORT' in category_map.keys():
        return -999

    return final_metric

threshold = 65.0
final_diagnostic = analyze_readings(processed_data, threshold)
print(f"Result: {final_diagnostic}")