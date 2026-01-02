from itertools import combinations

# Network node efficiency readings over a period
efficiency_data = [85, 92, 78, 96, 88]

# Simulate derived network flow values based on pairwise interactions
deltas = []
for pair in combinations(efficiency_data, 2):
    deltas.append(abs(pair[0] - pair[1]))

# Aggregate flow per unique magnitude
delta_count = {}
for d in deltas:
    delta_count[d] = delta_count.get(d, 0) + 1

# Only consider significant flows (occurring at least twice)
significant_deltas = {k: v for k, v in delta_count.items() if v >= 2}

# Map each significant delta to a simulated network flow capacity
network_flow = {d: d * count for d, count in significant_deltas.items()}

# Key statement
flow_capacity = max(network_flow.values()) - min(network_flow.values())

# Irrelevant helper variable (minor distraction, intervention level 4)
temp_analysis = [x for x in efficiency_data if x > 80]

print(f"Result: {flow_capacity}")