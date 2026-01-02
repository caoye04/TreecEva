def analyze_node_health(node_data, threshold=0.75):
    return sum(1 for val in node_data if val >= threshold)


def compute_entropy(values):
    from math import log2
    total = sum(values)
    if total == 0:
        return 0.0
    probabilities = [v / total for v in values if v > 0]
    entropy = -sum(p * log2(p) for p in probabilities)
    return round(entropy, 4)


def generate_checksum(sequence):
    # Irrelevant checksum function (dead code path)
    chk = 0
    for x in sequence:
        chk = (chk ^ x) << 1
        if chk > 255:
            chk = chk % 256
    return chk

# Simulated system telemetry data
node_a_telemetry = [0.82, 0.91, 0.67, 0.95, 0.73, 0.88]
node_b_telemetry = [0.54, 0.32, 0.77, 0.61, 0.83]
node_c_telemetry = [0.90, 0.93, 0.88, 0.91, 0.85]

# Misleading intermediate metrics
staging_metric_1 = sum(node_a_telemetry) * len(node_b_telemetry)
staging_metric_2 = max(node_c_telemetry) - min(node_a_telemetry)

# Core health indicators
a_health = analyze_node_health(node_a_telemetry)
b_health = analyze_node_health(node_b_telemetry)
c_health = analyze_node_health(node_c_telemetry)

# Hidden diagnostic flag
if a_health + b_health < 5:
    trigger_redundancy_protocol = True
else:
    trigger_redundancy_protocol = False

# System topology modeling using sets
primary_nodes = {'A', 'C'}
backup_nodes = {'B', 'D'}
active_nodes = primary_nodes.union({'B'}).difference({'D'})  # Results in {'A', 'B', 'C'}

# Load distribution simulation (irrelevant accumulation)
temp_load_log = []
for i in range(len(node_a_telemetry)):
    temp_load = 0
    for j in range(i + 1):
        if j < len(node_b_telemetry):
            temp_load += node_a_telemetry[j] * node_b_telemetry[j]
    temp_load_log.append(temp_load)

# Real-time anomaly tracking (unused structure)
anomaly_buffer = {f"event_{i}": 0 for i in range(5)}
for idx, val in enumerate(node_c_telemetry):
    if val > 0.9:
        anomaly_buffer[f"event_{idx % 5}"] += 1

# Critical system load profile
system_load = [
    sum(node_a_telemetry) / len(node_a_telemetry),
    sum(node_b_telemetry) / len(node_b_telemetry),
    sum(node_c_telemetry) / len(node_c_telemetry)
]

# Network node representation
class NetworkNode:
    def __init__(self, id, capacity, load_profile):
        self.id = id
        self.capacity = capacity
        self.load_profile = load_profile
        self.peak_usage = max(load_profile) if load_profile else 0

network_nodes = [
    NetworkNode('A', 100, node_a_telemetry),
    NetworkNode('B', 75,  node_b_telemetry),
    NetworkNode('C', 120, node_c_telemetry)
]

# Decoy aggregation function that is never called
def deprecated_aggregate(nodes):
    total = 0
    for n in nodes:
        total += n.capacity * len(n.load_profile)
    return total // 3

# Key computation with distractors
baseline_entropy = compute_entropy([a_health, b_health, c_health])
recovery_score = 100 - abs((a_health - b_health) * 10)  # Misleading score

# Main metric aggregation logic
health_counts = [a_health, b_health, c_health]
entropy_contribution = compute_entropy(health_counts)

# Set-based node validation
detected_nodes = {node.id for node in network_nodes}
missing_nodes = backup_nodes.difference(detected_nodes)  # {'D'}
validation_pass = len(missing_nodes) == 1 and 'C' in detected_nodes

# Final diagnostic calculation (target)
consistency_factor = 1.0 if trigger_redundancy_protocol else 1.25
load_balance_score = (system_load[0] + system_load[2]) / 2

# Actual answer computation buried in distractions
size_penalty = len(network_nodes) * 0.1
final_diagnostic = (
    (health_counts[0] * 2) + 
    (health_counts[2] * 3) + 
    int(entropy_contribution * 10) - 
    int(baseline_entropy) + 
    int(load_balance_score * 4)
) // 2

# Output target result
Result: {final_diagnostic}