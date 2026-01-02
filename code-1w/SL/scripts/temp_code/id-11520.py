import math

def analyze_signal(pattern):
    if len(pattern) < 3:
        return 0
    return sum([p ** 2 for p in pattern if p % 2 == 1])

def deprecated_checksum(data):
    # Dead function - not used in main logic
    return sum([data[i] * (i + 1) for i in range(len(data))]) % 17

def evaluate_stability(ratio):
    if ratio <= 0:
        return False
    log_val = math.log(ratio)
    return 0.5 <= log_val <= 2.0

def parse_timestamp(ts_str):
    # Irrelevant string processing distraction
    parts = ts_str.split(':')
    hours = int(parts[0]) if len(parts) > 0 else 0
    minutes = int(parts[1]) if len(parts) > 1 else 0
    seconds = float(parts[2]) if len(parts) > 2 else 0.0
    total_seconds = hours * 3600 + minutes * 60 + seconds
    normalized = round(total_seconds / 86400, 6)
    return normalized if normalized > 0.25 else 0.0

def transform_sequence(seq):
    # Complex but ultimately unused transformation
    shifted = [(seq[i] + seq[(i+1)%len(seq)]) for i in range(len(seq))]
    filtered = [x for x in shifted if x > 5]
    return [math.sqrt(x) for x in filtered if x > 0]

def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    probabilities = [v / total for v in values if v > 0]
    entropy = -sum(p * math.log(p) for p in probabilities)
    return round(entropy, 6)

def validate_nodes(node_map):
    # Distracting dictionary traversal with side computation
    scores = {}
    for k, v in node_map.items():
        if isinstance(v, list) and len(v) > 0:
            avg = sum(v) / len(v)
            scores[k] = avg * (1 + len(k) % 3)
    aggregate = sum(scores.values())
    return aggregate > 10

def process_metrics(log_entries, state_config):
    # Core relevant logic begins
    base_score = 0
    for entry in log_entries:
        if 'error' in entry['level']:
            base_score += 3
        elif 'warning' in entry['level']:
            base_score += 1
    
    # Extract numeric payload from logs
    readings = [e['value'] for e in log_entries if 'value' in e]
    
    # Key intermediate: signal analysis
    signal_strength = analyze_signal(readings)
    
    # Compute derived metric
    derived_ratio = (signal_strength + 1) / (base_score + 1)
    
    # Evaluate conditional stability
    stable_system = evaluate_stability(derived_ratio)
    
    # Extract configuration threshold
    threshold = state_config.get('critical_threshold', 100)
    
    # Real answer path depends on this conditional
    if stable_system and signal_strength > threshold:
        multiplier = 2
    elif not stable_system and base_score > 5:
        multiplier = -1
    else:
        multiplier = 1
    
    # Final diagnostic calculation
    final_diagnostic = (signal_strength - base_score) * multiplier
    
    # Decoy assignment - looks important but unused
    final_diagnostic_shadow = compute_entropy(readings) * 100
    
    return final_diagnostic

# Simulated input data
log_data = [
    {'timestamp': '03:15:22.100', 'level': 'warning', 'value': 5},
    {'timestamp': '03:15:23.250', 'level': 'info', 'value': 7},
    {'timestamp': '03:15:24.400', 'level': 'error', 'value': 3},
    {'timestamp': '03:15:25.550', 'level': 'warning', 'value': 9},
    {'timestamp': '03:15:26.700', 'level': 'error', 'value': 5},
    {'timestamp': '03:15:27.850', 'level': 'info', 'value': 11}
]

system_state = {
    'mode': 'active',
    'nodes': {'A': [4,6,8], 'B': [2,5], 'C': [7,9,3]},
    'critical_threshold': 8,
    'timeout': 30
}

# Unused complex data structure
auxiliary_grid = [[i*j + 2 for j in range(5)] for i in range(4)]

# Trigger irrelevant functions to create red herrings
parse_timestamp('01:45:30.500')
deprecated_checksum([3, 6, 9, 12])
transform_sequence([8, 4, 6, 10])
validate_nodes(system_state['nodes'])

# Critical execution point
final_diagnostic = process_metrics(log_data, system_state)

# Output result
print(f"Result: {final_diagnostic}")