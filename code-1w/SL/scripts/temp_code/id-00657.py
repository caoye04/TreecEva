def calculate_node_load(node):
    base_load = node['cpus'] * node['memory_gb']
    efficiency_factor = 0.8 if node['active_sessions'] > 50 else 1.0
    return base_load * efficiency_factor

nodes = [
    {'cpus': 8, 'memory_gb': 32, 'active_sessions': 65},
    {'cpus': 4, 'memory_gb': 16, 'active_sessions': 30},
    {'cpus': 16, 'memory_gb': 64, 'active_sessions': 80}
]

loads = [calculate_node_load(node) for node in nodes]
total_load = sum(loads)
avg_load = total_load / len(loads)

threshold = 350
scaling_factor = 1.2 if avg_load > threshold else 1.0

initial_capacity = total_load * scaling_factor
maintenance_overhead = 50 if len(nodes) >= 3 else 25
final_capacity = int(initial_capacity - maintenance_overhead)

Result: final_capacity