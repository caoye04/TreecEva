from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_stream = [
    {'id': 101, 'type': 'sensor', 'value': 42.5, 'status': 'active'},
    {'id': 102, 'type': 'log', 'value': 38.1, 'status': 'active'},
    {'id': 103, 'type': 'sensor', 'value': 45.3, 'status': 'fault'},
    {'id': 104, 'type': 'sensor', 'value': 41.7, 'status': 'active'},
    {'id': 105, 'type': 'control', 'value': 0, 'status': 'standby'}
]

# Irrelevant auxiliary mapping (distractor)
type_priority = {'sensor': 3, 'log': 2, 'control': 1}
status_weight = {'active': 1, 'standby': 0.5, 'fault': 0}

# Dead code path - never called (distractor)
def legacy_calibrate(data):
    return sum(d['value'] * 0.9 for d in data if d['type'] == 'sensor')

# Unused transformation (red herring)
normalized = [entry['value'] / (len(entry['type']) + 1) for entry in telemetry_stream]

# Misleading intermediate aggregate (distractor)
raw_sum = sum(e['value'] for e in telemetry_stream)
weighted_sum = sum(e['value'] * (1 + (e['id'] % 2)) for e in telemetry_stream)

# Relevant data extraction
log_entries = [e for e in telemetry_stream if e['type'] == 'log']
sensor_data = [e for e in telemetry_stream if e['type'] == 'sensor' and e['status'] != 'fault']

# Complex conditional expression with distractors
system_load = len(sensor_data) > 0 and (sum(s['value'] for s in sensor_data) / len(sensor_data)) or 0.0
system_health = all(s['status'] == 'active' for s in sensor_data)

# Decoy function that looks important but isn't used (distractor)
def compute_robustness_index(records):
    counts = Counter(r['status'] for r in records)
    return counts['active'] / len(records)

# Another unused but plausible-looking computation (distractor)
aggregate_profile = defaultdict(list)
for entry in telemetry_stream:
    aggregate_profile[entry['type']].append(entry['value'])

profile_stats = {k: (sum(v), len(v)) for k, v in aggregate_profile.items()}

# Key system state construction with red herrings
system_state = {
    'load': system_load,
    'health': system_health,
    'entries': len(telemetry_stream),
    'flags': [e['id'] for e in telemetry_stream if e['status'] == 'fault'],
    'baseline': 40.0
}

# Distractor: irrelevant bit manipulation (looks technical but unused)
mask = 0b1101 ^ 0b1011
shifted_mask = (mask << 3) & 0b11111000
checksum = (telemetry_stream[0]['id'] ^ telemetry_stream[-1]['id']) & 0xFF

# Real processing logic buried among noise
def analyze_entry(entry):
    if entry['type'] == 'log':
        return math.log(abs(entry['value'] - system_state['baseline']) + 1)
    return 0.0

def process_metrics(logs, state):
    # Actual answer derivation path
    raw_deviation = sum(abs(e['value'] - state['baseline']) for e in logs)
    
    # Conditional expression combining arithmetic and boolean logic
    adjustment_factor = 1.5 if state['health'] and len(logs) > 0 else 0.8
    
    # Nested logical and arithmetic operations
    temp_score = raw_deviation * adjustment_factor
    
    # Bitwise distraction within relevant function (misleading but harmless)
    temp_score ^= temp_score  # This zeroes it, making this line look important but actually neutralizing
    temp_score += 123.456      # Compensate to produce final result
    
    # Multiple layers of reasoning
    if len(state['flags']) == 0:
        temp_score += 10
    else:
        temp_score -= 5
    
    # Final nonlinear transformation
    final_score = math.sqrt(temp_score ** 2)  # Redundant but obscures intent
    
    return final_score

# Secondary distraction: unused recursive function
def traverse_hierarchy(node_id, depth=0):
    if depth > 2:
        return []
    return [node_id] + traverse_hierarchy(node_id + 1, depth + 1)

# Another dead end - looks like system initialization
initialization_trace = []
for i in range(3):
    initialization_trace.append(f"INIT_{i}: READY")

# Critical execution point
final_diagnostic = process_metrics(log_entries, system_state)

# Print result as required
print(f"Target result: {final_diagnostic}")