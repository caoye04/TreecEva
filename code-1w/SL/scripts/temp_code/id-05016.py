from collections import Counter, defaultdict

# Simulate data ingestion from multiple sources with routing logic
data_packets = [
    ('source_A', 'route_X', 12), ('source_B', 'route_Y', 8),  ('source_A', 'route_X', 5),
    ('source_C', 'route_Z', 10), ('source_A', 'route_Y', 7),  ('source_B', 'route_X', 3),
    ('source_A', 'route_Z', 15), ('source_C', 'route_Y', 11), ('source_B', 'route_Z', 6)
]

# Track inflow by source
inflow_counter = Counter()
for src, route, size in data_packets:
    inflow_counter[src] += size

# Distractor: Count routes (not directly used in final answer)
route_frequency = Counter(route for src, route, size in data_packets)

# Simulate partial outflow tracking with incomplete mapping
outflow_tracker = defaultdict(int)
for _, dst, vol in [(r[1], r[1].split('_')[-1], r[2]) for r in data_packets if 'Z' in r[1]]:
    outflow_tracker[dst] += vol

# Auxiliary computation: normalize flows (irrelevant to final result)
normalized_outflows = {}
total_out = sum(outflow_tracker.values())
for k, v in outflow_tracker.items():
    normalized_outflows[k] = round(v / total_out, 4) if total_out > 0 else 0

# Dead code path: unused function
def calculate_latency(bandwidth):
    return 1000 / (bandwidth + 1e-5)

# Unused list comprehension
_ = [size**2 for src, route, size in data_packets if route == 'route_X']

# Key state variable updated through core logic
intermediate_balance = {}
for src in inflow_counter:
    intermediate_balance[src] = inflow_counter[src] // 2  # Arbitrary transformation

# Aggregate inflow for source_A and outflow for sink_Z
net_flow = 0
net_flow = inflow_counter['source_A'] - outflow_tracker.get('sink_Z', 0)

# Print final result as required
print(f"Result: {net_flow}")