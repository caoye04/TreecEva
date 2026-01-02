from collections import Counter, defaultdict

# Simulate data ingestion from multiple sensors
data_packets = [
    ('source_A', 'sensor_1', 12), ('source_B', 'sensor_2', 8), ('source_A', 'sensor_3', 5),
    ('source_C', 'sensor_1', 10), ('source_B', 'sensor_4', 7), ('source_A', 'sensor_2', 3)
]

# Track inflow by source
inflow_counter = Counter()
for src, sensor, count in data_packets:
    inflow_counter[src] += count

# Initialize various trackers (some are distractions)
temp_cache = {}
processing_flags = {'active': True, 'mode': 'batch'}
buffer_stats = defaultdict(int)
outflow_tracker = {}

# Simulate outflow registration (only partial sources logged)
outflow_events = [
    ('sink_X', 'source_A', 15),
    ('sink_Y', 'source_B', 5)
]

for sink, src, amount in outflow_events:
    if sink == 'sink_X':
        outflow_tracker[src] = outflow_tracker.get(src, 0) + amount
    else:
        # Misleading branch: not used later
        buffer_stats[sink] += amount

# Red herring computation: unused statistical summary
mean_packet_size = sum(c for _, _, c in data_packets) / len(data_packets)
peak_inflow = max(inflow_counter.values())

# Auxiliary diagnostic string processing (distraction)
diag_labels = [f"Node:{s.split('_')[1]}" for s in inflow_counter.keys()]
label_concat = ''.join(diag_labels).upper()
char_frequency = Counter(label_concat)

# Core state update: relevant assignment
net_flow = inflow_counter['source_A'] - outflow_tracker.get('sink_X', 0)

# Additional irrelevant state mutation
temp_cache['last_calc'] = 'completed'
processing_flags['updated'] = True

# Final output (must print result in required format)
print(f"Result: {net_flow}")