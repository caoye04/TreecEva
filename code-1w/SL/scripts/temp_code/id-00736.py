import math

# Simulated system telemetry data with mixed relevance
telemetry_stream = [
    {'id': 101, 'load': 85.2, 'temp': 67, 'uptime': 42100},
    {'id': 102, 'load': 92.7, 'temp': 73, 'uptime': 38000},
    {'id': 103, 'load': 78.3, 'temp': 61, 'uptime': 45200},
    {'id': 104, 'load': 95.1, 'temp': 77, 'uptime': 33000},
    {'id': 105, 'load': 88.9, 'temp': 70, 'uptime': 39500}
]

# Irrelevant historical thresholds (distractor)
historical_thresholds = {
    'v1': [80, 90, 75], 'v2': [85, 88, 70], 'v3': [90, 92, 80]
}

# Decoy function - looks important but unused
def legacy_calibrate(data):
    return sum(d['load'] * 0.9 for d in data if d['temp'] > 65)

# Auxiliary transformation (partially relevant)
normalize = lambda x, low, high: (x - low) / (high - low)

# Bitmask simulation for fault detection (red herring)
fault_signature = 0b101101
mask_applied = fault_signature & 0b111111

# Unused intermediate calculations (dead code paths)
aggregated_load = sum(node['load'] for node in telemetry_stream)
avg_temp = sum(node['temp'] for node in telemetry_stream) / len(telemetry_stream)
max_uptime = max(node['uptime'] for node in telemetry_stream)

# Simulated environmental interference (irrelevant)
environment_factor = math.sin(math.pi / 6) * 1.5

# Core diagnostic logic begins here
status_flags = []
for node in telemetry_stream:
    load_norm = normalize(node['load'], 70, 100)
    temp_risk = 1 if node['temp'] >= 70 else 0
    # Hidden weighting: only nodes with id ending in odd digit contribute
    if node['id'] % 2 == 1:
        score = (load_norm * 0.7) + (temp_risk * 0.3)
        status_flags.append(score)

# Unused combinatorics (distractor)
from itertools import combinations
critical_pairs = list(combinations([n['id'] for n in telemetry_stream if n['load'] > 90], 2))

# Key dictionary operations and filtering
efficiency_map = {node['id']: node['uptime'] / 1000 for node in telemetry_stream}
active_ids = [101, 103, 105]  # Only these are processed further

# Primary analysis function with lambda integration
evaluate_stability = lambda scores: sum(s ** 1.2 for s in scores if s > 0.5)

# Misleading intermediate metric (looks final but isn't)
preliminary_index = evaluate_stability(status_flags) * 0.87

# Actual critical computation path
system_snapshot = {
    'readings': status_flags,
    'efficiency': efficiency_map,
    'actives': active_ids
}

# Final diagnostic calculation
final_diagnostic = 0
for node_id in system_snapshot['actives']:
    idx = node_id - 101  # index alignment
    if idx < len(system_snapshot['readings']):
        raw_score = system_snapshot['readings'][idx]
        # Apply non-linear correction based on efficiency
        efficiency_factor = system_snapshot['efficiency'][node_id] / 40.0
        final_diagnostic += raw_score * (1 + efficiency_factor)

# Output required result
print(f"Result: {final_diagnostic}")