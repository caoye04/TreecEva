from collections import defaultdict, Counter
import math

# Simulated network node data with diagnostic flags
def generate_node_data():
    nodes = []
    for i in range(16):
        node = {
            'id': f'N{i:02d}',
            'signal_strength': (i * 17) % 89,
            'latency': (i * 13 + 41) % 101,
            'errors': (i * 7) % 17,
            'active': (i % 3) != 1,
            'priority': i % 4
        }
        nodes.append(node)
    return nodes

# Irrelevant helper - looks important but unused in critical path
def compute_entropy(data_list):
    counts = Counter(data_list)
    total = len(data_list)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 3)

# Decoy function - never called but looks related
def analyze_error_patterns(nodes):
    pattern_count = defaultdict(int)
    for node in nodes:
        key = (node['errors'] % 4, node['latency'] % 5)
        pattern_count[key] += 1
    return dict(pattern_count)

# Misleading accumulation - used but ultimately irrelevant
def calculate_jitter_score(nodes):
    scores = []
    for node in nodes:
        temp_score = 0
        if node['signal_strength'] > 50:
            temp_score += 10
        if node['latency'] < 50:
            temp_score += 15
        if node['errors'] == 0:
            temp_score += 5
        scores.append(temp_score)
    
    # Dead code branch - never executed due to data constraints
    if any(s > 100 for s in scores):
        return sum(scores) * 2
    else:
        return sum(scores) // 3  # Distractor result

# Core processing pipeline
def filter_active_nodes(nodes):
    return [node for node in nodes if node['active']]

def classify_by_priority(nodes):
    buckets = defaultdict(list)
    for node in nodes:
        buckets[node['priority']].append(node)
    return buckets

def compute_diagnostic_value(bucket):
    # Uses bitwise mixing of aggregated values
    total_signal = sum(n['signal_strength'] for n in bucket)
    total_latency = sum(n['latency'] for n in bucket)
    error_sum = sum(n['errors'] for n in bucket)
    
    # Complex transformation with masking
    base = (total_signal ^ total_latency) & 0xFFFF
    shifted = (base << 1) & 0xFFFF
    combined = shifted ^ (error_sum << 2)
    
    # Normalize using harmonic-like mean component
    size = len(bucket)
    if size == 0:
        return 0
    harmonic_component = size / sum(1/(n['signal_strength'] + 1) for n in bucket)
    
    # Final blend - only this matters
    return int((combined * 0.7) + (harmonic_component * 0.3))

# Real critical path
def aggregate_metrics(nodes):
    active_nodes = filter_active_nodes(nodes)
    priority_groups = classify_by_priority(active_nodes)
    
    # Accumulate diagnostics across priorities
    diagnostics = []
    for pri in range(4):
        group = priority_groups.get(pri, [])
        if len(group) >= 3:  # Threshold filter
            diag_val = compute_diagnostic_value(group)
            diagnostics.append(diag_val)
    
    # Main answer computation
    final = sum(diagnostics) & 0xFFFFFF  # Bounded combination
    
    # DEAD CODE PATH - unreachable due to above logic
    if len(diagnostics) == 0:
        fallback = 0
        for n in nodes:
            fallback ^= (n['signal_strength'] * n['latency']) % 1000
        final = fallback  # Never used
    
    # Red herring: extensive but irrelevant statistical analysis
    signal_vals = [n['signal_strength'] for n in active_nodes]
    latency_vals = [n['latency'] for n in active_nodes]
    sorted_pairs = sorted(zip(signal_vals, latency_vals), key=lambda x: x[0])
    median_idx = len(sorted_pairs) // 2
    median_signal = sorted_pairs[median_idx][0]
    
    # Another decoy metric
    variance_proxy = 0
    if signal_vals:
        mean_sig = sum(signal_vals) / len(signal_vals)
        variance_proxy = sum((x - mean_sig) ** 2 for x in signal_vals) / len(signal_vals)
    
    # This print is a distraction - not the real answer
    debug_status = f"Nodes: {len(active_nodes)}, Median: {median_signal}, Var: {variance_proxy:.1f}"
    print(f'DEBUG: {debug_status}')  # Distractor output
    
    return final

# Initialization and execution
network_nodes = generate_node_data()

# Phantom modification - looks important but doesn't affect outcome
for node in network_nodes:
    if node['id'] in ['N05', 'N12']:
        node['priority'] = (node['priority'] + 1) % 4

# Critical statement
final_diagnostic = aggregate_metrics(network_nodes)
print(f'Target result: {final_diagnostic}')