def analyze_sequence(data, threshold=5):
    count = 0
    temp_sum = 0
    for val in data:
        if val > threshold:
            count += 1
            temp_sum += val
    return count


def compute_checksum(sequence):
    checksum = 0
    for i, v in enumerate(sequence):
        checksum ^= (v + i) * 3
    return checksum


def evaluate_conditions(flags, mode='strict'):
    if mode == 'strict':
        return all(flags)
    else:
        return any(flags)


def transform_record(record_dict):
    # Irrelevant transformation
    new_dict = {}
    for k, v in record_dict.items():
        if isinstance(v, int):
            new_dict[k] = v ** 2
        else:
            new_dict[k] = len(str(v))
    return new_dict


def filter_and_aggregate(values, limit):
    filtered = [v for v in values if v % 2 == 0 and v < limit]
    decoy_result = sum(x ** 0.5 for x in filtered if x > 10)  # Distractor
    return sum(filtered)


def recursive_reduce(n, cache={}):
    if n <= 1:
        return n
    if n in cache:
        return cache[n]
    cache[n] = recursive_reduce(n - 2) + recursive_reduce(n - 3)
    return cache[n]


def generate_lookup(keys):
    # Dead function - not used in main logic
    lookup = {k: hash(k) % 100 for k in keys}
    return lookup

def merge_states(state_a, state_b):
    merged = {}
    for key in set(state_a.keys()) | set(state_b.keys()):
        a_val = state_a.get(key, 0)
        b_val = state_b.get(key, 0)
        if isinstance(a_val, int) and isinstance(b_val, int):
            merged[key] = min(a_val, b_val)
        else:
            merged[key] = a_val or b_val
    return merged

def calculate_entropy(data):
    total = sum(data)
    if total == 0:
        return 0.0
    entropy = 0.0
    for x in data:
        if x > 0:
            p = x / total
            entropy -= p * (p ** 0.5)  # Not actual entropy, just misleading
    return round(entropy, 6)

def extract_features(dataset):
    features = []
    for record in dataset:
        if 'x' in record and 'y' in record:
            magnitude = (record['x']**2 + record['y']**2)**0.5
            features.append(int(magnitude))
    return features

def detect_anomalies(time_series):
    anomalies = []
    moving_avg = 0
    count = 0
    for t in time_series:
        moving_avg = 0.7 * moving_avg + 0.3 * t
        count += 1
        if t > 2 * moving_avg and count > 1:
            anomalies.append(count)
    return anomalies if anomalies else [0]

def build_index_map(elements):
    index_map = {}
    for idx, elem in enumerate(elements):
        index_map[elem] = index_map.get(elem, []) + [idx]
    return index_map

def validate_transitions(seq):
    errors = 0
    for i in range(len(seq) - 1):
        if seq[i] == seq[i+1]:
            errors += 1
    return errors == 0

def process_state(transitions, log_data):
    # Core relevant logic starts here
    state_vector = [t['state'] for t in transitions if t['valid']]
    
    # Extract counts using dictionary
    state_count = {}
    for s in state_vector:
        state_count[s] = state_count.get(s, 0) + 1
    
    # Use set to find unique states
    unique_states = set(state_vector)
    
    # Apply recursive reduction on length
    r_value = recursive_reduce(len(state_vector))
    
    # Aggregate log metrics
    log_entries = [entry['duration'] for entry in log_data if entry['success']]
    total_duration = sum(log_entries)
    duration_threshold = 100
    
    # Filter and get aggregate below threshold
    filtered_duration_sum = filter_and_aggregate(log_entries, duration_threshold)
    
    # Decoy computations (irrelevant)
    avg_duration = total_duration / len(log_entries) if log_entries else 0
    duration_set = set(log_entries)
    extended_analysis = calculate_entropy(log_entries)
    feature_snapshot = extract_features([{'x': d, 'y': d+1} for d in log_entries[:3]])
    
    # Key decision point
    if evaluate_conditions([len(unique_states) > 2, r_value > 5]):
        base_score = state_count.get(1, 0) * 17
        adjustment = len(log_data) - len(transitions)
        intermediate = base_score + adjustment
        
        # More distractions
        checksum = compute_checksum(log_entries)
        sequence_valid = validate_transitions(state_vector)
        
        # Final computation
        final_output = intermediate * 3 + filtered_duration_sum
        
        # Additional red herring
        debug_info = {
            'checksum': checksum,
            'anomalies': detect_anomalies(log_entries),
            'features': feature_snapshot
        }
        
        return final_output
    else:
        fallback = sum(state_count.values()) * 5
        return fallback * 2

# Main execution
transitions = [
    {'state': 1, 'valid': True},
    {'state': 2, 'valid': True},
    {'state': 3, 'valid': True},
    {'state': 1, 'valid': True},
    {'state': 4, 'valid': True},
    {'state': 2, 'valid': False},  # invalid
    {'state': 1, 'valid': True}
]

system_log = [
    {'duration': 20, 'success': True},
    {'duration': 40, 'success': True},
    {'duration': 60, 'success': True},
    {'duration': 80, 'success': True},
    {'duration': 90, 'success': True},
    {'duration': 150, 'success': False},  # failed
    {'duration': 110, 'success': True},
    {'duration': 120, 'success': True}
]

# Irrelevant data structures
metadata_store = {
    'version': '2.1.0',
    'author': 'sysbot_42',
    'tags': ['diagnostic', 'legacy'],
    'active': False
}

config_profile = {
    'timeout': 300,
    'retries': 3,
    'debug_mode': True
}

feature_flags = [True, False, True, True, False]

lookup_table = build_index_map(['A', 'B', 'C', 'A', 'D'])

# Trigger the main computation
final_output = process_state(transitions, system_log)
print(f"Target result: {final_output}")