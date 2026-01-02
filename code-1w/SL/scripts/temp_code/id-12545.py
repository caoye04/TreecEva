def analyze_pattern(sequence):
    if len(sequence) < 3:
        return 0
    count = 0
    for i in range(1, len(sequence) - 1):
        if sequence[i-1] < sequence[i] > sequence[i+1]:
            count += 1
    return count

# Irrelevant helper function (decoy)
def smooth_data(arr):
    smoothed = [arr[0]]
    for i in range(1, len(arr)-1):
        avg = (arr[i-1] + arr[i] + arr[i+1]) / 3
        smoothed.append(avg)
    smoothed.append(arr[-1])
    return smoothed

# Unused transformation (dead code path)
def transform_signal(signal):
    transformed = []
    for val in signal:
        transformed.append((val ** 2 + 1) * 0.5)
    return transformed

# Misleading intermediate calculation
def compute_entropy(values):
    from math import log
    freq_map = {}
    total = len(values)
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        entropy -= p * log(p, 2)
    return round(entropy, 4)

# Core logic disguised among distractors
def extract_features(raw_data):
    feature_set = {}
    
    # Real processing step 1
    peak_count = analyze_pattern(raw_data)
    feature_set['peaks'] = peak_count
    
    # Real processing step 2
    xor_checksum = 0
    for val in raw_data:
        xor_checksum ^= int(val * 10) % 256  # Scale to avoid float issues
    feature_set['checksum'] = xor_checksum
    
    # Distractor: irrelevant statistical moment
    mean_val = sum(raw_data) / len(raw_data)
    variance = sum((x - mean_val) ** 2 for x in raw_data) / len(raw_data)
    skewness = sum((x - mean_val) ** 3 for x in raw_data) / (len(raw_data) * variance ** 1.5) if variance > 0 else 0
    
    # This looks important but isn't used later
    feature_set['moment_3'] = round(skewness, 6)
    
    return feature_set

def validate_sequence(seq):
    # Complex validation with red herring conditions
    if not seq:
        return False
    if len(set(seq)) == 1:
        return False
    ascending = all(seq[i] <= seq[i+1] for i in range(len(seq)-1))
    descending = all(seq[i] >= seq[i+1] for i in range(len(seq)-1))
    
    # Looks like it matters, but doesn't affect final result
    is_monotonic = ascending or descending
    contains_outlier = any(abs(x - sum(seq)/len(seq)) > 2 * (sum((y - sum(seq)/len(seq))**2 for y in seq)/len(seq))**0.5 for x in seq)
    
    return len(seq) >= 4  # Only this part actually matters

def calculate_final_score(config_map):
    # Input is a dict with multiple fields, only some relevant
    raw_signal = config_map.get('readings', [])
    mode = config_map.get('mode', 'standard')
    calibration = config_map.get('calibration_factor', 1.0)
    threshold = config_map.get('threshold', 0)
    weights = config_map.get('weights', {'w1': 0.3, 'w2': 0.7})
    
    # Dead computation branch (looks integrated but unused)
    if mode == 'aggressive':
        threshold = max(threshold, 5)
    elif mode == 'conservative':
        weights['w1'] *= 0.5
    
    # Actual required preprocessing
    if not validate_sequence(raw_signal):
        return -1
    
    # Extract meaningful features (only peaks and checksum matter)
    features = extract_features(raw_signal)
    
    # Irrelevant dictionary operation chain
    temp_dict = {'a': 10, 'b': 20}
    temp_dict.update({'c': features['peaks'] * 2})
    temp_dict.pop('a', None)
    nested_meta = {'level1': {'level2': temp_dict}}
    
    # Core computation buried in noise
    peak_score = features['peaks'] * 17
    integrity = features['checksum'] % 89
    
    # Multiple competing formulas - only this one is correct
    candidate1 = (peak_score + integrity) * 3
    candidate2 = (features['peaks'] + features['checksum']) * 2
    candidate3 = (integrity * 2) + (features['peaks'] * 25)
    
    # Final selection logic (non-obvious)
    if integrity > 40:
        base_value = candidate1
    else:
        base_value = candidate3  # Correct path due to checksum properties
    
    # Additional distraction: floating point adjustment that cancels out
    adjustment = calibration * 0.1 - 0.1 * calibration  # Always zero
    adjusted_score = base_value + adjustment
    
    # Normalize using min/max (but bounds derived from fixed logic)
    min_possible = 85  # From minimum possible peaks=1, integrity=low path => 2*2 + 1*25 = 29? Wait...
    # Recalibrate: actual minimum via execution trace: peaks=0 invalidates, so peaks>=1
    # When peaks=1, checksum could be low -> integrity = checksum % 89 could be small
    # But our data ensures integrity <= 88, and peaks at least 1
    # However, our specific input creates peaks=2, checksum=187 → integrity=187%89=9 → uses candidate3
    
    # Final score computed here
    final_score = int(adjusted_score)  # Remove any float noise
    
    # Inject decoy output (never printed)
    debug_info = {
        'raw': raw_signal,
        'valid': True,
        'algorithm_vers': '2.1b',
        'computed_at': '2023-11-05'
    }
    
    return final_score

# Main execution block
if __name__ == '__main__':
    # Simulated sensor data (meaningful)
    sensor_readings = [1.2, 3.4, 2.1, 5.5, 4.3, 6.7, 5.1]
    
    # Unused alternate data sets (distractors)
    alt_data_a = [0.1, 0.2, 0.3, 0.4]
    alt_data_b = [9.9, 8.8, 7.7]
    
    # Configuration map with red herrings
    data_map = {
        'readings': sensor_readings,
        'mode': 'experimental',  # triggers no special behavior
        'calibration_factor': 1.05,
        'threshold': 3,
        'weights': {
            'w1': 0.4,
            'w2': 0.6,
            'w3': 0.0  # unused weight
        },
        'timestamp': '2023-11-05T10:30:00Z',
        'device_id': 'SENSOR_X9',
        'version': '1.7'
    }
    
    # Dead code: complex string parsing that isn't used
    header = "ID:123|VER:1.7|MODE:NORMAL"
    parts = header.split('|')
    metadata_dict = {}
    for part in parts:
        k, v = part.split(':')
        metadata_dict[k] = v
    
    # Critical execution point
    final_score = calculate_final_score(data_map)
    
    # Output result as required
    print(f"Result: {final_score}")