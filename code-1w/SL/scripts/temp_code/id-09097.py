import math

def analyze_node_health(signal_strength, latency):
    # Irrelevant health check with decoy logic
    baseline = 75.0
    if signal_strength > 80:
        return baseline + 10
    elif latency < 20:
        return baseline + 5
    else:
        return baseline - 15


def compute_bandwidth_efficiency(data_rate, interference_level):
    # Complex but irrelevant efficiency formula
    adjusted_rate = data_rate * (1 - interference_level / 100)
    penalty = math.log(max(1, interference_level))
    return adjusted_rate / (penalty + 1)

# Unused function - red herring
def legacy_redundancy_check(nodes):
    return len([n for n in nodes if 'legacy' in n]) > 2

# Decoy variables
system_uptime_hours = 1273
maintenance_window = "weekly"
config_version = "v2.4.1"
reboot_required = False

# Real input data
network_nodes = [
    {'id': 'N001', 'type': 'router', 'signal': 85, 'latency': 18, 'data_rate': 92, 'interference': 30},
    {'id': 'N002', 'type': 'switch', 'signal': 76, 'latency': 25, 'data_rate': 88, 'interference': 22},
    {'id': 'N003', 'type': 'router', 'signal': 90, 'latency': 12, 'data_rate': 95, 'interference': 35},
    {'id': 'N004', 'type': 'bridge', 'signal': 65, 'latency': 45, 'data_rate': 60, 'interference': 50},
    {'id': 'N005', 'type': 'router', 'signal': 88, 'latency': 22, 'data_rate': 90, 'interference': 28}
]

system_load = [0.78, 0.82, 0.75, 0.85, 0.80, 0.77, 0.83, 0.79]
system_mode = "diagnostic"

temporal_weights = [math.sin(i * 0.5) ** 2 for i in range(len(system_load))]
weighted_load = sum(w * l for w, l in zip(temporal_weights, system_load))

# Distractor: complex string manipulation with no impact
log_header = "SYS_DIAG_2024"
header_parts = log_header.split('_')
version_tag = "_".join([header_parts[0], header_parts[1]]) + f"_{len(network_nodes)}"

# Fake aggregation path
redundant_sum = 0
for node in network_nodes:
    redundant_sum += len(node['id'])

# Real processing begins here
healthy_nodes = 0
bandwidth_scores = []

for node in network_nodes:
    health_score = analyze_node_health(node['signal'], node['latency'])
    if health_score > 80:
        healthy_nodes += 1
    
    efficiency = compute_bandwidth_efficiency(node['data_rate'], node['interference'])
    bandwidth_scores.append(efficiency)

# Misleading intermediate calculation
average_efficiency = sum(bandwidth_scores) / len(bandwidth_scores)
peak_efficiency = max(bandwidth_scores)

# Critical distractor: unused transformation
buffer_snapshot = "".join([n['id'][3:] for n in network_nodes])
segment_map = {i: ord(c) for i, c in enumerate(buffer_snapshot)}

# Real logic: determine diagnostic level based on healthy routers and load stability
router_count = len([n for n in network_nodes if n['type'] == 'router'])
stable_load = all(0.75 <= load <= 0.85 for load in system_load)

# Key computation
base_diagnostic = healthy_nodes * 100
if router_count >= 3 and stable_load:
    base_diagnostic += 50

# Final adjustment using slicing and dictionary lookup
status_lookup = {'low': 10, 'moderate': 25, 'high': 40}
load_status = 'moderate'
if weighted_load < 0.77:
    load_status = 'low'
elif weighted_load > 0.80:
    load_status = 'high'

adjustment_factor = status_lookup[load_status]

# Final statement
final_diagnostic = base_diagnostic + adjustment_factor
print(f"Result: {final_diagnostic}")