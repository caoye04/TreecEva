from collections import Counter, defaultdict

# Simulate data flow monitoring in a distributed system
nodes = ['source_A', 'source_B', 'relay_C', 'sink_X', 'sink_Y']

# Raw event logs (simulated)
event_log = [
    ('ingest', 'source_A'), ('ingest', 'source_A'), ('ingest', 'source_B'),
    ('route', 'relay_C'), ('route', 'relay_C'), ('route', 'relay_C'),
    ('deliver', 'sink_X'), ('deliver', 'sink_X'), ('deliver', 'sink_Y')
]

# Track counts by type
inflow_counter = Counter(tag for tag, node in event_log if tag == 'ingest')
outflow_tracker = defaultdict(int)
for tag, node in event_log:
    if tag == 'deliver':
        outflow_tracker[node] += 1

# Auxiliary tracking (distraction: not used in final result)
processing_delays = [0.12, 0.08, 0.34, 0.21, 0.19, 0.27, 0.33, 0.29, 0.15]
total_delay = sum(processing_delays)
node_status = {node: 'active' for node in nodes}
node_status['relay_C'] = 'degraded'  # simulated failure

# Misleading intermediate computation (dead-end analysis)
critical_paths = 0
for src in ['source_A', 'source_B']:
    for sink in ['sink_X', 'sink_Y']:
        if src == 'source_B' and sink == 'sink_Y':
            critical_paths += 1

# State accumulation with red herring variables
buffer_load = 0
for _ in range(len(event_log)):
    buffer_load = (buffer_load + 1) % 3  # cycling state, irrelevant

# Core logic step: compute net flow for source_A vs sink_X
net_flow = inflow_counter['source_A'] - outflow_tracker.get('sink_X', 0)

# Additional distraction: unused health score
health_score = len(inflow_counter) * 10 - total_delay

# Final output
print(f"Result: {net_flow}")