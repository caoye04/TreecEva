from collections import defaultdict, Counter
import math

# Simulated sensor data from a distributed monitoring system
timestamped_readings = [
    (1623456780, 'node_A', 23.5), (1623456781, 'node_B', 24.1),
    (1623456782, 'node_A', 25.3), (1623456783, 'node_C', 19.8),
    (1623456784, 'node_B', 26.0), (1623456785, 'node_A', 24.8),
    (1623456786, 'node_C', 20.2), (1623456787, 'node_B', 25.6),
    (1623456788, 'node_A', 26.1), (1623456789, 'node_C', 19.9)
]

# Irrelevant auxiliary function - dead code path
def legacy_calibrate(x):
    return (x * 1.02) + 0.5 if x < 20 else (x * 0.98) - 0.3

# Unused transformation map
transform_map = {k: v for k, v in zip('ABCDEF', range(6))}

# Misleading intermediate aggregation
raw_stats = defaultdict(list)
for ts, node, val in timestamped_readings:
    raw_stats[node].append(val)

# Compute per-node averages - seems important but not directly used later
node_averages = {node: sum(vals)/len(vals) for node, vals in raw_stats.items()}

# Fake normalization step with decoy logic
normalized_offsets = {}
baseline_ref = 20.0
for node in raw_stats:
    offset = abs(node_averages[node] - baseline_ref) * 0.1
    normalized_offsets[node] = round(offset, 2)

# Real processing begins: extract sequences above threshold
high_load_periods = []
critical_threshold = 25.0
for _, node, temp in timestamped_readings:
    if temp > critical_threshold:
        high_load_periods.append((node, temp))

# Build frequency profile using Counter - relevant
load_frequency = Counter([node for node, _ in high_load_periods])

# Secondary metric: deviation magnitude
magnitude_shifts = [temp - 25 for _, temp in high_load_periods]
total_deviation = sum(abs(x) for x in magnitude_shifts)

# Decoy statistical analysis with unused results
skewness_estimate = 0.0
if len(magnitude_shifts) >= 3:
    n = len(magnitude_shifts)
    mean_val = sum(magnitude_shifts) / n
    variance = sum((x - mean_val)**2 for x in magnitude_shifts) / n
    if variance > 0:
        cubed_deviations = sum((x - mean_val)**3 for x in magnitude_shifts)
        skewness_estimate = (cubed_deviations / n) / (variance ** 1.5)

# Simulate network hop simulation - completely irrelevant
network_hops = defaultdict(int)
for i, (ts, node, _) in enumerate(timestamped_readings):
    hop_count = (ts + i) % 4 + 1
    network_hops[node] += hop_count

# Shadow data structure - red herring
diag_matrix = [[0]*3 for _ in range(3)]
for idx, (_, _, val) in enumerate(timestamped_readings):
    diag_matrix[idx % 3][idx % 3] += val / 10

# Core diagnostic logic
status_flags = set()
if load_frequency['node_A'] > 1:
    status_flags.add('A_HIGH')
if sum(magnitude_shifts) > 2.0:
    status_flags.add('OVERHEAT_TREND')
if len(high_load_periods) >= 4:
    status_flags.add('SUSTAINED_LOAD')

# Data summary construction - key input
active_nodes = [n for n, cnt in load_frequency.items() if cnt >= 2]
data_summary = {
    'nodes': active_nodes,
    'total_anomalies': len(high_load_periods),
    'deviation_score': round(total_deviation, 3),
    'flags': list(status_flags)
}

# System load vector with fake components
system_load = [0] * 5
for i, node in enumerate(['node_A', 'node_B', 'node_C']):
    system_load[i] = load_frequency.get(node, 0) * 1.5
system_load[3] = int(skewness_estimate * 100)  # Unused artifact
system_load[4] = network_hops['node_A'] % 7  # Red herring value

# Primary processing function
def process_metrics(metrics, load_vector):
    score = 0
    
    # Check active nodes
    if 'node_A' in metrics['nodes']:
        score += 100
    
    # Weighted anomaly count
    weighted_anomalies = metrics['total_anomalies'] * 17
    score += weighted_anomalies
    
    # Deviation multiplier
    base_dev = metrics['deviation_score']
    if base_dev > 3.0:
        score *= 1.1
    
    # Process flags
    flag_bonus = {'A_HIGH': 25, 'OVERHEAT_TREND': 40, 'SUSTAINED_LOAD': 60}
    for flag in metrics['flags']:
        if flag in flag_bonus:
            score += flag_bonus[flag]
    
    # Irrelevant bitwise manipulation on load vector
    magic_shift = 0
    for val in load_vector:
        if val > 0:
            magic_shift ^= int(val) << 2
    
    # Dummy recursive checksum (never alters score)
    def checksum_recursive(arr, depth=0):
        if depth >= 3 or len(arr) == 0:
            return 1
        mid = len(arr) // 2
        return (checksum_recursive(arr[:mid], depth+1) * 
                checksum_recursive(arr[mid:], depth+1) + depth)
    
    dummy_key = checksum_recursive(load_vector)
    obscure_factor = (magic_shift & 0xFF) ^ dummy_key
    
    # Final adjustment - obscured but deterministic
    final_modifier = (obscure_factor % 9) - 4
    score += final_modifier * 2  # Small tweak based on noise
    
    return int(score)

# Execution point of interest
final_diagnostic = process_metrics(data_summary, system_load)
print(f"Result: {final_diagnostic}")