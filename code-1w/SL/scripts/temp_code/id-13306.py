import math

def collect_samples():
    # Simulated sensor readings (relevant data)
    raw_readings = [14.2, 18.7, 15.1, 20.3, 13.9, 16.8, 17.5, 19.0, 15.6, 14.8]
    scaling_factor = 1.05
    adjusted = [x * scaling_factor for x in raw_readings]
    return adjusted

def filter_noise(data):
    # Apply moving average filter (partially relevant)
    filtered = []
    window_size = 3
    for i in range(len(data)):
        if i < window_size - 1:
            filtered.append(data[i])
        else:
            avg = sum(data[i - window_size + 1:i + 1]) / window_size
            filtered.append(avg)
    return filtered

def compute_entropy(values):
    # Irrelevant function – decoy related to information theory
    total = sum(values)
    probabilities = [v / total for v in values if v > 0]
    entropy = -sum(p * math.log(p) for p in probabilities)
    return round(entropy, 4)

def generate_checksum(sequence):
    # Distractor: checksum computation that isn't used in final result
    checksum = 0
    for i, val in enumerate(sequence):
        checksum ^= int(val * 10)  # bitwise XOR hash
    return checksum % 1000

def validate_integrity(arr):
    # Dead code path – never actually called
    return len(arr) % 2 == 0 and sum(arr) > 0

def extract_features(signal):
    # Extract statistical features, some irrelevant
    features = {
        'mean': sum(signal) / len(signal),
        'max_val': max(signal),
        'min_val': min(signal),
        'range': max(signal) - min(signal),
        'median': sorted(signal)[len(signal)//2],
        'variance': sum((x - sum(signal)/len(signal))**2 for x in signal) / len(signal),
        'skew_hint': 'unknown'
    }
    
    # Add red herring computations
    temp_set = {int(x) for x in signal}
    outlier_candidates = {x for x in temp_set if x > 19}
    correction_offset = len(outlier_candidates) * 0.25
    
    # Modify feature using set-derived logic (still not critical)
    if len(outlier_candidates) > 0:
        features['mean'] += correction_offset
    
    return features

def detect_anomalies(seq):
    # Unused anomaly detection – dead-end logic
    anomalies = []
    threshold = sum(seq) / len(seq) + 2 * (sum((x - sum(seq)/len(seq))**2 for x in seq)/len(seq))**0.5
    for x in seq:
        if abs(x - threshold) > 5:
            anomalies.append(x)
    return anomalies

def analyze_readings(readings):
    # Core transformation: map to categories based on thresholds
    categories = []
    for val in readings:
        if val < 15.0:
            categories.append('LOW')
        elif val < 18.0:
            categories.append('NORMAL')
        elif val < 20.0:
            categories.append('ELEVATED')
        else:
            categories.append('HIGH')
    
    # Use dictionary to count category frequencies (key step)
    freq_map = {}
    for cat in categories:
        freq_map[cat] = freq_map.get(cat, 0) + 1
    
    # Determine dominant category (most frequent)
    dominant = max(freq_map, key=lambda k: freq_map[k])
    
    # Compute secondary metric: normalized spread index (distractor but looks important)
    mean_val = sum(readings) / len(readings)
    spread = sum(abs(x - mean_val) for x in readings)
    normalization_factor = len(readings) * 10
    spread_index = spread / normalization_factor
    
    # Mapping logic with hidden rule: each category has a weight
    weights = {'LOW': -10, 'NORMAL': 5, 'ELEVATED': -20, 'HIGH': -50}
    score = 0
    for cat, count in freq_map.items():
        score += weights[cat] * count
    
    # Final decision tree based on score thresholds
    if score <= -100:
        diagnosis = 404
    elif score <= -50:
        diagnosis = 802
    elif score < 0:
        diagnosis = 132
    else:
        diagnosis = 999
    
    # Red herring: modify diagnosis with spread_index?
    # NO – this branch is logically unreachable due to integer truncation
    if isinstance(spread_index, float) and spread_index > 1.0:
        diagnosis = int(diagnosis / (spread_index + 1))
    
    # Another distraction: use set difference on category keys
    expected_cats = {'LOW', 'NORMAL', 'ELEVATED', 'HIGH'}
    present_cats = set(freq_map.keys())
    missing = expected_cats - present_cats
    penalty = len(missing) * 10
    
    # But penalty is NOT applied – just computed
    
    return diagnosis

# Main execution flow
raw_signals = collect_samples()
processed_signals = filter_noise(raw_signals)

# Extraneous operations
feature_summary = extract_features(processed_signals)
entropy_value = compute_entropy([int(x) for x in processed_signals])
checksum_value = generate_checksum(processed_signals)

# Critical statement
final_diagnostic = analyze_readings(processed_signals)

Result: {final_diagnostic}