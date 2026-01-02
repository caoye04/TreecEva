from collections import defaultdict, Counter
from itertools import combinations, cycle
import math

# Simulated sensor network diagnostic system
def analyze_node_health(sensor_readings, thresholds):
    healthy_count = 0
    stress_flags = []
    cumulative_variance = 0.0

    for node_id, readings in sensor_readings.items():
        if len(readings) < 5:
            continue

        avg = sum(readings) / len(readings)
        variance = sum((x - avg) ** 2 for x in readings) / len(readings)
        cumulative_variance += variance

        high_stress = sum(1 for r in readings if r > thresholds['critical'])
        if high_stress > 2:
            stress_flags.append(node_id)

        if avg < thresholds['safe'] and variance < 25:
            healthy_count += 1

    # Irrelevant aggregation (distractor)
    phantom_metric = sum(math.sin(i) for i in range(len(stress_flags) + 1))

    return healthy_count, cumulative_variance, stress_flags

def detect_anomalies(log_entries):
    anomaly_count = 0
    temporal_gaps = []
    prev_timestamp = None

    for entry in log_entries:
        timestamp = entry['ts']
        if prev_timestamp is not None:
            gap = timestamp - prev_timestamp
            temporal_gaps.append(gap)
            if gap > 1000:
                anomaly_count += 1
        prev_timestamp = timestamp

    # Dead code path (misleading)
    if len(temporal_gaps) > 100:
        smoothing_factor = 0.85
        adjusted_gaps = [g * smoothing_factor for g in temporal_gaps]

    # Unused computation
    entropy = -sum((count / len(temporal_gaps)) * math.log2(count / len(temporal_gaps)) 
                   for count in Counter(temporal_gaps).values()) if temporal_gaps else 0

    return anomaly_count

def reconstruct_topology(active_pairs):
    graph = defaultdict(set)
    node_degree = defaultdict(int)

    for a, b in active_pairs:
        graph[a].add(b)
        graph[b].add(a)
        node_degree[a] += 1
        node_degree[b] += 1

    cycles_detected = 0
    # Use itertools to generate potential triangles (irrelevant to final result)
    for node in graph:
        if len(graph[node]) >= 2:
            for neighbor_pair in combinations(graph[node], 2):
                if neighbor_pair[0] in graph[neighbor_pair[1]]:
                    cycles_detected += 1

    # Complex but irrelevant structural analysis
    clustering_coeff = 0.0
    if node_degree:
        clustering_coeff = sum(v % 3 == 0 for v in node_degree.values()) / len(node_degree)

    return len(graph), cycles_detected  # Only first matters

def compute_integrity_score(nodes, log):
    base_score = len(nodes) * 10
    penalty = 0

    # Real health check
    readings = {nid: nd['readings'] for nid, nd in nodes.items()}
    thresholds = {'safe': 40, 'critical': 85}
    healthy, variance_total, stressed = analyze_node_health(readings, thresholds)
    
    # Primary deduction path
    if healthy < len(nodes) * 0.6:
        penalty += 25

    # Anomaly-based penalty
    anomalies = detect_anomalies(log)
    if anomalies > 3:
        penalty += 15

    # Topology validity
    active_links = [(n, nb) for n, nd in nodes.items() for nb in nd['neighbors']]
    node_count, _ = reconstruct_topology(active_links)
    if node_count != len(nodes):
        penalty += 20

    # One more red herring: historical decay factor (unused)
    history_log = log[:-10] if len(log) > 10 else log
    decay_weight = sum(1 / (1 + math.exp(-len(entry['data']) / 5)) for entry in history_log)

    # Final score computation (only this line matters for answer)
    final_diagnostic = base_score - penalty
    
    # Irrelevant printing (distraction)
    debug_state = {
        'variance_trace': round(variance_total, 3),
        'stressed_nodes': len(stressed),
        'temporal_anomalies': anomalies
    }
    
    return final_diagnostic

# System state initialization (real data)
sensor_network = {
    'N01': {'readings': [35, 38, 41, 37, 36, 39], 'neighbors': ['N02', 'N03']},
    'N02': {'readings': [88, 92, 85, 90, 87, 89], 'neighbors': ['N01']},
    'N03': {'readings': [40, 42, 38, 41, 39], 'neighbors': ['N01', 'N04']},
    'N04': {'readings': [82, 86, 88, 84, 85], 'neighbors': ['N03']}
}

system_activity_log = [
    {'ts': 100, 'data': 'init'},
    {'ts': 250, 'data': 'ping'},
    {'ts': 300, 'data': 'ack'},
    {'ts': 1350, 'data': 'retry'},
    {'ts': 1400, 'data': 'ack'},
    {'ts': 1450, 'data': 'data_chunk'},
    {'ts': 2500, 'data': 'retry'},
    {'ts': 2550, 'data': 'ack'},
    {'ts': 3600, 'data': 'retry'},
    {'ts': 3650, 'data': 'ack'}
]

# Execution point of interest
final_diagnostic = compute_integrity_score(sensor_network, system_activity_log)
print(f"Result: {final_diagnostic}")