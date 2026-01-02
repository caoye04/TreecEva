from collections import defaultdict, Counter

def analyze_node_health(metrics):
    healthy = []
    for node, values in metrics.items():
        cpu_avg = sum(values['cpu']) / len(values['cpu'])
        mem_avg = sum(values['memory']) / len(values['memory'])
        if cpu_avg < 75 and mem_avg < 80:
            healthy.append(node)
    return set(healthy)

def balance_workload(node_loads, threshold):
    total_load = sum(node_loads.values())
    adjusted_loads = defaultdict(float)
    overflow_nodes = []

    for node, load in node_loads.items():
        if load > threshold:
            adjusted_loads[node] = threshold
            overflow = load - threshold
            overflow_nodes.append((node, overflow))
        else:
            adjusted_loads[node] = load

    # Distribute overflow proportionally among underloaded nodes
    available_capacity = 0
    eligible_nodes = []
    for node, load in node_loads.items():
        if load <= threshold:
            available_capacity += threshold - load
            eligible_nodes.append(node)

    distributed_overflow = 0
    if available_capacity > 0 and overflow_nodes:
        total_overflow = sum(ov[1] for ov in overflow_nodes)
        distribution_ratio = min(1.0, available_capacity / total_overflow) if total_overflow > 0 else 0
        per_node_share = total_overflow * distribution_ratio / len(eligible_nodes) if eligible_nodes else 0
        
        for en in eligible_nodes:
            adjusted_loads[en] += per_node_share
            distributed_overflow += per_node_share

    # Dummy computation: simulate logging overhead (irrelevant to final result)
    log_entry = f"Distributed {distributed_overflow:.2f} units across {len(eligible_nodes)} nodes"
    dummy_counter = Counter(log_entry.split())
    noise_value = sum(dummy_counter.values()) * 0.01  # Not used

    # Final aggregation step
    final_total = sum(adjusted_loads.values())
    scaling_factor = total_load / final_total if final_total != 0 else 1
    for node in adjusted_loads:
        adjusted_loads[node] *= scaling_factor

    return sum(v for k, v in adjusted_loads.items() if 'primary' in k)

# Simulated system metrics (not directly used but adds context)
metrics = {
    'node-alpha': {'cpu': [60, 65, 70], 'memory': [60, 70, 65]},
    'node-beta': {'cpu': [80, 85, 90], 'memory': [85, 80, 88]},
    'node-primary-gamma': {'cpu': [50, 55, 60], 'memory': [50, 55, 60]},
    'node-backup-delta': {'cpu': [70, 68, 72], 'memory': [75, 70, 74]}
}

# Main workload data
node_loads = {
    'node-alpha': 120.0,
    'node-beta': 150.0,
    'node-primary-gamma': 80.0,
    'node-backup-delta': 60.0
}
threshold = 100.0

# Irrelevant pre-processing (adds distraction)
data_stream = ['load', 'peak', 'spike', 'normal', 'burst']
enumerated_tags = [f'{i}-{tag}' for i, tag in enumerate(data_stream)]
filtered_tags = [tag for tag in enumerated_tags if 'e' in tag]
joined_string = '-'.join(filtered_tags)
char_count_map = {c: joined_string.count(c) for c in 'abcdefghijklmnopqrstuvwxyz'}

# Key execution point
final_load = balance_workload(node_loads, threshold)

# Output result
print(f"Result: {final_load}")