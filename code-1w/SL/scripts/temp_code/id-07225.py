def optimize_storage(nodes, threshold):
    active_nodes = [node for node in nodes if node['status'] == 'active']
    capacities = [node['capacity'] for node in active_nodes]
    sorted_caps = sorted(capacities, reverse=True)
    top_half = sorted_caps[:len(sorted_caps)//2]
    if not top_half:
        return 0
    avg_top = sum(top_half) / len(top_half)
    adjusted = [cap for cap in top_half if cap >= avg_top * 0.8]
    trimmed = adjusted[1:-1] if len(adjusted) > 2 else adjusted
    return sum(trimmed) // len(trimmed) if trimmed else 0

# System node configuration
test_nodes = [
    {'name': 'node_a1', 'capacity': 45, 'status': 'active'},
    {'name': 'node_a2', 'capacity': 60, 'status': 'inactive'},
    {'name': 'node_a3', 'capacity': 75, 'status': 'active'},
    {'name': 'node_a4', 'capacity': 30, 'status': 'active'},
    {'name': 'node_a5', 'capacity': 90, 'status': 'active'},
    {'name': 'node_a6', 'capacity': 50, 'status': 'active'},
    {'name': 'node_a7', 'capacity': 40, 'status': 'inactive'}
]
threshold = 50

# Irrelevant auxiliary variable (minimal distraction)
backup_schedule = ['daily', 'weekly']

final_capacity = optimize_storage(test_nodes, threshold)
print(f"Result: {final_capacity}")