import itertools

# System diagnostics and network health monitoring simulation
def analyze_node_health(node_data, threshold=0.75):
    if not node_data['active'] or node_data['latency'] > 1000:
        return 'CRITICAL'
    elif node_data['utilization'] > threshold:
        return 'WARNING'
    else:
        return 'HEALTHY'

def compute_entropy(data_stream):
    # Misleading function - looks relevant but unused in final calculation
    from collections import Counter
    counts = Counter(data_stream)
    total = len(data_stream)
    entropy = 0
    for k in counts:
        p = counts[k] / total
        entropy -= p * (p ** 0.5)  # Not actual entropy, just distraction
    return round(entropy, 4)

def generate_combinations(elements):
    # Distractor: generates unused combinations
    combs = []
    for r in range(1, len(elements)+1):
        combs.extend(itertools.combinations(elements, r))
    return combs  # Never used

def filter_active_nodes(nodes):
    return {k: v for k, v in nodes.items() if v['active']}  # Used once, then ignored

def calculate_redundancy_score(primary, backups):
    score = 0
    for node in backups:
        if node['geographic_diversity']:
            score += 0.3
        if node['power_source'] == 'redundant':
            score += 0.2
    return min(score, 1.0)

def extract_timestamps(log_entries):
    # Dead code path - collected but never analyzed
    timestamps = []
    for entry in log_entries:
        if 'timestamp' in entry:
            timestamps.append(entry['timestamp'])
    return sorted(timestamps)

def validate_consistency(node_list, log):
    # Complex-looking validation with no real impact
    inconsistencies = 0
    for record in log:
        if record['node_id'] in node_list:
            if record['status'] == 'ERROR' and node_list[record['node_id']]['active']:
                inconsistencies += 1
    # Result discarded; only used to populate decoy variables
    temp_flag = inconsistencies > 5
    debug_snapshot = {'inconsistencies': inconsistencies, 'flag': temp_flag}
    return True  # Always returns True regardless

def aggregate_metrics(nodes, system_log):
    # Core logic hidden among distractions
    filtered = {k: v for k, v in nodes.items() if v['active']}
    health_states = [analyze_node_health(node) for node in filtered.values()]
    
    # Real computation begins here — obscurely dependent on prior filtering
    uptime_weights = [node['uptime'] * 0.001 for node in filtered.values()]
    base_score = sum(uptime_weights) / len(uptime_weights) if uptime_weights else 0
    
    # Conditional adjustment based on health distribution
    warnings = health_states.count('WARNING')
    criticals = health_states.count('CRITICAL')
    
    if criticals > 0:
        base_score *= 0.3
    elif warnings > 2:
        base_score *= 0.7
    else:
        base_score *= 1.1
    
    # Incorporate slicing of sorted utilization values
    utilizations = sorted([node['utilization'] for node in filtered.values()])
    mid_range = utilizations[len(utilizations)//4 : len(utilizations)//4*3]  # Middle 50%
    adjustment_factor = sum(mid_range) / len(mid_range) if mid_range else 0
    
    # Final formula
    result = (base_score * 100) - (adjustment_factor * 10)
    return int(round(result))

# Simulated infrastructure data
network_nodes = {
    'node_01': {
        'active': True,
        'latency': 80,
        'utilization': 0.65,
        'uptime': 950,
        'geographic_diversity': False,
        'power_source': 'standard'
    },
    'node_02': {
        'active': True,
        'latency': 120,
        'utilization': 0.88,
        'uptime': 1100,
        'geographic_diversity': True,
        'power_source': 'redundant'
    },
    'node_03': {
        'active': False,  # Inactive -> excluded
        'latency': 40,
        'utilization': 0.45,
        'uptime': 800,
        'geographic_diversity': True,
        'power_source': 'redundant'
    },
    'node_04': {
        'active': True,
        'latency': 200,
        'utilization': 0.72,
        'uptime': 980,
        'geographic_diversity': False,
        'power_source': 'standard'
    },
    'node_05': {
        'active': True,
        'latency': 60,
        'utilization': 0.89,
        'uptime': 1050,
        'geographic_diversity': True,
        'power_source': 'redundant'
    }
}

system_log = [
    {'node_id': 'node_01', 'status': 'OK', 'timestamp': 1678886400},
    {'node_id': 'node_02', 'status': 'ERROR', 'timestamp': 1678886405},
    {'node_id': 'node_04', 'status': 'OK', 'timestamp': 1678886410},
    {'node_id': 'node_05', 'status': 'ERROR', 'timestamp': 1678886415},
    {'node_id': 'node_01', 'status': 'OK', 'timestamp': 1678886420}
]

# Irrelevant preprocessing steps
all_keys = list(network_nodes.keys())
combined_pairs = generate_combinations(all_keys[:3])  # Unused result
timestamp_sequence = extract_timestamps(system_log)

# Dummy dictionary operations
snapshot_log = {entry['node_id']: entry['status'] for entry in system_log}
status_count = {s: list(snapshot_log.values()).count(s) for s in set(snapshot_log.values())}

# Decoy analysis
validate_consistency(network_nodes, system_log)  # Returns True, no side effects

# Actual pipeline
active_nodes = filter_active_nodes(network_nodes)  # Used only to distract from core flow
baseline_metric = calculate_redundancy_score(network_nodes['node_01'], [network_nodes['node_02'], network_nodes['node_05']])
data_stream = [1, 0, 1, 1, 0, 0, 0, 1]
entropy_value = compute_entropy(data_stream)  # Computed but irrelevant

# Key execution point
final_diagnostic = aggregate_metrics(network_nodes, system_log)

# Output required format
print(f"Result: {final_diagnostic}")