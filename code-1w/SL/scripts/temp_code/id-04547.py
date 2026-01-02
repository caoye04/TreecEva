import math

def collect_metrics(data_points):
    # Irrelevant function: collects metrics but not used in final calculation
    return {k: len(v) for k, v in data_points.items()}

def validate_entry(entry):
    # Superficial validation with misleading side effects
    if 'flag' in entry and entry['flag'] == 'critical':
        return False
    return True

def transform_signal(raw_signal):
    # Applies transformation but some parts are decoys
    magnitude = sum([x ** 2 for x in raw_signal])
    normalized = [x / (magnitude ** 0.5) for x in raw_signal if x != 0]
    filtered = [x for x in normalized if abs(x) > 0.1]
    reversed_phase = [-x for x in filtered][::-1]  # Unused
    return filtered  # Only this matters

def extract_features(signal_chunk):
    # Extracts features using set operations and string logic
    squares = {x**2 for x in signal_chunk}
    evens = {x for x in signal_chunk if x % 2 == 0}
    feature_set = squares.intersection(evens)
    modifier_key = "shift_active"
    shift_code = len(modifier_key.replace("_", ""))  # 12
    adjusted_features = [val - shift_code for val in feature_set]
    return sorted(adjusted_features)

def simulate_buffer_overflow():
    # Dead code path — looks important but never called
    buffer = [0] * 1024
    for i in range(len(buffer)):
        buffer[i] = (buffer[i-1] + i) % 256
    return buffer

def decode_timestamp(ts_str):
    # Processes timestamp string with red herring logic
    clean = ts_str.strip().lower()
    if 'z' in clean:
        clean = clean.replace('z', '')
    segments = clean.split(':')
    parsed = [int(s) for s in segments if s.isdigit()]
    checksum = sum(parsed) * 7
    fake_offset = math.sin(checksum)  # Not used
    return parsed[-1] if parsed else 0

def process_logs(raw_logs):
    # Main processing chain with distractions
    processed_entries = []
    temp_cache = []
    for log in raw_logs:
        if not validate_entry(log):  # Some filtering
            continue
        timestamp_sec = decode_timestamp(log['timestamp'])
        signal_data = log['readings']
        transformed = transform_signal(signal_data)
        features = extract_features(transformed)
        entry_hash = hash(tuple(features)) % 1000
        # Construct enriched entry
        enriched = {
            'time': timestamp_sec,
            'feature_count': len(features),
            'hash_id': entry_hash,
            'diagnostic_flag': entry_hash % 3 == 0
        }
        temp_cache.append(enriched)  # Unused cache
        processed_entries.append(enriched)
    return processed_entries

def compute_entropy(values):
    # Unused advanced math function — red herring
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log(p) for p in probs)

def analyze_readings(processed_logs):
    # Final analysis with critical computation
    flagged_count = 0
    time_sum = 0
    diagnostic_scores = []
    for entry in processed_logs:
        time_sum += entry['time']
        if entry['diagnostic_flag']:
            flagged_count += 1
        # Core logic hidden among distractions
        score = entry['feature_count'] * 17 - entry['hash_id']
        diagnostic_scores.append(abs(score))
    
    # Critical line: real answer comes from here
    base_result = sum(diagnostic_scores) // (flagged_count or 1)
    adjustment = len(set(diagnostic_scores))  # Set operation
    final_score = base_result - adjustment
    
    # Decoy calculations
    outlier = max(diagnostic_scores) - min(diagnostic_scores)
    noise_ratio = outlier / (base_result + 1e-8)
    final_checksum = str(final_score).zfill(8)  # String method use
    verification = sum(int(d) for d in final_checksum if d in '13579')
    
    return final_score  # This is the actual output used

# Simulated input data
raw_system_logs = [
    {
        'timestamp': '2023-11-05T14:48:32Z',
        'readings': [1.2, -2.4, 3.6, 0.0, -1.2, 4.8],
        'flag': 'normal'
    },
    {
        'timestamp': '2023-11-05T14:49:15',
        'readings': [2.1, -2.1, 4.2, -4.2, 6.3],
        'flag': 'critical'  # Will be filtered out
    },
    {
        'timestamp': '2023-11-05T14:50:01Z',
        'readings': [0.5, 1.5, -0.5, -1.5, 2.5, 3.5],
        'flag': 'normal'
    },
    {
        'timestamp': '2023-11-05T14:51:22',
        'readings': [1.0, 2.0, 3.0, 4.0],
        'flag': 'normal'
    }
]

# Processing pipeline
filtered_entries = [entry for entry in raw_system_logs if entry.get('flag') != 'critical']
processed_logs = process_logs(filtered_entries)
final_diagnostic = analyze_readings(processed_logs)
print(f"Target result: {final_diagnostic}")