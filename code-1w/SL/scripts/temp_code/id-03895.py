def analyze_node(traffic, threshold=75):
    return sum(1 for t in traffic if t > threshold)


def encode_signature(timestamps):
    encoded = 0
    for ts in timestamps:
        encoded ^= int(ts % 17)
    return encoded

# Irrelevant helper (distractor)
def compute_entropy(data):
    from math import log2
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    total = len(data)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 4)

# Unused function (dead code path)
def validate_checksum(structure):
    checksum = 0
    for i, val in enumerate(structure):
        checksum += i * val
    return checksum % 101

# Core logic with distractors
network_state = {
    'nodes': [12, 8, 23, 45, 67, 89, 34],
    'load_profile': [60, 70, 85, 90, 65, 78, 82],
    'timestamps': [1623.4, 1623.7, 1624.1, 1625.3, 1626.0],
    'flags': [True, False, True, False, True],
    'meta': {'version': '3.1.4', 'mode': 'diagnostic'}
}

system_log = [
    {'event': 'connect', 'latency': 45, 'active': True},
    {'event': 'query', 'latency': 120, 'active': True},
    {'event': 'update', 'latency': 67, 'active': False},
    {'event': 'sync', 'latency': 200, 'active': True},
    {'event': 'ping', 'latency': 30, 'active': True}
]

# Distractor variables
baseline_score = sum(network_state['nodes']) // len(network_state['nodes'])
diagnostic_flag = any(f for f in network_state['flags'])
raw_latency_sum = sum(entry['latency'] for entry in system_log)

# Irrelevant transformation (slicing used here)
history_slice = network_state['timestamps'][1:-1]
processed_history = [int(h * 10) % 100 for h in history_slice]

# Another decoy metric
temporal_variance = 0
for i in range(1, len(processed_history)):
    temporal_variance += (processed_history[i] - processed_history[i-1]) ** 2

# Real computation begins
high_load_count = analyze_node(network_state['load_profile'], threshold=75)
signature_key = encode_signature(network_state['timestamps'])

# Simulated weight adjustment
adjustment_factor = 1.5 if signature_key > 20 else 0.8

# Accumulation with logical filtering
active_latencies = []
for entry in system_log:
    if entry['active'] and entry['latency'] > 50:
        active_latencies.append(entry['latency'])

latency_ceiling = max(active_latencies) if active_latencies else 0
efficiency_ratio = len(active_latencies) / len(system_log)

# Data structure manipulation (dictionary and slicing)
summary_stats = {
    'node_count': len(network_state['nodes']),
    'high_load_nodes': high_load_count,
    'avg_active_latency': sum(active_latencies) / len(active_latencies) if active_latencies else 0,
    'signature': signature_key,
    'flag_status': diagnostic_flag
}

# Misleading aggregation (not used in final result)
mock_metric = (summary_stats['node_count'] * summary_stats['signature']) % 97

# Actual critical computation path
weight_1 = summary_stats['high_load_nodes'] * adjustment_factor
weight_2 = summary_stats['avg_active_latency'] // 10

# Final integration using dictionary values and logical condition
if summary_stats['flag_status']:
    base_score = weight_1 + weight_2
else:
    base_score = weight_1 - weight_2

# Secondary correction based on event pattern
critical_events = 0
for entry in system_log:
    if entry['latency'] > 100:
        critical_events += 1

# Apply correction only if more than one critical event
if critical_events > 1:
    base_score *= 1.2

# Final diagnostic computed from relevant state
final_diagnostic = int(base_score * 10)  # Scale for precision

# Output required
print(f"Result: {final_diagnostic}")