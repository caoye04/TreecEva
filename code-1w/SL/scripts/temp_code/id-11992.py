from itertools import combinations, cycle

def analyze_signal_path(topology):
    # Irrelevant analysis function (dead code path)
    return sum(len(path) for path in topology if len(path) > 3)

def generate_frequency_map(signals):
    # Distractor: builds frequency map but unused
    freq = {}
    for s in signals:
        freq[s] = freq.get(s, 0) + 1
    return freq

def validate_node_sync(nodes):
    # Misleading validation that returns a decoy number
    sync_score = 0
    for i, node in enumerate(nodes):
        if i % 2 == 0 and len(node['channels']) >= 3:
            sync_score += node['id'] ^ 7
    return sync_score + 1000  # Red herring result

def compute_integrity_score(nodes):
    # Core logic: compute checksum based on specific conditions
    active_weights = []
    for node in nodes:
        # Relevant condition: only consider active nodes with even IDs
        if node['status'] == 'active' and node['id'] % 2 == 0:
            # Weight calculation: id * number of channels
            weight = node['id'] * len(node['channels'])
            active_weights.append(weight)
    
    # Additional filtering: only use weights divisible by 4
    filtered_weights = [w for w in active_weights if w % 4 == 0]
    
    # Use itertools to generate pairs and compute sum of XORs
    xor_sum = 0
    for a, b in combinations(filtered_weights, 2):
        xor_sum += (a ^ b)
    
    # Final transformation: multiply by number of valid nodes
    modifier = len(filtered_weights)
    if modifier > 0:
        result = xor_sum * modifier
    else:
        result = 0
    
    # Decoy operation: makes it look like something else matters
    _ = [result // (i+1) for i in range(3) if result > 100]
    
    return result

# Simulated network node data (mixed relevant and irrelevant entries)
network_nodes = [
    {'id': 2, 'status': 'active', 'channels': [50, 60, 70], 'latency': 12},
    {'id': 3, 'status': 'inactive', 'channels': [55, 65], 'latency': 20},
    {'id': 4, 'status': 'active', 'channels': [75, 85, 95, 105], 'latency': 8},
    {'id': 6, 'status': 'active', 'channels': [110, 120], 'latency': 15},
    {'id': 8, 'status': 'active', 'channels': [130, 140, 150, 160], 'latency': 5},
    {'id': 10, 'status': 'inactive', 'channels': [170], 'latency': 30},
]

# Unused signal data — distractor
digital_signals = [1, 0, 1, 1, 0, 0, 1]
signal_topology = [[1,2],[3,4,5],[6]]

# Dead function calls that don't affect outcome
dummy_analysis = analyze_signal_path(signal_topology)
frequency_profile = generate_frequency_map(digital_signals)

# Key execution point
checksum = compute_integrity_score(network_nodes)

# Print result as required
print(f"Result: {checksum}")