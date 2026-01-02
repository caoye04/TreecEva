from collections import defaultdict, Counter

# Simulated sensor data with noise and metadata
def get_sensor_data():
    raw = [
        (100, 'temp', 'A'), (205, 'pressure', 'B'), (98, 'temp', 'A'),
        (512, 'flow', 'C'), (102, 'temp', 'A'), (198, 'pressure', 'B'),
        (488, 'flow', 'C'), (101, 'temp', 'A'), (210, 'pressure', 'B'),
        (505, 'flow', 'C'), (99, 'temp', 'A'), (495, 'flow', 'C')
    ]
    return raw

# Irrelevant utility: converts units but not used in main logic
def convert_units(value, from_unit, to_unit):
    if from_unit == 'kPa' and to_unit == 'psi':
        return value * 0.145038
    return value

# Decoy function: looks important but unused
def analyze_trend(data_list):
    sorted_vals = sorted(data_list)
    median = sorted_vals[len(sorted_vals) // 2]
    deviation = sum(abs(x - median) for x in sorted_vals)
    return {'median': median, 'total_dev': deviation}

# Auxiliary transformation: splits string representations (distractor)
def encode_label(category, source_id):
    encoded = f'{category[0].upper()}{source_id}X'
    return ''.join([chr(ord(c) + 1) for c in encoded])  # meaningless shift

# Core filtering logic
def filter_by_mode(data, mode):
    result = []
    count_map = defaultdict(int)
    
    for val, cat, src in data:
        count_map[cat] += 1
        if cat == mode and val > 0:
            result.append(val)
    
    # Distractor computation: counts per source (not used later)
    src_counter = Counter()
    for _, _, src in data:
        src_counter[src] += 1
    
    temp_str = "sensor.data.stream"
    segments = temp_str.split('.')
    joined = '-'.join(segments)  # irrelevant string manipulation
    fragment = joined[7:11]  # slicing red herring
    
    return result

# Secondary processing: applies correction factors (some paths are dead)
def apply_correction(values, correction_type='linear'):
    corrected = []
    base_factor = 1.0
    
    if correction_type == 'linear':
        base_factor = 0.98
    elif correction_type == 'quadratic':
        base_factor = 0.95  # dead branch (never taken)
    else:
        base_factor = 1.0  # dead branch
    
    for v in values:
        adj = v * base_factor
        if adj < 100:  # rare case, never triggers
            adj = 100
        corrected.append(adj)
    
    # Dead code path with early break
    for x in corrected:
        if x > 1000:
            break  # never reached
    
    return [round(c, 2) for c in corrected]

# Main processing with key logic buried among distractions
def process_readings(data_list, limit):
    stats = defaultdict(float)
    total = 0
    count = 0
    
    for item in data_list:
        total += item
        count += 1
        bucket = 'low' if item < 300 else 'high'
        stats[bucket] += 1
    
    avg = total / count if count else 0
    
    # Complex distraction: bit manipulation on hash (irrelevant)
    magic_seed = len(data_list) ^ 255
    magic_shift = (magic_seed << 2) | (magic_seed >> 1)
    checksum = (magic_shift + 77) % 1000
    
    # String-based control flow (misleading)
    flag_code = "ABORT" if avg < 50 else "CONTINUE"
    if "ABORT" in flag_code:
        return -999  # dead path
    
    # Key decision point
    adjustment = 0
    if avg > limit:
        adjustment = 10
    else:
        adjustment = -5
    
    # Multiple assignments and decoy unpacking
    primary, secondary = avg, avg * 0.1
    info_tuple = (primary, secondary, adjustment)
    p, s, a = info_tuple  # unpacking distraction
    
    # Final computation (answer depends only on this)
    diagnostic_score = int(round(avg + a))
    
    # Unused destructuring (distractor)
    sample_data = [(1, 2), (3, 4), (5, 6)]
    x_vals, y_vals = zip(*sample_data)
    
    return diagnostic_score

# Entry point with orchestrated distractions
if __name__ == '__main__':
    # Irrelevant initialization
    system_status = {"active": True, "mode": "diagnostic", "version": "2.1.0"}
    calibration_matrix = [[1, 0], [0, 1]]
    
    # Main data pipeline
    raw_entries = get_sensor_data()
    
    # Filtering for temperature readings only
    filtered_data = filter_by_mode(raw_entries, 'temp')
    
    # Apply correction (uses default argument)
    calibrated = apply_correction(filtered_data)  # not actually used
    
    # Threshold logic
    threshold = 100
    
    # Critical statement
    final_diagnostic = process_readings(filtered_data, threshold)
    
    # Print required result
    print(f"Target result: {final_diagnostic}")