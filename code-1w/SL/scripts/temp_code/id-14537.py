import math

def analyze_signal(pattern):
    # Irrelevant signal processing function (dead path)
    magnitude = sum([x ** 2 for x in pattern])
    return math.sqrt(magnitude) if magnitude > 100 else 0

def validate_checksum(data):
    # Unused validation logic (distractor)
    checksum = 0
    for item in data:
        if isinstance(item, int):
            checksum ^= item
    return checksum == 0

def transform_sequence(seq):
    # Complex but irrelevant transformation (red herring)
    transformed = []
    for i, val in enumerate(seq):
        if i % 2 == 0:
            transformed.append(val * 2 + (i // 2))
        else:
            transformed.append(val - 1)
    return [t % 7 for t in transformed]

def compute_entropy(values):
    # Misleading statistical computation (not used in final result)
    total = sum(values)
    probs = [(v / total) for v in values if v > 0]
    entropy = -sum(p * math.log2(p) for p in probs)
    return round(entropy, 4)

def evaluate_health_status(sensor_readings):
    # Health scoring with decoy logic
    base_score = 50
    for reading in sensor_readings:
        if reading < 0:
            base_score -= 5
        elif reading > 100:
            base_score += 3
    # This function appears important but is not directly connected
    return base_score > 60

def extract_features(logs):
    # Extracts features but some are unused
    feature_set = {}
    for entry in logs:
        level = entry.get('level', 'INFO')
        code = entry.get('code', 0)
        feature_set[level] = feature_set.get(level, 0) + 1
        if code > 0:
            feature_set['error_codes'] = feature_set.get('error_codes', []) + [code]
    # Only 'ERROR' count matters later; others are distractions
    return feature_set

def process_metrics(log_entries, state):
    # Core logic buried among distractors
    error_count = 0
    warning_count = 0
    info_count = 0
    for log in log_entries:
        lvl = log.get('level')
        if lvl == 'ERROR':
            error_count += 1
        elif lvl == 'WARNING':
            warning_count += 1
        elif lvl == 'INFO':
            info_count += 1

    # Real computation begins here
    severity_index = error_count * 7 + warning_count * 3
    
    # Destructuring assignment (tuple unpacking)
    (system_load, memory_usage, disk_io) = state['load'], state['memory'], state['disk']

    # Conditional expression (required language feature)
    load_factor = 2 if system_load > 80 else (1.5 if system_load > 50 else 1)
    
    # Bit manipulation as distraction
    masked_load = system_load & 63  # irrelevant
    inverted_memory = ~memory_usage & 0xFFFF  # red herring

    # Decoy combinatorial calculation
    combo_keys = ['a', 'b', 'c']
    permutations = []
    for i in range(len(combo_keys)):
        for j in range(len(combo_keys)):
            if i != j:
                permutations.append((combo_keys[i], combo_keys[j]))
    
    # String manipulation distraction
    status_str = "System: " + "_".join([k.upper() for k in state.keys()])
    status_str = status_str.replace("LOAD", "LOAD_FACTOR")

    # Actual core logic: diagnostic depends only on error count and load factor
    base_diagnostic = severity_index * load_factor
    
    # Final adjustment using conditional expression
    final_diagnostic = base_diagnostic if error_count > 0 else base_diagnostic / 2
    
    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Simulated input data
log_data = [
    {'timestamp': 1678886400, 'level': 'INFO', 'code': 200, 'msg': 'Service started'},
    {'timestamp': 1678886405, 'level': 'WARNING', 'code': 404, 'msg': 'Resource missing'},
    {'timestamp': 1678886410, 'level': 'ERROR', 'code': 500, 'msg': 'Server crash'},
    {'timestamp': 1678886415, 'level': 'ERROR', 'code': 503, 'msg': 'Timeout'},
    {'timestamp': 1678886420, 'level': 'WARNING', 'code': 403, 'msg': 'Forbidden'},
    {'timestamp': 1678886425, 'level': 'ERROR', 'code': 500, 'msg': 'Crash again'}
]

system_state = {
    'load': 75,
    'memory': 4200,
    'disk': 85,
    'network': 'active'
}

# Dead function calls (misleading execution paths)
transformed_seq = transform_sequence([1, 3, 5, 7, 9])
analyze_signal([10, 20, 30, 40])
compute_entropy([1, 2, 3, 4])

# Key execution point
final_diagnostic = process_metrics(log_data, system_state)
