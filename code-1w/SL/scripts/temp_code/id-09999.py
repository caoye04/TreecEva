import math

def analyze_node_health(node_id, readings):
    # Irrelevant helper with misleading complexity
    if len(readings) < 3:
        return 0
    avg = sum(readings) / len(readings)
    variance = sum((x - avg) ** 2 for x in readings) / len(readings)
    return math.sqrt(variance) if variance > 1 else avg

def compute_entropy(data):
    # Dead code path — never called
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

def filter_anomalies(events):
    # Distractor function: looks important but unused
    threshold = 3.5
    return [e for e in events if abs(e['magnitude']) < threshold]

def evaluate_stability(loads, thresholds):
    # Another decoy function with plausible logic
    stable_count = 0
    for load, limit in zip(loads, thresholds):
        if load < limit * 0.8:
            stable_count += 1
    return stable_count > len(loads) // 2

def aggregate_metrics(nodes, log_entries):
    # Core logic begins
    node_ids = set(nodes.keys())
    active_ids = set(log_entry['node'] for log_entry in log_entries if log_entry['status'] == 'active')
    inactive_ids = node_ids - active_ids

    # Misleading intermediate: complex but partially irrelevant calculation
    performance_scores = []
    for nid in active_ids:
        history = nodes[nid]['metrics']['response_time']
        if len(history) > 0:
            raw_score = sum(history) / len(history)
            adjusted_score = raw_score * (1 + 0.1 * math.sin(len(history)))
            performance_scores.append(adjusted_score)

    # Red herring: elaborate but unused data transformation
    diagnostic_snapshot = {
        'timestamp': 1678886400,
        'version': '2.1.5',
        'checksum': sum(hash(k) % 1000 for k in nodes) % 97
    }
    temp_debug = [analyze_node_health(nid, nodes[nid]['metrics']['cpu_load']) for nid in nodes]

    # Actual critical computation chain
    base_metric = len(active_ids) * 100
    penalty = 0
    for nid in inactive_ids:
        outage_duration = nodes[nid]['downtime']
        if outage_duration > 5:
            penalty += outage_duration * 10

    # Key distractor: multiple similar-looking accumulations
    auxiliary_sum = 0
    for entry in log_entries:
        if entry['type'] == 'error':
            auxiliary_sum += 1  # Looks important but not used in final result

    # Real dependency: uses set difference and conditional adjustment
    recovery_candidates = active_ids - {entry['source'] for entry in log_entries if entry['type'] == 'failure'}
    bonus = len(recovery_candidates) * 5

    # Final aggregation with red herring variables nearby
    preliminary = base_metric - penalty + bonus
    decay_factor = 0.95 ** (len(log_entries) % 10)
    final_diagnostic = int(preliminary * decay_factor)

    # Output required format
    return final_diagnostic

# Simulated input data
network_nodes = {
    'N001': {'metrics': {'response_time': [120, 110, 130], 'cpu_load': [2.1, 1.9]}, 'downtime': 0},
    'N002': {'metrics': {'response_time': [95, 105], 'cpu_load': [3.1, 2.8]}, 'downtime': 8},
    'N003': {'metrics': {'response_time': [200, 180, 220], 'cpu_load': [1.5]}, 'downtime': 12},
    'N004': {'metrics': {'response_time': [80], 'cpu_load': [2.5, 2.7]}, 'downtime': 0}
}

system_log = [
    {'node': 'N001', 'status': 'active', 'type': 'heartbeat'},
    {'node': 'N002', 'status': 'inactive', 'type': 'failure', 'source': 'N001'},
    {'node': 'N004', 'status': 'active', 'type': 'update'},
    {'node': 'N003', 'status': 'inactive', 'type': 'error', 'source': 'N002'},
    {'node': 'N001', 'status': 'active', 'type': 'failure', 'source': 'N004'}
]

# Execution point of interest
final_diagnostic = aggregate_metrics(network_nodes, system_log)
print(f"Target result: {final_diagnostic}")