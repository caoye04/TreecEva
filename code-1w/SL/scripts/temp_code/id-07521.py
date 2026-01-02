import math

# Simulated network diagnostic tool with interference

def analyze_node_health(signal_strength, latency):
    if signal_strength > 75:
        return 'OPTIMAL'
    elif signal_strength > 40 and latency < 120:
        return 'STABLE'
    else:
        return 'CRITICAL'


def compute_bandwidth_capacity(frequency, channels=8):
    # Irrelevant calculation - decoy function
    base = frequency * channels
    overhead = base * 0.15
    return base - overhead


def detect_anomalies(log_data):
    # Dead code path - never actually used in final computation
    anomalies = []
    threshold = sum(log_data) / len(log_data) + 10
    for entry in log_data:
        if entry > threshold:
            anomalies.append(entry)
    return anomalies

# Distractor variables
system_uptime_hours = 973.2
maintenance_window = ["02:00", "04:00"]
redundant_flag = True
temporal_factor = 0.87
auxiliary_matrix = [[1, 2], [3, 4]]

# Core data structures
network_nodes = [
    {'id': 'N001', 'signal': 88, 'latency': 45, 'load': 67},
    {'id': 'N002', 'signal': 72, 'latency': 98, 'load': 83},
    {'id': 'N003', 'signal': 34, 'latency': 200, 'load': 41},
    {'id': 'N004', 'signal': 91, 'latency': 33, 'load': 76},
    {'id': 'N005', 'signal': 65, 'latency': 110, 'load': 54}
]

system_load = [67, 83, 41, 76, 54, 92, 61]  # Extra element to mislead

# Unused transformation
shifted_load = [x - 10 for x in system_load if x > 70]

# Decoy set operations (appear meaningful but unused)
critical_nodes_set = {node['id'] for node in network_nodes if node['signal'] < 50}
high_load_set = {node_id for node_id in ['N002', 'N005', 'N001'] if 'N' in node_id}
overlap_nodes = critical_nodes_set & high_load_set

# Real processing begins here — heavily masked by above noise
node_statuses = []
for node in network_nodes:
    status = analyze_node_health(node['signal'], node['latency'])
    node_statuses.append(status)

# Count nodes per category
status_count = {}
for status in node_statuses:
    status_count[status] = status_count.get(status, 0) + 1

# Compute health score based on status distribution
health_score = 0
if 'OPTIMAL' in status_count:
    health_score += status_count['OPTIMAL'] * 25
if 'STABLE' in status_count:
    health_score += status_count['STABLE'] * 15
if 'CRITICAL' in status_count:
    health_score -= status_count['CRITICAL'] * 40  # Penalty

# Aggregate using modular arithmetic and summation
raw_sum = sum(system_load)
mod_key = len(network_nodes) % 7 or 1
adjusted_sum = raw_sum % mod_key

# Real metric computation
average_load = sum(system_load) / len(system_load)
fluctuation_index = max(system_load) - min(system_load)

# Core logic: recursive load smoothing (actually used)
def smooth_load(data, depth=2):
    if depth == 0 or len(data) < 2:
        return data[0] if data else 0
    new_data = [(data[i] + data[i+1]) / 2 for i in range(len(data)-1)]
    return smooth_load(new_data, depth - 1)

smoothed_component = smooth_load(system_load)

# Final aggregation incorporating set-derived logic (only one set used meaningfully)
node_ids = [node['id'] for node in network_nodes]
used_ids_set = set(node_ids)  # Actually used

# Key statement
final_diagnostic = int(
    health_score 
    + math.floor(average_load) 
    - fluctuation_index // 3 
    + int(smoothed_component)
    + (50 if len(used_ids_set & {'N001', 'N004'}) == 2 else 0)  # Only this set op matters
)

Result: final_diagnostic