from collections import defaultdict, Counter

# Simulated network node diagnostic system with red herrings and distractions

def analyze_node_health(node_data, threshold=0.85):
    # Irrelevant helper function (decoy)
    return sum(node_data.values()) / len(node_data) > threshold

def compute_bandwidth_weight(nodes):
    # Distractor computation - not used in final result
    total = 0
    for node in nodes:
        if 'bw' in node:
            total += node['bw'] * 0.7
    return total

def validate_checksum(log_entry):
    # Misleading function that looks important but isn't used
    return sum(ord(c) for c in log_entry) % 256

# Real data structures
network_nodes = [
    {'id': 'N1', 'load': 0.6, 'temp': 45, 'flags': [1,0,1], 'bw': 100},
    {'id': 'N2', 'load': 0.9, 'temp': 65, 'flags': [0,1,1], 'bw': 200},
    {'id': 'N3', 'load': 0.4, 'temp': 38, 'flags': [1,1,0], 'bw': 150},
    {'id': 'N4', 'load': 0.95, 'temp': 72, 'flags': [1,1,1], 'bw': 300}
]

system_log = [
    "ERR_CRITICAL:N4:VOLT",
    "INFO:HEALTHY:N1",
    "WARN:TEMP_HIGH:N2",
    "INFO:HEALTHY:N3",
    "ERR_CRITICAL:N4:OVERLOAD"
]

# Dead code path - unused class (red herring)
class DiagnosticCache:
    def __init__(self):
        self.cache = {}
    def get(self, key):
        return self.cache.get(key, 0)

# Irrelevant counters
temp_alerts = 0
voltage_issues = 0
for entry in system_log:
    if 'TEMP' in entry:
        temp_alerts += 1
    if 'VOLT' in entry:
        voltage_issues += 1

# Decoy data structure
checksum_map = {entry: validate_checksum(entry) for entry in system_log}

# Begin actual relevant logic (buried among distractions)
node_loads = [node['load'] for node in network_nodes]
overloaded = [load for load in node_loads if load > 0.85]
high_temp_ids = [node['id'] for node in network_nodes if node['temp'] > 60]

# Critical dictionary operation
node_flag_summary = defaultdict(int)
for node in network_nodes:
    node_id = node['id']
    flag_sum = sum(node['flags'])
    node_flag_summary[node_id] = flag_sum

# Another irrelevant calculation
average_bandwidth = compute_bandwidth_weight(network_nodes)
peak_load = max(node_loads) * 1000  # Misleading scaling

# Core logic embedded within noise
error_counts = Counter()
for log in system_log:
    parts = log.split(':')
    if len(parts) >= 3:
        level = parts[0]
        node_id = parts[1]
        if level == "ERR_CRITICAL" and node_id.startswith('N'):
            error_counts[node_id] += 1

# Key intermediate step
consolidated_diagnostics = []
for node in network_nodes:
    node_id = node['id']
    base_score = node['load'] * 100
    flag_bonus = node_flag_summary[node_id] * 5
    error_penalty = error_counts.get(node_id, 0) * 15
    final_score = base_score + flag_bonus - error_penalty
    consolidated_diagnostics.append(final_score)

# Final aggregation function
def aggregate_metrics(nodes, log_entries):
    # Actual answer computation
    raw_values = consolidated_diagnostics  # Captured from outer scope
    adjusted = [val + 10 for val in raw_values if val < 80]  # Only some are adjusted
    if len(adjusted) == 0:
        adjusted = [min(raw_values) + 5]
    temperature_factor = len([n for n in nodes if n['temp'] > 50])
    # Final deterministic computation
    result = int(sum(adjusted) * (1 + temperature_factor * 0.1))
    return result

# Execution point of interest
final_diagnostic = aggregate_metrics(network_nodes, system_log)

# Print required output
print(f"Target result: {final_diagnostic}")