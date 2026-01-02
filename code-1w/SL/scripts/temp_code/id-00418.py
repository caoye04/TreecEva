from collections import Counter, defaultdict

# Simulate data ingestion from multiple sources with routing logic
data_packets = [
    ('source_A', 'route_1', 120), ('source_B', 'route_1', 85), ('source_A', 'route_2', 90),
    ('source_C', 'route_3', 200), ('source_A', 'route_1', 45), ('source_B', 'route_2', 60)
]

# Track inflow by source using Counter for efficiency
temp_buffer = [pkt for pkt in data_packets if pkt[1] != 'route_X']  # filter out invalid route
inflow_counter = Counter()
for src, route, size in temp_buffer:
    inflow_counter[src] += size

# Initialize outflow tracking with default dictionary
outflow_tracker = defaultdict(int)
outflow_tracker['sink_Z'] = 150
outflow_tracker['sink_Y'] = 95
# Red herring: unused sink
outflow_tracker['sink_X'] = 300  

# Auxiliary computation: validate route balance (not directly used)
route_utilization = {}
for _, route, size in data_packets:
    route_utilization[route] = route_utilization.get(route, 0) + size

# Simulate packet loss adjustment (distractor logic)
packet_loss_rate = 0.05
adjusted_total = sum(inflow_counter.values()) * (1 - packet_loss_rate)

# Critical state variables
system_load = sum(outflow_tracker.values()) + len(data_packets)
threshold = 500 if system_load > 400 else 250

# Decision logic based on threshold (semi-relevant)
is_overloaded = adjusted_total > threshold

# Key computational step with conditional override (red herring)
effective_inflow = inflow_counter['source_A']
effective_inflow = effective_inflow * 0.9 if is_overloaded else effective_inflow

# Core result calculation
net_flow = inflow_counter['source_A'] - outflow_tracker.get('sink_Z', 0)

# Print final result as required
print(f"Result: {net_flow}")