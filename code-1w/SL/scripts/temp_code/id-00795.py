import math

def analyze_phase(root_node, threshold):
    if not root_node['children']:
        return root_node['value'] > threshold
    return sum(analyze_phase(child, threshold) for child in root_node['children']) >= len(root_node['children']) // 2

def compute_entropy(data_stream):
    freq_map = {}
    for item in data_stream:
        freq_map[item] = freq_map.get(item, 0) + 1
    entropy = 0.0
    total = len(data_stream)
    for count in freq_map.values():
        p = count / total
        entropy -= p * math.log2(p) if p > 0 else 0
    return round(entropy, 6)

def validate_checksum(sequence):
    # Irrelevant validation logic (dead path)
    checksum = 0
    for x in sequence:
        checksum = (checksum + x) % 257
    return checksum == 131

def generate_waveform(frequency, duration):
    # Distractor function: unused in main logic
    waveform = []
    for t in range(duration * 100):
        sample = int(math.sin(2 * math.pi * frequency * t / 100) * 100)
        waveform.append(sample)
    return waveform

def filter_anomalies(log_entries):
    # Misleading processing with decoy results
    anomalies = []
    baseline = sum(e['metric'] for e in log_entries) / len(log_entries)
    for entry in log_entries:
        if abs(entry['metric'] - baseline) > 2 * baseline / 3:
            anomalies.append(entry['id'])
    return sorted(anomalies)  # Not used later

def aggregate_metrics(nodes, load_profile):
    active_set = set()
    backup_queue = []
    temp_results = {}

    for node in nodes:
        if node['status'] != 'active':
            continue
        
        # Core logic step 1: collect valid identifiers
        node_id = node['id']
        if node_id % 4 != 0:
            active_set.add(node_id)

        # Core logic step 2: accumulate diagnostic values under conditions
        if node['diagnostics']['level'] > 3:
            temp_results[node_id] = node['diagnostics']['value']

        # Dead branch: never taken due to invariant
        if node['id'] < 0:
            backup_queue.append(node)  # unreachable

    # Core logic step 3: sum relevant diagnostics
    base_score = sum(temp_results.values())

    # Core logic step 4: apply modular adjustment based on load profile
    load_mod = sum(load_profile) % 97

    # Core logic step 5: combine with set cardinality effect
    set_influence = len(active_set) * 13

    # Core logic step 6: final computation
    intermediate = (base_score + set_influence) * 7
    final_diagnostic = (intermediate + load_mod) % 100000

    # Decoy assignment: looks important but unused
    audit_trail = {
        'nodes_scanned': len(nodes),
        'valid_count': len(temp_results),
        'checksum_valid': validate_checksum([base_score, set_influence]),
        'entropy': compute_entropy(list(temp_results.keys()))
    }

    return final_diagnostic

# Simulated system state
network_nodes = [
    {'id': 4, 'status': 'active', 'value': 5, 'children': [], 'diagnostics': {'level': 5, 'value': 23}},
    {'id': 8, 'status': 'active', 'value': 3, 'children': [], 'diagnostics': {'level': 4, 'value': 17}},
    {'id': 12, 'status': 'inactive', 'value': 8, 'children': [], 'diagnostics': {'level': 6, 'value': 41}},
    {'id': 16, 'status': 'active', 'value': 2, 'children': [], 'diagnostics': {'level': 2, 'value': 5}},
    {'id': 20, 'status': 'active', 'value': 9, 'children': [], 'diagnostics': {'level': 5, 'value': 34}},
]

system_load = [15, 22, 8, 43, 19, 7, 31]

# Trigger key computation
final_diagnostic = aggregate_metrics(network_nodes, system_load)

# Output target result
print(f"Result: {final_diagnostic}")