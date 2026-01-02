def analyze_sensor(network_state):
    if not network_state:
        return 0
    return sum(ord(c) for c in str(network_state)) % 7

# Irrelevant sensor calibration data (distractor)
calibration_keys = ['K1', 'K2', 'K3']
key_weights = {k: len(k) * 1.5 for k in calibration_keys}
reference_map = {i: chr(65 + i) for i in range(10)}

# Simulated environmental readings with noise
event_log = [
    {'time': 1001, 'type': 'TEMP', 'value': 42.5, 'node': 'A'},
    {'time': 1003, 'type': 'PRESS', 'value': 101.3, 'node': 'B'},
    {'time': 1005, 'type': 'TEMP', 'value': 38.1, 'node': 'C'},
    {'time': 1008, 'type': 'HUMID', 'value': 65.2, 'node': 'A'},
    {'time': 1010, 'type': 'TEMP', 'value': 44.7, 'node': 'B'}
]

# Decoy function - looks important but unused
def compute_baseline(readings):
    total = 0
    for r in readings:
        if r['type'] == 'TEMP':
            total += r['value'] * 0.8
    return total / max(len(readings), 1)

# Real processing begins here
sensor_types = ['TEMP', 'PRESS', 'HUMID']
recent_nodes = [entry['node'] for entry in event_log[-3:]]

# Filtering logic with distraction
valid_entries = []
for entry in event_log:
    if entry['type'] in sensor_types and entry['value'] > 0:
        valid_entries.append(entry)

# Misleading aggregation (dead-end)
temp_snapshot = [e['value'] for e in valid_entries if e['type'] == 'TEMP']
press_snapshot = [e['value'] for e in valid_entries if e['type'] == 'PRESS']
humid_snapshot = [e['value'] for e in valid_entries if e['type'] == 'HUMID']

avg_temp = sum(temp_snapshot) / len(temp_snapshot) if temp_snapshot else 0
weighted_pressure = sum(p * 1.05 for p in press_snapshot)

# Threshold map with red herring entries
threshold_map = {
    'TEMP': 40.0,
    'PRESS': 100.0,
    'HUMID': 60.0,
    'CO2': 450,      # Irrelevant type
    'LIGHT': 800     # Irrelevant type
}

# Filter only temperature readings above threshold (core logic)
filtered_data = []
for entry in valid_entries:
    t = entry['type']
    v = entry['value']
    if t in threshold_map and v > threshold_map[t]:
        filtered_data.append(entry)

# Auxiliary transformation using enumerate and zip (actual use)
indexed = list(enumerate([d['value'] for d in filtered_data]))
shifted = [v * (i + 1) for i, v in indexed]
overlap_check = list(zip(temp_snapshot, press_snapshot))  # Unused but plausible

# Real computation path
status_flags = []
for d in filtered_data:
    node_score = ord(d['node']) - ord('A') + 1
    excitation = int(d['value'] - threshold_map[d['type']])
    status_flags.append(node_score * excitation)

# Recursive helper to aggregate diagnostic codes
def accumulate_diagnostics(flags, idx=0):
    if idx >= len(flags):
        return 0
    return flags[idx] + 2 * accumulate_diagnostics(flags, idx + 1)

# Another decoy structure (unused dictionary pattern)
diagnostic_tree = {
    'level_1': {'sub': [{'code': x} for x in status_flags]},
    'meta': {'count': len(filtered_data), 'version': 'X'}
}

# Core processing function
def process_readings(data, thresholds):
    if not data:
        return -1
    
    # Use list comprehension and slicing
    values = [d['value'] for d in data]
    recent_values = values[-2:]  # Last two only
    base = sum(recent_values)
    
    nodes = [d['node'] for d in data]
    # Use slicing and enumerate meaningfully
    node_contrib = sum((i + 1) * (ord(n) - 64) for i, n in enumerate(nodes))
    
    # Inject result from recursive accumulation
    flags = []
    for d in data:
        diff = d['value'] - thresholds[d['type']]
        rank = ord(d['node']) - ord('A') + 1
        flags.append(int(diff) * rank)
    recursive_sum = accumulate_diagnostics(flags)
    
    # Final composition
    return int(base + node_contrib + recursive_sum * 0.5)

# Execute critical statement
final_diagnostic = process_readings(filtered_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")