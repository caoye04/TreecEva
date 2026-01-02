import math

# System diagnostics simulation with interference

def generate_signal_strength(frequency, phase, noise_level=0.3):
    return abs(math.sin(frequency * phase) * (1 - noise_level))

def calculate_entropy(data_stream):
    if not data_stream:
        return 0.0
    freq_map = {}
    for item in data_stream:
        freq_map[item] = freq_map.get(item, 0) + 1
    entropy = 0.0
    total = len(data_stream)
    for count in freq_map.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 6)

def filter_anomalies(log_entries):
    # Irrelevant filtering logic (dead path)
    critical_entries = []
    for entry in log_entries:
        if entry['level'] == 'CRITICAL' and entry['code'] > 500:
            critical_entries.append(entry)
    return critical_entries  # Never used

def compute_hash_chain(seed_value, length):
    # Distractor function: simulates cryptographic hash chaining but unused
    result = seed_value
    for i in range(length):
        result = (result * 97 + 13) % 10007
    return result

def reconstruct_path(traces, mode='full'):
    # Unused path reconstruction (red herring)
    if mode == 'full':
        return [t['node'] for t in traces if t.get('active', True)]
    else:
        return []

def evaluate_node_stability(readings):
    # Computes stability index based on variance threshold
    mean_val = sum(readings) / len(readings)
    variance = sum((x - mean_val) ** 2 for x in readings) / len(readings)
    return 1 if variance < 0.25 else 0

def aggregate_metrics(nodes):
    # Core logic embedded within distractions
    active_flags = [node['status'] for node in nodes]
    signal_data = [node['signal'] for node in nodes]
    
    # Real computation begins
    valid_nodes = [n for n in nodes if n['active'] and n['version'] >= 2]
    
    # Extract diagnostic codes using slicing
    codes = [n['diagnostics'][1:4] for n in valid_nodes]  # slice positions 1-3
    flat_codes = [code for sublist in codes for code in sublist]
    
    # Compute modular checksum
    checksum = 0
    for i, code in enumerate(flat_codes):
        checksum += (code * (i + 1)) % 19
    
    # Secondary metric: stability consensus
    stability_votes = []
    for node in valid_nodes:
        stable = evaluate_node_stability(node['readings'])
        stability_votes.append(stable)
    
    # Aggregate via weighted combination
    base_score = sum(flat_codes)
    adjustment = (checksum * 0.7) + (sum(stability_votes) * 1.5)
    
    # Final diagnostic calculation
    final_diagnostic = int(base_score + adjustment)
    
    # Dead code branches below
    if final_diagnostic > 1000:
        fallback = compute_hash_chain(final_diagnostic, 5)
        final_diagnostic = (final_diagnostic + fallback) % 500
    
    return final_diagnostic

# Simulated network node data with red herrings
network_nodes = [
    {
        'name': 'node-alpha',
        'status': 'online',
        'active': True,
        'version': 2,
        'signal': generate_signal_strength(2.1, 1.8),
        'diagnostics': [5, 12, 18, 7, 3],
        'readings': [0.91, 0.93, 0.90, 0.92],
        'metadata': {'region': 'us-east', 'tier': 1}
    },
    {
        'name': 'node-beta',
        'status': 'degraded',
        'active': True,
        'version': 3,
        'signal': generate_signal_strength(1.7, 2.3),
        'diagnostics': [8, 14, 22, 9],
        'readings': [0.45, 0.55, 0.50, 0.48],
        'metadata': {'region': 'eu-west', 'tier': 2}
    },
    {
        'name': 'node-gamma',
        'status': 'offline',
        'active': False,
        'version': 1,
        'signal': generate_signal_strength(0.9, 3.1),
        'diagnostics': [3, 10, 15, 6],  # Not included due to inactive
        'readings': [0.10, 0.12, 0.08],
        'metadata': {'region': 'ap-south', 'tier': 1}
    },
    {
        'name': 'node-delta',
        'status': 'online',
        'active': True,
        'version': 2,
        'signal': generate_signal_strength(3.2, 1.4),
        'diagnostics': [7, 13, 19, 8, 1],
        'readings': [0.88, 0.91, 0.89, 0.90],
        'metadata': {'region': 'us-west', 'tier': 2}
    }
]

# Background entropy analysis (distractor)
data_log = [1, 1, 2, 2, 2, 3, 3, 1, 2]
entropy_diagnostic = calculate_entropy(data_log)

# Phantom anomaly detection
logs = [
    {'level': 'CRITICAL', 'code': 501},
    {'level': 'INFO', 'code': 200}
]
anomalies = filter_anomalies(logs)  # Computed but unused

# Fake path trace
trace_log = [
    {'node': 'A', 'active': True},
    {'node': 'B', 'active': False}
]
reconstructed = reconstruct_path(trace_log)  # Dead variable

# Hash chain decoy
decoy_seed = 42
phantom_hash = compute_hash_chain(decoy_seed, 10)  # Unused

# Key execution point
final_diagnostic = aggregate_metrics(network_nodes)

# Output result
print(f"Result: {final_diagnostic}")