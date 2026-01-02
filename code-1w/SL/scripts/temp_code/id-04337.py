import math

# Simulated network diagnostic system with red herrings and complex data flows
def analyze_node_load(node_id, history):
    if not history:
        return 0.0
    weighted_sum = sum(val * (0.5 ** i) for i, val in enumerate(reversed(history)))
    return weighted_sum / len(history)


def calculate_entropy(data_stream):
    # Irrelevant entropy calculation - dead code path
    freq_map = {}
    for item in data_stream:
        freq_map[item] = freq_map.get(item, 0) + 1
    total = len(data_stream)
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 6)

# Decoy function - never called in execution path
def deprecated_redundancy_check(nodes):
    return len(set(nodes)) < len(nodes)

# System state variables
network_state = {
    'nodes': ['N1', 'N2', 'N3', 'N4'],
    'status': [True, True, False, True],
    'latency': [120, 85, 150, 90],
    'bandwidth': [100, 200, 50, 300],
    'queue_depth': [30, 45, 60, 40]
}

# Signal cache with historical node metrics (relevant data)
signal_cache = [
    {'N1': [125, 118, 122], 'N2': [88, 82, 87], 'N3': [145, 155, 150], 'N4': [92, 88, 90]},
    {'N1': [119, 121], 'N2': [84, 86], 'N3': [152, 148], 'N4': [89, 91]},
    {'N1': [123], 'N2': [83], 'N3': [156], 'N4': [87]}
]

# Irrelevant auxiliary data structures (distractors)
resource_pool = {
    'cpu_units': [i * 17 % 13 for i in range(25)],  # Generated but unused
    'memory_segments': [[j for j in range(i, i+4)] for i in range(0, 20, 5)],
    'timestamp_log': ["2023-11-0{}T10:0{}.00Z".format(d, h) for d in range(1,4) for h in range(3,6)]
}

# Misleading intermediate calculations
baseline_latency = {node: max(50, min(200, network_state['latency'][i] * 0.9)) 
                     for i, node in enumerate(network_state['nodes'])}

peak_bandwidth = max(network_state['bandwidth'])
efficiency_ratio = sum(network_state['bandwidth']) / (4 * peak_bandwidth)

# Complex transformation chain - only some parts are relevant
node_health = {}
for idx, node in enumerate(network_state['nodes']):
    load_history = [cache[node] for cache in signal_cache if node in cache]
    flat_history = [item for sublist in load_history for item in sublist]
    avg_load = sum(flat_history) / len(flat_history) if flat_history else 0
    current_status = network_state['status'][idx]
    latency_score = 100 - abs(network_state['latency'][idx] - avg_load)
    bandwidth_weight = network_state['bandwidth'][idx] / sum(network_state['bandwidth'])
    
    # Health metric computed but only indirectly used later
    health = (latency_score * 0.6) + (avg_load * -0.1) + (bandwidth_weight * 50)
    node_health[node] = {
        'raw_health': health,
        'last_load': flat_history[-1] if flat_history else 0,
        'stability': len(flat_history) >= 3
    }

# Dead code block - looks important but unused
if any(not s for s in network_state['status']):
    failed_indices = [i for i, s in enumerate(network_state['status']) if not s]
    recovery_priority = sorted(failed_indices, key=lambda x: network_state['latency'][x], reverse=True)

# Red herring data structure
shadow_metrics = []
for i in range(len(network_state['nodes'])):
    temp_val = (network_state['latency'][i] ** 2)
    temp_val -= (network_state['queue_depth'][i] // 2) * 3
    shadow_metrics.append(max(0, temp_val))

# Core logic buried in distractions
health_scores = []
for node, data in node_health.items():
    score = data['raw_health']
    if data['stability']:
        score += 5.0
    if 'N3' in node:  # Penalty for faulty node
        score -= 20.0
    health_scores.append(score)

# Secondary irrelevant processing
unique_depths = set(network_state['queue_depth'])
congestion_level = len([d for d in network_state['queue_depth'] if d > 40])

# Key computation - integrates multiple concepts
transition_costs = []
for i in range(len(health_scores)):
    if i == 0:
        transition_costs.append(health_scores[i])
    else:
        delta = health_scores[i] - health_scores[i-1]
        adjusted_delta = delta * (network_state['bandwidth'][i] / 100)
        transition_costs.append(abs(adjusted_delta))

# Critical aggregation function
def aggregate_metrics(state, cache):
    base = 0.0
    # Use of list comprehension (required)
    active_nodes = [i for i, s in enumerate(state['status']) if s]
    
    for i in active_nodes:
        node = state['nodes'][i]
        queue_factor = state['queue_depth'][i] / 100
        latency_norm = state['latency'][i] / 50
        # Composite metric
        contribution = (latency_norm * 2) - (queue_factor * 0.8)
        base += contribution
    
    # Set operation (required): filter unique latency values from recent signals
    recent_latencies = []
    for snapshot in cache:
        recent_latencies.extend([vals[-1] for vals in snapshot.values() if vals])
    
    trimmed_set = set(recent_latencies)
    if len(trimmed_set) > 3:
        trimmed_set.remove(max(trimmed_set))
        trimmed_set.remove(min(trimmed_set))
    
    adjustment = sum(trimmed_set) / len(trimmed_set) if trimmed_set else 0
    
    # Final combination
    result = (base * 10) + (adjustment / 10)
    return round(result, 6)

# Execution point of interest
final_diagnostic = aggregate_metrics(network_state, signal_cache)

# Output required format
print(f"Target result: {final_diagnostic}")