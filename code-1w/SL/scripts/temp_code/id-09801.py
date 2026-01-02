def sensor_validation(readings):
    if not readings:
        return False
    valid_count = sum(1 for r in readings if 10 <= r <= 95)
    return valid_count >= len(readings) * 0.75

def normalize(value, min_val=10, max_val=95):
    return max(min_val, min(value, max_val))

def compute_entropy(data):
    from math import log2
    freq = {}
    total = len(data)
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 4)

def filter_anomalies(logs, tolerance=1.5):
    # Irrelevant function – dead code path
    cleaned = []
    for log in logs:
        if isinstance(log, dict) and 'status' in log:
            cleaned.append(log['status'])
    return cleaned

def transform_sequence(seq):
    # Unused transformation with bit manipulation red herring
    transformed = []
    for i, val in enumerate(seq):
        shifted = (val << 2) ^ 0xA
        if i % 3 == 0:
            shifted = shifted ^ (i | 5)
        transformed.append(shifted % 100)
    return transformed

def merge_ranges(ranges):
    # Distractor: set operation that looks important but isn't used in critical path
    merged = set()
    for start, end in ranges:
        merged.update(range(start, end + 1))
    return sorted(merged)

def extract_metrics(events):
    # Dead code: processes strings but unused
    timestamps = []n    for event in events:
        if 'timestamp' in event:
            ts = event['timestamp'].replace('T', '').split('.')[0]
            timestamps.append(int(ts[-6:]))
    return timestamps

def preprocess_readings(raw):
    # Core preprocessing — relevant
    result = []
    for item in raw:
        if isinstance(item, dict) and 'value' in item:
            norm = normalize(item['value'])
            result.append(norm)
    return result

def generate_signature(data):
    # Decoy function using XOR on indices
    sig = 0
    for i, v in enumerate(data):
        sig ^= (v * i) & 0xFFFF
    return sig

def analyze_readings(data, constraints):
    # Critical analysis logic
    base_score = sum(data)
    adjustment = 0
    constraint_violations = 0
    
    s1 = {x for x in data if x > 50}  # Set comprehension: relevant distractor
    s2 = {x for x in constraints if x < 70}
    overlap = s1 & s2  # Meaningful set operation
    
    if len(overlap) > 3:
        adjustment += 12
    else:
        adjustment -= 8
    
    for d in data:
        if d < 15:
            constraint_violations += 1
        elif d > 90:
            constraint_violations += 2
    
    penalty = constraint_violations * 5
    return base_score - penalty + adjustment

# --- Main Execution ---
raw_sensor_data = [
    {'value': 102, 'source': 'A'},
    {'value': 14, 'source': 'B'},
    {'value': 67, 'source': 'C'},
    {'value': 91, 'source': 'D'},
    {'value': 45, 'source': 'E'},
    {'value': 11, 'source': 'F'},
    {'value': 73, 'source': 'G'},
    {'value': 88, 'source': 'H'}
]

# Irrelevant auxiliary data
system_logs = [
    {'event': 'startup', 'status': 1},
    {'event': 'ping', 'status': 1},
    {'event': 'error', 'status': 0}
]

config_ranges = [(10, 20), (30, 45), (50, 95)]
feature_flags = {'debug': False, 'enhanced': True, 'legacy_mode': False}
event_stream = ['T123456Z', 'T123458X', 'T123460Y']

# Step 1: Preprocess the sensor data
processed_data = preprocess_readings(raw_sensor_data)

# Step 2: Define thresholds as a set
threshold_set = {15, 25, 40, 55, 60, 70, 85, 90}

# Step 3: Validate input (side check, doesn't affect final result)
sensor_ok = sensor_validation([r['value'] for r in raw_sensor_data])

# Step 4: Compute entropy (distractor metric)
data_entropy = compute_entropy(processed_data)

# Step 5: Transform sequence (red herring computation)
shifted_sequence = transform_sequence(processed_data)

# Step 6: Merge ranges (irrelevant set usage)
coverage_spans = merge_ranges(config_ranges)

# Step 7: Extract metrics (dead-end string processing)
timing_marks = extract_metrics([{'timestamp': t} for t in event_stream])

# Step 8: Generate signature (bitwise decoy)
data_signature = generate_signature(processed_data)

# Step 9: Analyze readings with constraints (critical step)
final_diagnostic = analyze_readings(processed_data, threshold_set)

# Output result
print(f"Result: {final_diagnostic}")