from collections import defaultdict, Counter

# Simulated network node diagnostic system
def analyze_node_consistency(node_data, baseline):
    score = 0
    for k in node_data:
        if k in baseline:
            score += abs(node_data[k] - baseline[k])
    return score + len(node_data)

# Irrelevant helper - distractor
def calculate_entropy(data):
    counts = Counter(data)
    total = sum(counts.values())
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * p  # Not actual entropy, misleading
    return entropy

# Unused function - dead code path
def deprecated_routing(nodes):
    return sorted(nodes, key=lambda x: x[1], reverse=True)

# Data transformation with red herring operations
network_nodes = {
    'alpha': {'signal': 5, 'load': 3, 'tier': 1},
    'beta': {'signal': 8, 'load': 1, 'tier': 2},
    'gamma': {'signal': 4, 'load': 4, 'tier': 1},
    'delta': {'signal': 9, 'load': 2, 'tier': 3}
}

# Misleading intermediate structure
snapshot_buffer = []
for node, attrs in network_nodes.items():
    temp_val = (attrs['signal'] * attrs['load']) ** 0.5
    snapshot_buffer.append(f'{node}:{temp_val:.2f}')

# Active links represented as tuples - relevant input
active_links = [('alpha', 'beta'), ('beta', 'gamma'), ('gamma', 'delta'), ('alpha', 'delta')]

# Decoy statistical analysis
link_weights = defaultdict(int)
correlation_cache = {}
for i, (src, tgt) in enumerate(active_links):
    link_weights[src] += i + 1
    correlation_cache[(src, tgt)] = pow(len(src) + len(tgt), 1.5)

# Fake signal propagation simulation (irrelevant)
propagation_matrix = []
for src, tgt in active_links:
    strength = network_nodes[src]['signal'] - network_nodes[tgt]['load']
    if strength > 0:
        propagation_matrix.append((src, tgt, strength * 0.75))

# Real computation begins here - obscured by prior noise
baseline_profile = {'signal': 6, 'load': 2, 'tier': 2}
consistency_logs = []

for node_id, attributes in network_nodes.items():
    raw_deviation = analyze_node_consistency(attributes, baseline_profile)
    normalized = raw_deviation / (attributes['tier'] + 1)
    consistency_logs.append(normalized)

# Core logic buried in middle of distractions
tier_grouping = defaultdict(list)
for node, attrs in network_nodes.items():
    tier_grouping[attrs['tier']].append(attrs['signal'])

average_signals = {t: sum(sigs)/len(sigs) for t, sigs in tier_grouping.items()}

# Critical computation hidden among decoys
def compute_integrity_score(nodes, links):
    base_score = 0
    for attrs in nodes.values():
        base_score += attrs['signal'] * attrs['load']
    
    # Red herring operation
    unused_diagnostic = calculate_entropy([n['tier'] for n in nodes.values()])
    
    # Actual dependency on link structure
    connection_bonus = 0
    node_degree = defaultdict(int)
    for a, b in links:
        node_degree[a] += 1
        node_degree[b] += 1
    
    for degree in node_degree.values():
        connection_bonus += degree ** 2
    
    # Final score computation
    adjustment = len(links) * 0.5
    return int((base_score + connection_bonus) - adjustment)

# Trigger point of interest
final_diagnostic = compute_integrity_score(network_nodes, active_links)

# Print required result
print(f"Target result: {final_diagnostic}")