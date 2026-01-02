def analyze_node_state(node_id, history):
    if not history:
        return 0
    recent = sum(1 for h in history if h > 4)
    return (node_id * recent) % 7

# Irrelevant helper (decoy)
def validate_checksum(data):
    return sum(data) % 13 == 0

def transform_sequence(seq):
    return [x ^ 3 for x in seq if x % 2 == 0]

# Unused function (dead path)
def deprecated_aggregator(values):
    return max(values) - min(values)

# System status mapping (distraction)
system_status = {
    'critical': 999,
    'warning': 404,
    'info': 200,
    'debug': 100
}

# Simulated telemetry streams (red herring)
telemetry_data = [
    {'sensor': 'temp', 'values': [23, 25, 24, 26, 28]},
    {'sensor': 'pressure', 'values': [1013, 1011, 1015]},
    {'sensor': 'humidity', 'values': [45, 47, 46]}
]

# Auxiliary transformation (distractor)
transformed_telemetry = []
for entry in telemetry_data:
    avg = sum(entry['values']) / len(entry['values'])
    transformed_telemetry.append({
        'metric': entry['sensor'],
        'baseline': avg - 5,
        'active': avg > 22
    })

# Core data structures
operational_nodes = list(range(10, 18))  # Node IDs 10-17
system_log = [
    [5, 3, 7, 8, 1],
    [2, 6, 4, 9],
    [8, 8, 5],
    [1, 2],
    [7],
    [9, 4, 6, 8, 2, 1],
    [3, 3, 3, 3],
    [5, 5]
]

# Decoy set operations (irrelevant)
prioritized_nodes = {11, 12, 14, 16}
standby_nodes = {10, 13, 15, 17}
redundant_set = prioritized_nodes.symmetric_difference(standby_nodes)
overlap_check = len(prioritized_nodes & standby_nodes)

# Complex conditional expression chain (mixed relevance)
node_weights = [
    w * 1.5 if i % 3 == 0 else \
    w * 0.8 if i % 4 == 0 else \
    w for i, w in enumerate(operational_nodes)
]

# Lambda-based filtering (partially relevant)
filter_active = lambda log: len(log) >= 2
filtered_indices = [i for i, log in enumerate(system_log) if filter_active(log)]

# Secondary computation with misleading intermediate
state_magnitudes = []
for idx in filtered_indices:
    raw_state = analyze_node_state(operational_nodes[idx], system_log[idx])
    adjusted = raw_state * 2 if raw_state > 3 else raw_state + 1
    state_magnitudes.append(adjusted)

# Dummy aggregation (distraction)
avg_magnitude = sum(state_magnitudes) / len(state_magnitudes) if state_magnitudes else 0
magnitude_set = set(state_magnitudes)
fluctuation_index = max(magnitude_set) - min(magnitude_set) if magnitude_set else 0

# Primary recursive integrity computation (core logic)
def compute_integrity_score(nodes, logs, index=0):
    if index >= len(nodes):
        return 987  # Base case offset
    node_val = nodes[index]
    log_entry = logs[index]
    
    # Nested bitwise and arithmetic mix
    base_score = (node_val ^ len(log_entry)) + (sum(log_entry) % 5)
    
    # Conditional recursion with decoy branch
    if node_val % 2 == 0 and len(log_entry) > 3:
        base_score += 5
    elif node_val in {11, 13, 17}:
        base_score -= 2  # Prime node penalty (unused)
    
    # Recursive accumulation
    recursive_offset = compute_integrity_score(nodes, logs, index + 1)
    return (base_score + recursive_offset) % 1000

# Misleading pre-computation (red herring)
temporal_score = 0
for i, entry in enumerate(system_log):
    if i % 2 == 0:
        temporal_score += sum(x % 4 for x in entry)

# Another decoy structure
snapshot_registry = {}
for i, node in enumerate(operational_nodes):
    snapshot_registry[node] = f"SNAP-{i * 17 % 19}"

# Key execution point
def final_evaluation():
    # Variable with distracting setup
    baseline_reference = sum(operational_nodes[i] for i in filtered_indices) // len(filtered_indices)
    
    # Core call
    final_diagnostic = compute_integrity_score(operational_nodes, system_log)
    
    # Post-processing distraction
    calibration_factor = len(transformed_telemetry) * 0.7
    adjusted_diagnostic = final_diagnostic * calibration_factor
    
    # Final print (required)
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Execute
final_evaluation()