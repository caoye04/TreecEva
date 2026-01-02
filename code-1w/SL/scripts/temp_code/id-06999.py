import math

# Network topology simulation with optimization logic
def calculate_hop_distance(routing_table, source, target):
    if source == target:
        return 0
    if target in routing_table[source]:
        return 1
    for intermediate in routing_table[source]:
        if calculate_hop_distance(routing_table, intermediate, target) == 1:
            return 2
    return 3

def generate_routing_matrix(nodes):
    matrix = {node: [] for node in nodes}
    for i, node in enumerate(nodes):
        neighbors = []
        if i > 0: neighbors.append(nodes[i-1])
        if i < len(nodes)-1: neighbors.append(nodes[i+1])
        matrix[node] = neighbors
    return matrix

def simulate_packet_loss(channel_noise, signal_strength):
    base_loss = 0.05
    if signal_strength < 30:
        base_loss += 0.2
    elif channel_noise > 75:
        base_loss += 0.15
    return round(base_loss, 4)

def estimate_latency(hop_count, congestion_factor):
    return hop_count * 12.5 * (1 + congestion_factor / 100)

def assess_redundancy(paths):
    primary, backup = paths['primary'], paths['backup']
    if len(primary) == 0 or len(backup) == 0:
        return False
    return set(primary) != set(backup)

def compute_crc32(data_chunk):
    # Simulated lightweight checksum
    crc = 0
    for char in data_chunk:
        crc ^= ord(char) << 8
        for _ in range(8):
            if crc & 0x8000:
                crc = (crc << 1) ^ 0x1021
            else:
                crc <<= 1
            crc &= 0xFFFF
    return crc

def normalize_signal(readings):
    avg = sum(readings) / len(readings)
    return [round(x / avg * 100, 2) for x in readings]

def detect_anomaly(metrics_log):
    threshold = 85
    anomalies = []
    for entry in metrics_log:
        if entry['utilization'] > threshold and entry['jitter'] > 20:
            anomalies.append(entry['timestamp'])
    return anomalies

def optimize_bandwidth(links, load_profile):
    # Core calculation
    total_capacity = 0
    for link in links.values():
        total_capacity += link['bandwidth']

    base_requirement = sum(load_profile) * 1.2
    efficiency_ratio = 0.88 if len(links) > 4 else 0.75

    adjusted_demand = base_requirement / efficiency_ratio

    # Determine bottleneck
    min_link_bw = min(link['bandwidth'] for link in links.values())
    max_link_bw = max(link['bandwidth'] for link in links.values())

    scaling_factor = 1.0
    if adjusted_demand > total_capacity * 0.9:
        scaling_factor = 1.3
    elif min_link_bw < 100:
        scaling_factor = 1.1

    proposed = (adjusted_demand * scaling_factor) / len(links)

    # Secondary adjustment based on traffic pattern
    peak_load = max(load_profile)
    if peak_load > 90:
        proposed *= 1.05
    elif peak_load < 30:
        proposed *= 0.95

    # Final smoothing
    final_value = int(round(proposed / 25) * 25)  # Round to nearest 25 Mbps

    return final_value

# Irrelevant helper - distractor
def encrypt_payload(data, key):
    shifted = ''n    for c in data:
        shifted += chr((ord(c) + key - 32) % 95 + 32)
    return shifted

# Irrelevant constant - red herring
MAX_RETRIES = 7
RETRY_DELAY_MS = 250

# Simulated network nodes
nodes = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta']
routing_table = generate_routing_matrix(nodes)

# Link definitions with specs - relevant data
link_matrix = {
    'l1': {'src': 'alpha', 'dst': 'beta', 'bandwidth': 200, 'latency': 15},
    'l2': {'src': 'beta', 'gamma': 'gamma', 'bandwidth': 150, 'latency': 20},
    'l3': {'src': 'gamma', 'dst': 'delta', 'bandwidth': 100, 'latency': 25},
    'l4': {'src': 'delta', 'epsilon': 'epsilon', 'bandwidth': 180, 'latency': 18},
    'l5': {'src': 'epsilon', 'dst': 'zeta', 'bandwidth': 120, 'latency': 22},
    'l6': {'src': 'zeta', 'dst': 'alpha', 'bandwidth': 160, 'latency': 19}
}

# Traffic load profile (in Mbps) - relevant input
traffic_load = [45, 67, 89, 54, 76, 61, 72, 58]

# Dead function - unused path
def fallback_route_config():
    return [{'hop': node, 'seq': i} for i, node in enumerate(nodes[::-1])]

# Misleading intermediate computation
aggregate_throughput = sum(link['bandwidth'] for link in link_matrix.values()) // len(link_matrix)  # Irrelevant average

# Signal readings - decoy data
signal_levels = [88, 76, 91, 85, 79, 93]
normalized_signals = normalize_signal(signal_levels)

# Simulated packet loss rate - irrelevant to final answer
loss_rate = simulate_packet_loss(channel_noise=68, signal_strength=82)

# CRC test - distractor operation
test_checksum = compute_crc32("network_frame_2024")

# Anomaly detection log - dead end
event_log = [
    {'timestamp': 1001, 'utilization': 78, 'jitter': 18},
    {'timestamp': 1002, 'utilization': 88, 'jitter': 22},
    {'timestamp': 1003, 'utilization': 92, 'jitter': 25}
]
anomalies_detected = detect_anomaly(event_log)

# Unused path configuration
path_options = {
    'primary': ['alpha', 'beta', 'gamma'],
    'backup': ['zeta', 'epsilon', 'delta']
}
redundant_paths = assess_redundancy(path_options)

# Critical execution point
final_bandwidth = optimize_bandwidth(link_matrix, traffic_load)

# Output result
print(f"Result: {final_bandwidth}")