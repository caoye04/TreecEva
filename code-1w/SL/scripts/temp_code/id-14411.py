def analyze_node_health(node_data, threshold=0.75):
    return sum(1 for val in node_data if val >= threshold)

# Irrelevant helper function (dead code path)
def compute_entropy(data):
    from math import log
    total = sum(data)
    if total == 0: return 0
    probs = [x / total for x in data]
    return -sum(p * log(p) for p in probs if p > 0)

def filter_active_connections(connections):
    # Only keep bidirectional active links
    active_set = set()
    for a, b, status in connections:
        if status == 'active':
            active_set.add((a, b))
            active_set.add((b, a))
    return active_set

def calculate_stability_score(metrics):
    # Distractor calculation with misleading intermediate result
    base_score = sum(metrics) * 0.87
    penalty = len([m for m in metrics if m < 0.5]) * 0.3
    return round(base_score - penalty, 4)

def integrate_diagnostics(primary, secondary):
    # Merges two diagnostic streams using set union and averaging
    combined_keys = set(primary.keys()) | set(secondary.keys())
    fusion = {}
    for k in combined_keys:
        vals = []
        if k in primary: vals.append(primary[k])
        if k in secondary: vals.append(secondary[k])
        fusion[k] = sum(vals) / len(vals)
    return fusion

def aggregate_metrics(nodes, log_entries):
    health_counts = {}
    stability_history = []
    
    # Core relevant logic starts here
    for node_id, readings in nodes.items():
        healthy_count = analyze_node_health(readings)
        health_counts[node_id] = healthy_count
        
        # Accumulate stability metrics
        if len(readings) > 0:
            avg_reading = sum(readings) / len(readings)
            stability_history.append(avg_reading)
    
    # Compute global indicators (distractor)
    max_health = max(health_counts.values()) if health_counts else 0
    min_health = min(health_counts.values()) if health_counts else 0
    range_health = max_health - min_health
    
    # Real computation path
    if stability_history:
        mean_stability = sum(stability_history) / len(stability_history)
    else:
        mean_stability = 0
    
    # Simulated log parsing (partially relevant)
    error_count = 0
    warning_levels = []
    for entry in log_entries:
        level = entry.get('level', '').lower()
        if level == 'error':
            error_count += 1
        elif level == 'warning':
            severity = entry.get('severity', 1)
            warning_levels.append(severity)
    
    # Red herring: complex but unused structure
    diagnostic_cube = {
        'dimensions': (len(nodes), len(log_entries), 3),
        'checksum': (len(nodes) * len(log_entries)) % 7,
        'flags': [False, True, False]
    }
    cube_volume = diagnostic_cube['dimensions'][0] * diagnostic_cube['dimensions'][1] * diagnostic_cube['dimensions'][2]
    
    # Unused recursive function (decoy)
    def trace_propagation(start, graph, depth=0):
        if depth > 2 or start not in graph:
            return 0
        return 1 + sum(trace_propagation(n, graph, depth+1) for n in graph.get(start, []))
    
    # Actual final computation
    base_metric = mean_stability * 100
    error_penalty = error_count * 2.5
    warning_factor = sum(warning_levels) * 1.2 if warning_levels else 0
    adjustment = (base_metric - error_penalty + warning_factor) / 1.8
    
    # Final answer variable
    final_diagnostic = int(round(adjustment))
    
    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Simulated input data
network_nodes = {
    'node_a': [0.8, 0.9, 0.7, 0.95],
    'node_b': [0.6, 0.4, 0.7, 0.8],
    'node_c': [0.9, 0.9, 0.85, 0.92],
    'node_d': [0.5, 0.3, 0.4, 0.6]
}

system_log = [
    {'timestamp': '2023-05-01T10:00:01', 'level': 'info', 'msg': 'startup'},
    {'timestamp': '2023-05-01T10:01:22', 'level': 'warning', 'severity': 2, 'msg': 'temp rise'},
    {'timestamp': '2023-05-01T10:02:33', 'level': 'error', 'msg': 'timeout'},
    {'timestamp': '2023-05-01T10:03:44', 'level': 'warning', 'severity': 3, 'msg': 'load peak'},
    {'timestamp': '2023-05-01T10:04:55', 'level': 'error', 'msg': 'disconnect'}
]

# Key execution point
final_diagnostic = aggregate_metrics(network_nodes, system_log)