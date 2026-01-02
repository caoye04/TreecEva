from collections import defaultdict

# Network routing simulation with capacity optimization
nodes = ['A', 'B', 'C', 'D']
base_load = {'A': 12, 'B': 8, 'C': 15, 'D': 7}
redundancy_factor = 1.25

capacity_map = defaultdict(float)
for node in nodes:
    base = base_load[node]
    adjusted = base * redundancy_factor
    if adjusted > 10:
        adjusted *= 0.9  # efficiency discount for high-load nodes
    capacity_map[node] = adjusted

# Route optimization: select only high-throughput routes
optimized_routes = []
for node, cap in capacity_map.items():
    if cap >= 10:
        optimized_routes.append(cap)

total_capacity = sum(optimized_routes)

# Irrelevant tracking variable (minor distraction)
node_count = len(nodes)

print(f"Result: {total_capacity}")