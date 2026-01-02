from collections import Counter, defaultdict

# Simulate data ingestion from multiple sensors
data_packets = [
    ('source_A', 'sensor_X', 12),
    ('source_B', 'sensor_Y', 8),
    ('source_A', 'sensor_Z', 15),
    ('source_C', 'sensor_X', 5),
    ('source_A', 'sensor_X', 3)
]

# Track inflow counts by source
inflow_counter = Counter()
for src, sensor, val in data_packets:
    inflow_counter[src] += 1
    inflow_counter[sensor] += 0  # Red herring: tracking sensors as sources (not used)

# Simulate partial outflow records (some data lost)
outflow_logs = [('sink_Z', 'source_A'), ('sink_Z', 'source_B'), ('sink_Y', 'source_A')]
outflow_tracker = defaultdict(int)
backup_count = 0
for sink, src in outflow_logs:
    outflow_tracker[sink] += 1
    if src == 'source_A':
        backup_count += 1  # Irrelevant metric, not used later

# Auxiliary debug calculation - dead code path
if len(data_packets) > 4:
    avg_packet_size = sum(v for _, _, v in data_packets) / len(data_packets)
    size_category = 'large' if avg_packet_size > 10 else 'small'

# Critical state variables
temp_offset = inflow_counter['source_C'] * 2  # Unused but plausible
reference_flow = inflow_counter['source_A'] + inflow_counter['source_B']  # Semi-relevant

# Key computation point
disruption_flag = len(outflow_logs) < 5 and 'sensor_Z' in inflow_counter  # Evaluates to True
net_flow = 0
if disruption_flag:
    net_flow = inflow_counter['source_A'] - outflow_tracker.get('sink_Z', 0)

# Print result for evaluation
print(f"Result: {net_flow}")