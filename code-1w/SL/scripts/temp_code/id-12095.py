import math

# Simulated sensor data processing system for health monitoring
# Many variables are distractions or used in dead paths

def analyze_rhythm(signal):
    if len(signal) < 5:
        return 0
    rhythm_score = 0
    for i in range(1, len(signal)):
        if signal[i] > signal[i-1]:
            rhythm_score += 1
    return rhythm_score // 2

def compute_entropy(data):
    # Unused function - red herring
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return entropy

def validate_pattern(seq):
    # Dead code path - never called
    return all(x in [0,1] for x in seq)

def transform_readings(raw):
    adjusted = []
    for val in raw:
        if val < 0:
            adjusted.append(abs(val) * 1.1)
        elif val == 0:
            adjusted.append(0.5)
        else:
            adjusted.append(math.sqrt(val) + 0.1)
    return [round(x, 2) for x in adjusted]

def generate_baseline(n):
    # Distractor: generates unused baseline data
    base = []
    for i in range(n):
        base.append((i * 0.3) % 2.5)
    return base

def extract_features(data, mode='strict'):
    features = {}
    temp_sum = sum(data)
    temp_avg = temp_sum / len(data)
    
    # Conditional expression (required feature)
    deviation = [(x - temp_avg) ** 2 for x in data]
    variance = sum(deviation) / len(deviation) if len(deviation) > 0 else 0
    
    features['mean'] = temp_avg
    features['variance'] = variance
    features['peak'] = max(data)
    features['threshold_flag'] = features['peak'] > 15
    
    # Complex nested logic with distractors
    if features['variance'] > 2.0:
        if features['mean'] < 10:
            features['class'] = 'A'
        else:
            features['class'] = 'B'
    else:
        features['class'] = 'C' if features['peak'] < 8 else 'D'
    
    return features

def process_metrics(signature, logs):
    # Core computation path
    readings_count = len(logs)
    scale_factor = 1.75 if readings_count > 6 else 0.85
    
    processed = transform_readings(logs)
    stats = extract_features(processed)
    
    # Key intermediate values
    base_score = int(stats['mean'] * 10)
    adjustment = 0
    
    if stats['class'] == 'A':
        adjustment = -5
    elif stats['class'] == 'B':
        adjustment = 3
    elif stats['class'] == 'C':
        adjustment = 7
    else:
        adjustment = 2
    
    rhythm_analysis = analyze_rhythm(logs)
    temporal_weight = rhythm_analysis * 1.5
    
    # Irrelevant computations - red herrings
    dummy_matrix = [[i*j for j in range(3)] for i in range(3)]
    checksum = 0
    for row in dummy_matrix:
        for elem in row:
            checksum += elem
    checksum = checksum % 97  # unused
    
    # Decoy variable with misleading name
    critical_failure_risk = stats['threshold_flag'] and (stats['variance'] > 5)
    emergency_override = False
    
    # Another distraction: unused conditional block
    if critical_failure_risk:
        emergency_override = True
        recovery_attempt = 0
        while recovery_attempt < 3:
            recovery_attempt += 1
    
    # Actual answer derivation chain
    raw_diagnostic = base_score + adjustment + temporal_weight
    
    # Final transformation using conditional expression (required python feature)
    modifier = 1.2 if stats['class'] in ['A','B'] else 0.9
    final_diagnostic = int(raw_diagnostic * modifier)
    
    # Additional irrelevant string manipulation
    log_id = "HMX-" + "-".join(str(int(x)) for x in logs[:3])
    status_label = log_id.lower().replace('-', '_').upper()  # meaningless
    
    # Sorting a set - distraction
    unique_values = list(set(processed))
    unique_values.sort(reverse=True)
    
    # Grouping by magnitude (unused result)
    groups = {"low": [], "med": [], "high": []}
    for v in processed:
        if v < 1.0:
            groups["low"].append(v)
        elif v < 2.0:
            groups["med"].append(v)
        else:
            groups["high"].append(v)
    
    return final_diagnostic

# Main execution flow
sensor_ids = [101, 102, 103, 104]
config_flags = {"debug": False, "safe_mode": True, "calibrated": False}

# Real input data
health_signature = [0.8, 1.2, 0.9, 1.5, 2.1, 1.8, 0.7]
readings = [4, -2, 9, 16, 0, 25, 36, 1, 49]  # Used in actual computation

# Unused but plausible-looking initialization
baseline_ref = generate_baseline(len(readings))
analysis_cache = {}
temp_record = {}

# Core call that produces the answer
final_diagnostic = process_metrics(health_signature, readings)

# Output result as required
print(f"Result: {final_diagnostic}")