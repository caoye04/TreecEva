from collections import defaultdict, Counter
import math

# Simulated sensor data aggregation for a distributed system health monitor
def collect_telemetry(nodes):
    raw_readings = defaultdict(list)
    for node_id, metrics in nodes.items():
        raw_readings['cpu'].append(metrics['cpu'])
        raw_readings['mem'].append(metrics['mem'])
        raw_readings['queue_depth'].append(metrics.get('queue', 0))
    return raw_readings

# Irrelevant function: calculates network latency distribution (not used in final result)
def analyze_latency(peers):
    latencies = [p['rtt'] for p in peers.values()]
    avg = sum(latencies) / len(latencies)
    variance = sum((x - avg) ** 2 for x in latencies) / len(latencies)
    return {'average': avg, 'std_dev': math.sqrt(variance)}

# Core signal processing chain
def extract_entropy(signal):
    # Simulate entropy extraction from bit patterns
    binary_stream = ''.join(f'{int(x * 100) % 16:04b}' for x in signal)
    ones_count = binary_stream.count('1')
    return ones_count ^ len(binary_stream)  # Bitwise mix

def normalize_range(values):
    min_val, max_val = min(values), max(values)
    if min_val == max_val:
        return [0.5] * len(values)
    return [(v - min_val) / (max_val - min_val) for v in values]

# Misleading diagnostic path (dead end)
def legacy_diagnostic(data):
    score = 0
    for k, v in data.items():
        if len(v) > 3:
            score += sum(v[:3])
        else:
            score += sum(v)
    return score * 0.7

# Real computation begins here
node_data = {
    'alpha': {'cpu': 78.2, 'mem': 65.4, 'queue': 12},
    'beta': {'cpu': 82.1, 'mem': 70.0, 'queue': 15},
    'gamma': {'cpu': 65.3, 'mem': 88.2, 'queue': 8},
    'delta': {'cpu': 91.7, 'mem': 79.1, 'queue': 23}
}

network_peers = {
    'peer1': {'rtt': 45.2, 'loss': 0.1},
    'peer2': {'rtt': 52.8, 'loss': 0.0},
    'peer3': {'rtt': 38.1, 'loss': 0.2}
}

# Step 1: Collect and preprocess telemetry
telemetry = collect_telemetry(node_data)
sorted_cpu = sorted(telemetry['cpu'])
sorted_mem = sorted(telemetry['mem'])

# Step 2: Compute derived health indicators
cpu_normalized = normalize_range(telemetry['cpu'])
mem_normalized = normalize_range(telemetry['mem'])

# Step 3: Generate signature from combined signals
combined_signal = [a + b for a, b in zip(cpu_normalized, mem_normalized)]
bias_correction = sum(1 for x in combined_signal if x > 1.0)
trimmed_signal = [min(x, 1.0) for x in combined_signal]

# Step 4: Extract bit-level features
entropy_measure = extract_entropy(trimmed_signal)

# Step 5: Calculate load factor with combinatoric weight
n_nodes = len(node_data)
connection_complexity = (n_nodes * (n_nodes - 1)) // 2  # Fully connected pairs
system_load = connection_complexity + sum(telemetry['queue_depth'])

# Step 6: Create health fingerprint using Counter
fingerprint = Counter()
for val in telemetry['cpu']:
    bucket = int(val // 10)
    fingerprint[bucket] += 1

# Dead-end red herring call
legacy_score = legacy_diagnostic(telemetry)  # Unused afterward

# Step 7: Construct health signature
health_signature = (
    entropy_measure ^ 
    fingerprint[7] * 100 + 
    fingerprint[8] * 10 + 
    len([x for x in telemetry['mem'] if x > 75])
)

# Step 8: Final diagnostic processing
def process_metrics(signature, load):
    if load > 30:
        signature = signature * 1.1
    adjusted = math.floor(signature) & 0xFF  # Clamp to byte range
    checksum = (adjusted ^ (adjusted << 3) ^ (adjusted >> 2)) & 0xFF
    return (adjusted + checksum) // 2

# Critical execution point
final_diagnostic = process_metrics(health_signature, system_load)

# Distractor variables
theoretical_max = 255
normal_threshold = 45.0
emergency_override = False
latency_analysis = analyze_latency(network_peers)  # Computed but irrelevant

print(f"Result: {final_diagnostic}")