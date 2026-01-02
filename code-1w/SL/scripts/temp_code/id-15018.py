import math

def analyze_signal(pattern, threshold=0.75):
    # Irrelevant signal processing function (dead end)
    magnitude = sum(abs(x) for x in pattern)
    normalized = [x / magnitude for x in pattern if magnitude > 0]
    return [math.sin(x) * threshold for x in normalized]

def validate_checksum(data):
    # Complex but irrelevant checksum validation
    if not data:
        return False
    checksum = 0
    for i, val in enumerate(data):
        checksum ^= (val + i) & 0xFF
    return checksum % 13 == 0

def transform_sequence(seq, key_map):
    # Unused transformation logic (red herring)
    mapped = []
    for s in seq:
        temp = 0
        for ch in str(s):
            if ch in key_map:
                temp += key_map[ch] ** 2
        mapped.append(temp)
    return mapped

def decode_payload(payload):
    # Distractor: looks important but unused
    parts = []
    for p in payload:
        if isinstance(p, tuple) and len(p) == 2:
            a, b = p
            parts.append((a << 2) | (b >> 1))
    return parts

def evaluate_health(metrics):
    # Evaluates system health with complex logic
    score = 0
    weights = {'cpu': 0.3, 'mem': 0.25, 'io': 0.2, 'net': 0.15, 'disk': 0.1}
    
    # Simulated thresholds and scaling
    for k, v in metrics.items():
        if k in weights:
            norm = min(v / 100.0, 1.0)
            if norm > 0.8:
                score += weights[k] * (1.0 + (norm - 0.8) * 2)
            elif norm > 0.5:
                score += weights[k] * 1.0
            else:
                score += weights[k] * norm / 0.5
    
    return score

def compute_entropy(values):
    # Unused entropy calculation (distractor)
    total = sum(values)
    if total == 0:
        return 0.0
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log2(p) for p in probs)

def process_metrics(log_data, state):
    # Core relevant function
    baseline = {"A": 5, "B": 3, "C": 8}
    adjustments = []
    
    for entry in log_data:
        if 'error' in entry and entry['error']:
            continue
        if 'values' not in entry:
            continue
        
        # Extract and filter valid integers
        raw_vals = [x for x in entry['values'] if isinstance(x, int)]
        if len(raw_vals) < 2:
            continue
        
        # Key computation step
        avg_val = sum(raw_vals) / len(raw_vals)
        capped = min(avg_val, 100)
        adjustments.append(capped)
    
    # Conditional expression used meaningfully
    base_score = sum(adjustments) if adjustments else 42.0
    
    # Dictionary operations for routing logic
    routing_table = {
        'critical': lambda x: x * 1.8,
        'warning': lambda x: x * 1.3,
        'normal': lambda x: x * 0.9
    }
    
    mode = state.get('mode', 'normal')
    if mode in routing_table:
        base_score = routing_table[mode](base_score)
    
    # Final adjustment based on nested condition
    override_flag = state.get('override', False)
    safety_margin = state.get('margin', 0.95)
    
    if override_flag and base_score > 50:
        result = base_score * safety_margin
    else:
        result = base_score * (1.05 if base_score <= 75 else 0.98)
    
    # Additional distraction: unused intermediate
    temp_diag = {'raw': log_data, 'score': result, 'version': '2.1'}
    temp_diag['timestamp'] = 1678886400
    temp_diag['checksum'] = sum(result.__hash__() % 1000 for _ in range(1))
    
    return int(round(result))

# Irrelevant global constants (distractors)
MAX_BUFFER_SIZE = 8192
DEFAULT_TIMEOUT = 30
RETRY_LIMIT = 3
ACTIVE_MODULES = ['sensor', 'comms', 'power']

# Simulated system logs (input data)
log_entries = [
    {'timestamp': 1678886400, 'values': [10, 20, 30], 'error': False},
    {'timestamp': 1678886401, 'values': [40, 'skip', 60], 'error': False},
    {'timestamp': 1678886402, 'values': [], 'error': True},
    {'timestamp': 1678886403, 'values': [25, 75]},
    {'timestamp': 1678886404, 'values': [100]}  # will be skipped due to length
]

# System state configuration
system_status = {
    'mode': 'warning',
    'override': True,
    'margin': 0.93,
    'active_sensors': 4,
    'firmware': 'v3.4.1'
}

# Dead code path invocation (never used)
dummy_sequence = [123, 456, 789]
key_lookup = {'1': 2, '2': 3, '3': 5, '4': 7, '5': 11, '6': 13, '7': 17, '8': 19, '9': 23}
_ = transform_sequence(dummy_sequence, key_lookup)

# Another red herring call
payload_data = [(10, 20), (30, 40)]
_ = decode_payload(payload_data)

# Critical execution point
final_diagnostic = process_metrics(log_entries, system_status)

# Print result as required
print(f"Target result: {final_diagnostic}")