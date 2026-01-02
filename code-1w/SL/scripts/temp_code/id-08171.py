import itertools

# Simulated sensor data processing pipeline with diagnostic analysis
raw_readings = [54, 23, 78, 12, 89, 34, 67, 45, 76, 19]

def apply_noise_filter(data, level=1):
    # Irrelevant preprocessing: applies a dummy smoothing (not used in final result)
    filtered = []
    for i in range(len(data)):
        val = sum(data[max(0, i-level):min(len(data), i+level+1)]) // (2*level + 1)
        filtered.append(val)
    return filtered

def generate_frequency_bands(signal):
    # Distractor function: computes FFT-like bins but unused
    bands = {f'band_{i}': 0 for i in range(8)}
    for i, x in enumerate(signal):
        for b in range(8):
            bands[f'band_{b}'] += (x >> b) & 1
    return bands

def compute_entropy(data):
    # Dead code path: calculates Shannon entropy of bit distribution
    flat_bits = ''.join(f'{x:08b}' for x in data)
    from collections import Counter
    counts = Counter(flat_bits)
    total = len(flat_bits)
    entropy = 0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * (p).bit_length()
    return round(entropy, 6)

def extract_features(series):
    # Extracts multiple features, some irrelevant
    features = {
        'mean': sum(series) / len(series),
        'xor_all': 0,
        'peak_count': 0,
        'rolling_xor': 1,
        'pattern_score': 0
    }
    for x in series:
        features['xor_all'] ^= x
    for i in range(1, len(series)-1):
        if series[i] > series[i-1] and series[i] > series[i+1]:
            features['peak_count'] += 1
    # Rolling XOR chain with decay (misleading intermediate)
    acc = series[0]
    for x in series[1:]:
        acc = (acc ^ x) % 17
        features['rolling_xor'] = (features['rolling_xor'] + acc) % 997
    return features

def transform_sequence(seq, key=3):
    # Core transformation: cyclic shift combined with modular arithmetic
    shifted = [(x + key) % 101 for x in seq]
    doubled = [x * 2 for x in shifted]
    return [doubled[i] ^ doubled[-i-1] for i in range(len(doubled))]  # symmetric XOR

def build_threshold_map(keys, base_offset=10):
    # Constructs map that will be partially used
    tmap = {}
    for k in keys:
        tmap[k] = (k * 7 + base_offset) % 50 + 30
        # Some decoy logic
        if tmap[k] % 5 == 0:
            tmap[k] += 1
    return tmap

def detect_anomalies(dataset, limits):
    # Another distractor: detects out-of-bound values
    anomalies = []
    for i, x in enumerate(dataset):
        if x < limits.get('min', 0) or x > limits.get('max', 100):
            anomalies.append(i)
    return anomalies

def recursive_condense(arr):
    # Simple recursion that collapses array via XOR until one element
    if len(arr) == 1:
        return arr[0]
    reduced = []
    for i in range(0, len(arr), 2):
        if i+1 < len(arr):
            reduced.append(arr[i] ^ arr[i+1])
        else:
            reduced.append(arr[i])
    return recursive_condense(reduced)

def analyze_signal(data, thresholds):
    # Critical function: performs final analysis using specific rules
    segment_size = thresholds.get(77, 42) % len(data)
    segments = [data[i:i+segment_size] for i in range(0, len(data), segment_size)]
    
    # Use itertools to generate overlapping pairs (core relevant step)
    paired_sums = []
    for seg in segments:
        if len(seg) > 1:
            pairs = list(itertools.combinations(seg, 2))
            paired_sums.extend([a + b for a, b in pairs])
    
    # Key accumulation
    accumulator = 0
    for val in paired_sums:
        if val % 7 == 0:
            accumulator += val.bit_length()  # use bit length as weight
        elif val % 3 == 0:
            accumulator -= val % 10
    
    # Final adjustment based on global properties
    feature_set = extract_features(data)
    control_flag = feature_set['peak_count'] ^ (len(paired_sums) % 256)
    accumulator ^= control_flag
    
    # Dead branch - never taken due to fixed condition
    if len(data) < 5 and thresholds.get('dummy', False):
        return -999
        
    return accumulator

# --- Execution Pipeline ---

# Step 1: Apply noise filter (result not used - red herring)
filtered_readings = apply_noise_filter(raw_readings, level=2)

# Step 2: Generate frequency bands (unused)
freq_bands = generate_frequency_bands(raw_readings)

# Step 3: Compute entropy (calculated but not used)
entropy_metric = compute_entropy(raw_readings)

# Step 4: Transform the sequence using key=5
target_key = 5
candidate_transform = transform_sequence(raw_readings, key=target_key)

# Step 5: Build threshold map using keys from transformed data
threshold_keys = [candidate_transform[0], candidate_transform[5], 77]
threshold_map = build_threshold_map(threshold_keys, base_offset=15)

# Step 6: Detect anomalies (dead function call - no impact)
anomaly_list = detect_anomalies(candidate_transform, {'min': 20, 'max': 90})

# Step 7: Extract features (partially used later)
feature_summary = extract_features(candidate_transform)

# Step 8: Recursive condense of original data (distractor)
condensed_value = recursive_condense(raw_readings)

# Step 9: Transform again with different key (creates decoy)
decoy_data = transform_sequence(raw_readings, key=8)

# Step 10: The actual critical transformation
transformed_data = transform_sequence(raw_readings, key=7)  # Key difference

# Step 11: Analyze signal using correct data and threshold map
final_diagnostic = analyze_signal(transformed_data, threshold_map)

# Output result
print(f"Result: {final_diagnostic}")