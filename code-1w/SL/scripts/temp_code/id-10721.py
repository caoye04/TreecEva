from collections import Counter, defaultdict

# Simulate data ingestion from multiple sources with routing logic
data_packets = ['source_A', 'source_B', 'source_A', 'source_C', 'source_B', 'source_A']
route_map = {'source_A': 'path_1', 'source_B': 'path_2', 'source_C': 'path_1'}
traffic_log = []

inflow_counter = Counter(data_packets)
outflow_tracker = defaultdict(int)
outflow_tracker['sink_X'] = 8
outflow_tracker['sink_Y'] = 3

# Misleading intermediate computations (distractors)
temp_aggregate = sum(inflow_counter.values()) * 2
cumulative_bias = temp_aggregate // len(route_map) if route_map else 0
shadow_buffer = [cumulative_bias ** 0.5]  # unused but plausible

# Simulated packet dispatch (some real, some irrelevant)
dispatched = 0
for src in inflow_counter:
    path = route_map[src]
    if 'path_1' in path:
        dispatched += inflow_counter[src]
        # Only source_A gets partially routed through sink_X
        if src == 'source_A':
            outflow_tracker['sink_X'] += inflow_counter[src] // 4

# Secondary distraction: cache warming for non-critical path
cache_state = {}
for i in range(3):
    cache_state[f'buffer_{i}'] = cumulative_bias * (i + 1)

# Key computation embedded in context
net_flow = inflow_counter['source_A'] - outflow_tracker.get('sink_X', 0)

# Final red herring: unused transformation
final_envelope = max(net_flow, 0) ** 2 + 1 if net_flow > 5 else net_flow

print(f'Result: {net_flow}')