def transform_signal(raw_values, factor):
    """Apply non-linear transformation to sensor signal (distractor function)"""
    return [x ** 0.5 * factor for x in raw_values if x > 0]


def filter_outliers(dataset, limit):
    """Remove extreme values beyond z-score threshold (unused decoy)"""
    mean_val = sum(dataset) / len(dataset)
    variance = sum((x - mean_val) ** 2 for x in dataset) / len(dataset)
    std_dev = variance ** 0.5
    return [x for x in dataset if abs((x - mean_val) / std_dev) < limit]


def accumulate_segments(data_stream):
    """Accumulate overlapping window sums (irrelevant computation)"""
    windows = []
    for i in range(len(data_stream) - 2):
        windows.append(sum(data_stream[i:i+3]))
    return [w * 0.9 for w in windows]


def decode_pattern(sequence):
    """Attempt to find repeating bit patterns (red herring)"""
    binary_rep = ''.join([bin(int(x))[2:] for x in sequence])
    if '1111' in binary_rep:
        return len(binary_rep) % 7
    return len(set(binary_rep))


def preprocess_readings(raw_input):
    """Valid preprocessing: normalize and slice central region"""
    normalized = [round(x / max(raw_input), 4) for x in raw_input]
    mid_section = normalized[2:-2]  # Slicing operation
    extended = [0.0] * 2 + mid_section + [0.0] * 2
    return extended


def build_threshold_map(keys, base_level=0.3):
    """Create dynamic threshold per category using set logic"""
    categories = set(keys)  # Set operation
    backup_categories = {'A', 'B', 'C', 'D', 'E'}
    active_zones = categories & backup_categories  # Intersection as distractor
    
    alt_map = {k: base_level + 0.1 * (i % 4) for i, k in enumerate(keys)}
    full_map = {}
    for idx, k in enumerate(keys):
        if idx % 3 == 0:
            full_map[k] = base_level + 0.05
        else:
            full_map[k] = base_level + (idx % 5) * 0.07
    return full_map


def analyze_readings(readings, thresholds):
    """Core analysis: compute weighted deviation score"""
    labels = ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8']
    weight_map = {lbl: (i+1)*0.2 for i, lbl in enumerate(labels)}
    
    aggregate = 0.0
    for i, val in enumerate(readings):
        key = labels[i % len(labels)]
        thresh = thresholds.get(key, 0.5)
        weight = weight_map[key]
        if val > thresh:
            aggregate += (val - thresh) * weight
        elif val < thresh * 0.8:
            aggregate -= (thresh * 0.8 - val) * weight * 0.5
    
    temp_snapshot = [readings[i] for i in range(0, len(readings), 2)]
    parity_check = sum(1 for x in temp_snapshot if x > 0.4)
    
    if parity_check > 3:
        aggregate *= 1.15
    
    return round(aggregate, 6)

# Simulated sensor input (real data path)
sensor_input = [12, 45, 32, 67, 43, 78, 39, 50, 30, 18]

# Irrelevant transformations (distractors)
signal_xform = transform_signal(sensor_input, 1.8)
windowed_data = accumulate_segments(sensor_input)
pattern_code = decode_pattern(sensor_input)

# Real processing path
processed_data = preprocess_readings(sensor_input)

# Generate multiple threshold maps (only last one used)
key_list = ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8']
t1_map = build_threshold_map(key_list, 0.1)
t2_map = build_threshold_map(key_list, 0.2)
threshold_map = build_threshold_map(key_list, 0.25)  # Final used map

# Core diagnostic calculation
baseline_score = analyze_readings(processed_data, t1_map)
interim_result = analyze_readings(processed_data, t2_map)
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Print required result
print(f"Result: {final_diagnostic}")