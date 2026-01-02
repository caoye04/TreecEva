from collections import Counter, defaultdict

# Simulate network flow data across multiple nodes
raw_data = [
    ('source_A', 'node_1', 15),
    ('source_B', 'node_1', 10),
    ('node_1', 'node_2', 12),
    ('node_2', 'sink_X', 8),
    ('node_2', 'sink_Y', 4),
    ('source_A', 'node_3', 20),
    ('node_3', 'sink_X', 18),
    ('node_3', 'sink_Z', 2)
]

# Track inflow and outflow per node
inflow_counter = Counter()
outflow_counter = Counter()
node_capacity = defaultdict(int)

# Initialize capacity thresholds (distractor: not used in final logic)
capacity_config = {'node_1': 25, 'node_2': 20, 'node_3': 30}
for node, cap in capacity_config.items():
    node_capacity[node] = cap

# Process raw flow data
for src, dst, volume in raw_data:
    outflow_counter[src] += volume
    inflow_counter[dst] += volume

# Extra processing for unused diagnostic metrics (distractor)
diagnostic_ratios = {}
total_inflow = sum(inflow_counter.values())
total_outflow = sum(outflow_counter.values())
if total_inflow > 0:
    for node in inflow_counter:
        diagnostic_ratios[node] = round(inflow_counter[node] / total_inflow, 4)

# Additional irrelevant aggregation (distractor)
node_summary = {}
for node in set(inflow_counter.keys()) | set(outflow_counter.keys()):
    node_summary[node] = {
        'in': inflow_counter[node],
        'out': outflow_counter[node],
        'net': inflow_counter[node] - outflow_counter[node]
    }

# Critical computation point
net_flow = inflow_counter['source_A'] - outflow_counter['sink_X']

# Print result as required
print(f"Result: {net_flow}")