from collections import defaultdict

# System resource simulation for a cluster
node_list = ['alpha', 'beta', 'gamma', 'delta']
base_power = [120, 85, 95, 110]
efficiency_ratio = [0.88, 0.92, 0.85, 0.90]

# Irrelevant metric (distractor)
avg_temperature = [23.5, 24.1, 22.8, 25.0]

# Map node to adjusted capacity using efficiency and base power
capacity_map = defaultdict(float)
for i, node in enumerate(node_list):
    raw_capacity = base_power[i] * efficiency_ratio[i]
    if raw_capacity > 90:
        capacity_map[node] = round(raw_capacity, 2)

# Add a fixed backup node manually
capacity_map['backup'] = 50.0

# Key computation point
max_node = max(capacity_map, key=capacity_map.get)
capacity_per_critical = {k: v / 10 for k, v in capacity_map.items() if v > 60}
total_capacity = sum(capacity_map.values())

# Print result for verification
print(f"Result: {total_capacity}")