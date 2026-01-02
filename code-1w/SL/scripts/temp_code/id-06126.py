from collections import Counter, defaultdict

# Simulate data ingestion from multiple sensors
data_packets = [
    ('source_A', 'sensor_1', 145), ('source_B', 'sensor_2', 98),
    ('source_A', 'sensor_3', 211), ('source_C', 'sensor_1', 87),
    ('source_A', 'sensor_2', 156), ('source_B', 'sensor_4', 203)
]

# Track inflow by source
inflow_counter = Counter()
for source, sensor, packets in data_packets:
    inflow_counter[source] += packets

# Initialize outflow tracking with default behavior
outflow_tracker = defaultdict(int)
outflow_tracker['sink_X'] = 198
outflow_tracker['sink_Y'] = 89

# Process intermediate buffer (distractor: doesn't affect final answer)
temporary_buffer = []
for item in data_packets:
    transformed = (item[1], item[2] * 0.95)  # Simulate signal loss
    temporary_buffer.append(transformed)

# Aggregate buffer stats (irrelevant to net flow)
buffer_stats = {}
for sensor, adjusted_val in temporary_buffer:
    if sensor not in buffer_stats:
        buffer_stats[sensor] = []
    buffer_stats[sensor].append(adjusted_val)

# Compute average per sensor (dead code path)
avg_per_sensor = {}
for sensor, values in buffer_stats.items():
    avg_per_sensor[sensor] = sum(values) / len(values)

# Additional metadata processing (misleading computation)
signal_quality_score = 0
for val in inflow_counter.values():
    if val > 100:
        signal_quality_score += 1.5
signal_quality_score *= 0.7  # Unused metric

# Key state variables
active_sources = len(inflow_counter)
peak_inflow = max(inflow_counter.values())

# Critical calculation point
net_flow = inflow_counter['source_A'] - outflow_tracker.get('sink_X', 0)

# Irrelevant sorting operation (adds cognitive load)
sorted_inflows = sorted(inflow_counter.items(), key=lambda x: x[1], reverse=True)

# Print result for evaluation
print(f"Result: {net_flow}")