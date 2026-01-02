import math

def analyze_pattern(seq):
    # Irrelevant function - dead code path
    return sum(x ** 2 for x in seq if x > 0)

def validate_checksum(data):
    # Distractor: looks important but unused
    checksum = 0
    for i, val in enumerate(data):
        checksum ^= (val + i) % 256
    return checksum == 42

def decode_sequence(signal):
    # Another decoy transformation
    decoded = []
    for s in signal:
        if s % 3 == 0:
            decoded.append(s // 3)
        elif s % 2 == 0:
            decoded.append(s // 2)
        else:
            decoded.append(s)
    return [x for x in decoded if x % 2 == 1]

def compute_entropy(values):
    # Misleading intermediate calculation
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    entropy = -sum(p * math.log2(p) for p in probs)
    return round(entropy, 4)

def extract_features(timestamps, readings):
    # Uses enumerate and zip — required Python features
    features = []
    for i, (ts, val) in enumerate(zip(timestamps, readings)):
        if i % 3 == 0 and val > 50:
            features.append(ts + val // 10)
        elif i % 4 == 2:
            features.append(val - ts % 7)
    return features

def filter_anomalies(data, limit=100):
    # Red herring filtering logic
    clean = []
    for x in data:
        if 10 <= x < limit:
            clean.append(x)
    return clean[:10]

def process_signals(diag, thresh):
    # Core logic hidden among distractions
    temp_buffer = []
    for idx, (key, values) in enumerate(diag.items()):
        if len(values) >= 3:
            avg = sum(values) / len(values)
            cap = thresh.get(key, 85)
            clamped_avg = min(avg, cap)
            temp_buffer.append(clamped_avg * (idx + 1))
    
    # Key transformation chain
    transformed = [round(t * 1.15) for t in temp_buffer]
    offset = len(temp_buffer) > 2
    adjusted = [t + (i * 2) for i, t in enumerate(transformed)]
    
    # Final computation
    base_score = sum(adjusted)
    penalty = 0
    for t in transformed:
        if t > 90:
            penalty += int(t // 10)
    
    final_output = base_score - penalty
    
    # Unused variables - distractors
    dummy_lookup = {k: v * 2 for k, v in enumerate(['a', 'b', 'c'])}
    shadow_copy = diag.copy()
    temp_string = "processing_complete_v2"
    version_flag = temp_string.endswith('v2') and 'active' or 'legacy'
    
    return int(final_output)

# Main execution block
if __name__ == '__main__':
    # Input data with meaningful names from sensor diagnostics domain
    diagnostics = {
        'sensor_A1': [65, 70, 75, 80],
        'sensor_B2': [50, 55],
        'sensor_C3': [90, 85, 88],
        'sensor_D4': [40, 45, 50, 55, 60]
    }
    
    thresholds = {
        'sensor_A1': 72,
        'sensor_C3': 87,
        'sensor_D4': 58
    }
    
    # Decoy data structures
    audit_log = [(1, 'init'), (2, 'calibrate'), (3, 'run')]
    config_flags = {'debug': False, 'safe_mode': True, 'override': None}
    timing_series = list(range(10, 60, 10))
    metadata_tags = ['SYS_01', 'VER_2.1', 'SECURE']
    tag_lengths = [len(t) for t in metadata_tags]
    
    # Trigger irrelevant functions to mislead reasoning
    dummy_entropy = compute_entropy([10, 20, 30])
    feature_vector = extract_features(timing_series, [55, 60, 65, 70, 75])
    filtered_data = filter_anomalies(feature_vector, limit=60)
    
    # Actual target computation
    final_output = process_signals(diagnostics, thresholds)
    
    # Output result as required
    print(f"Result: {final_output}")