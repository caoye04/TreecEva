from collections import defaultdict, Counter

# Simulated system performance data across multiple nodes
telemetry_logs = [
    'nodeA:cpu=75,mem=82,freq=3.2,status=active',
    'nodeB:cpu=60,mem=45,freq=2.8,status=standby',
    'nodeC:cpu=90,mem=88,freq=3.4,status=active',
    'nodeD:cpu=40,mem=30,freq=2.5,status=active',
    'nodeE:cpu=65,mem=50,freq=2.9,status=standby'
]

# Misleading auxiliary data — irrelevant to final computation
dummy_weights = [0.1, 0.05, 0.2, 0.15, 0.08, 0.12, 0.07, 0.11, 0.04, 0.06]
correction_factor = sum(w ** 2 for w in dummy_weights) * 100  # Dead-end calculation

# Parse logs into structured data
def parse_logs(logs):
    parsed = []
    for log in logs:
        node_data = {}
        parts = log.split(':', 1)
        node_data['id'] = parts[0]
        attrs = parts[1].split(',')
        for attr in attrs:
            k, v = attr.split('=')
            try:
                node_data[k] = float(v) if k != 'status' else v
            except:
                node_data[k] = v
        parsed.append(node_data)
    return parsed

parsed_telemetry = parse_logs(telemetry_logs)

# Extract active nodes
active_nodes = [node for node in parsed_telemetry if node['status'] == 'active']
standby_nodes = [node for node in parsed_telemetry if node['status'] == 'standby']

# Irrelevant transformation on standby nodes (distractor)
standby_cpu_avg = sum(node['cpu'] for node in standby_nodes) / len(standby_nodes) if standby_nodes else 0
adjusted_standby = [sb['cpu'] - standby_cpu_avg for sb in standby_nodes]

# Focus on CPU and memory for active nodes
metric_data = [{'cpu': n['cpu'], 'mem': n['mem']} for n in active_nodes]

# Decoy function — never used but looks important
def compute_health_index(data_list):
    total_health = 0
    for entry in data_list:
        h = (100 - entry['cpu']) * 0.6 + (100 - entry['mem']) * 0.4
        if entry.get('freq', 3.0) > 3.0:
            h *= 1.1
        total_health += max(h, 0)
    return total_health / len(data_list)

# Another red herring: frequency-based priority map (unused)
freq_priority_map = defaultdict(int)
for node in parsed_telemetry:
    freq_band = int(node['freq'] // 0.5)
    freq_priority_map[freq_band] += 1

# Real processing begins: score each active node based on resource pressure
resource_pressure = []
for md in metric_data:
    pressure = (md['cpu'] * 0.7 + md['mem'] * 0.3) / 100.0  # Normalized load index
    resource_pressure.append(pressure)

# Apply non-linear penalty for high pressure (threshold > 0.7)
penalized_scores = [
    rp + (rp - 0.7)**2 if rp > 0.7 else rp
    for rp in resource_pressure
]

# Aggregate with weighted contribution based on original telemetry order
order_weights = [1.5, 1.2, 1.0, 0.8, 0.6][:len(penalized_scores)]  # Truncated to actual length
weighted_aggregation = sum(
    score * order_weights[i]
    for i, score in enumerate(penalized_scores)
)

# Secondary adjustment using character frequency from node IDs (subtle but valid)
all_node_ids = ''.join([n['id'] for n in parsed_telemetry])
id_char_freq = Counter(all_node_ids)
letter_bonus = sum(1 for c, cnt in id_char_freq.items() if cnt >= 2 and c.isalpha())

# Combine into final score
temp_base = weighted_aggregation * 100
fluctuation_metric = abs(temp_base - 80)  # Misleading term

# Final scoring logic — only this matters
final_score = temp_base + (letter_bonus * 5) - fluctuation_metric

# Output target result
print(f"Result: {final_score}")