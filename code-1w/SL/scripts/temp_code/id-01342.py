from collections import defaultdict, Counter
import math

# Simulated network node diagnostic system
def analyze_node_signal(strength, history, threshold=0.75):
    if len(history) < 3:
        return False
    avg = sum(history) / len(history)
    recent_trend = (history[-1] - history[0]) / len(history)
    return strength > threshold and avg > 0.5 and recent_trend > 0

# Irrelevant helper - looks important but unused in final path
def deprecated_validation_chain(data):
    accumulator = 0
    for item in data:
        if isinstance(item, int):
            accumulator += item ^ 3
    return accumulator % 7 == 0

# Core transformation pipeline
def transform_metrics(raw_data):
    transformed = []
    scaling_factor = 1.75
    offset_correction = 0.23
    
    for entry in raw_data:
        base_val = abs(entry.get('value', 0))
        if base_val > 100:
            normalized = 100
        else:
            normalized = base_val
        
        # Apply non-linear correction
        corrected = math.log(1 + normalized * scaling_factor) + offset_correction
        transformed.append(max(0, corrected))
    
    return transformed

# Secondary analysis with red herring computation
def evaluate_redundancy_pattern(sequence):
    if not sequence:
        return 0
    
    freq = Counter(sequence)
    entropy = 0
    total = len(sequence)
    
    for count in freq.values():
        p = count / total
        entropy -= p * math.log2(p)
    
    # Complex but irrelevant transformation
    magic_sequence = [1, 1]
    for i in range(2, 10):
        magic_sequence.append(magic_sequence[i-1] + magic_sequence[i-2])
    
    # Dead code path - never reached in this execution
    if entropy > 100:
        return sum(magic_sequence) / entropy
    
    return round(entropy * 100) / 100

# Main processing graph
def build_dependency_graph(nodes):
    graph = defaultdict(list)
    reverse_graph = defaultdict(list)
    
    for i, node in enumerate(nodes):
        dependencies = node.get('links', [])
        for dep in dependencies:
            graph[dep].append(i)
            reverse_graph[i].append(dep)
    
    return graph, reverse_graph

# Critical integrity computation
def compute_integrity_score(nodes):
    # Transform raw metrics
    raw_values = [{'value': node['metric']} for node in nodes]
    processed = transform_metrics(raw_values)
    
    # Build dependency structure
    forward_deps, backward_deps = build_dependency_graph(nodes)
    
    # Analyze signal patterns (mostly unused fields here)
    valid_signals = 0
    for i, node in enumerate(nodes):
        signal_hist = node.get('history', [])
        current_strength = processed[i] if i < len(processed) else 0
        if analyze_node_signal(current_strength, signal_hist, threshold=0.65):
            valid_signals += 1
    
    # Primary accumulation logic
    cumulative_weight = 0.0
    for i, val in enumerate(processed):
        impact_factor = 1 + len(forward_deps.get(i, []))
        stability_modifier = 0.8 if len(backward_deps.get(i, [])) > 1 else 1.0
        
        # Key accumulation step
        cumulative_weight += val * impact_factor * stability_modifier
    
    # Decoy normalization chain
    if cumulative_weight > 50:
        dummy_normalized = cumulative_weight / (1 + math.exp(-0.1 * cumulative_weight))
        # This looks important but isn't used
        adjusted_dummy = math.tanh(dummy_normalized / 100)

    # Final score calculation - depends on multiple paths
    base_score = cumulative_weight
    penalty = 0
    
    for node in nodes:
        if 'deprecated_flag' in node:  # None have this
            penalty += 10
    
    # Actual answer determination
    final_diagnostic = int(round(base_score - penalty))
    
    return final_diagnostic

# Simulation data with meaningful and irrelevant fields
network_nodes = [
    {
        'id': 'N001',
        'metric': 42,
        'history': [0.3, 0.4, 0.6, 0.7],
        'links': [1, 2],
        'metadata': {'version': '2.1', 'priority': 'high'}
    },
    {
        'id': 'N002',
        'metric': 85,
        'history': [0.1, 0.2, 0.5, 0.8],
        'links': [2],
        'metadata': {'version': '2.3', 'priority': 'medium'}
    },
    {
        'id': 'N003',
        'metric': 63,
        'history': [0.5, 0.6, 0.7, 0.9],
        'links': [],
        'metadata': {'version': '1.9', 'priority': 'low'}
    },
    {
        'id': 'N004',
        'metric': 28,
        'history': [0.2, 0.3, 0.4, 0.5],
        'links': [0],
        'metadata': {'version': '2.4', 'priority': 'high'}
    }
]

# Execution flow with decoy calls
auxiliary_data = [{'value': 10}, {'value': 20}, {'value': 30}]
deprecated_validation_chain([1,2,3,4,5])  # Dead call

transformed_aux = transform_metrics(auxiliary_data)  # Unused result

_ = evaluate_redundancy_pattern(transformed_aux)  # Result ignored

# Key execution point
final_diagnostic = compute_integrity_score(network_nodes)
print(f"Result: {final_diagnostic}")