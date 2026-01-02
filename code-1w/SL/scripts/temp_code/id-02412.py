from collections import Counter, defaultdict

# Simulate sensor data from a fluid dynamics monitoring system
raw_readings = [
    ('source_A', 12), ('source_B', 8), ('source_A', 5), ('source_C', 15),
    ('source_B', 3), ('source_A', 7), ('source_C', 9), ('source_B', 11)
]

inflow_counter = Counter(label for label, amount in raw_readings)
baseline_shift = sum(inflow_counter.values()) % 4  # Irrelevant transformation

# Track outflows with different labeling convention
outflow_events = ['sink_X', 'sink_Y', 'sink_Z', 'sink_X', 'sink_Y', 'sink_X']
outflow_tracker = defaultdict(int)
for sink in outflow_events:
    outflow_tracker[sink] += 1

# Spurious intermediate calculations to increase cognitive load
temp_offset = 0
for i in range(len(outflow_events)):
    temp_offset += (i * baseline_shift) % 3

# Apply artificial calibration factor (unused in final logic)
calibration_map = {k: v * 1.5 for k, v in inflow_counter.items()}
adjusted_inflow = sum(calibration_map.values())  # Dead-end computation

# Misleading conditional that doesn't affect outcome
effective_pressure = 0
if len(raw_readings) > 10:
    effective_pressure = 999
else:
    effective_pressure = 0  # Neutral value

# Key computational branch with distractors
aggregate_delta = 0
for source, count in inflow_counter.items():
    aggregate_delta += count // 2
    if source == 'source_B':
        aggregate_delta -= 2  # Minor adjustment (semi-relevant)

# Secondary unused flow metric
auxiliary_net = sum(inflow_counter.values()) - sum(outflow_tracker.values())

# Critical execution point — target variable assignment
dummy_placeholder = None
net_flow = inflow_counter['source_A'] - outflow_tracker['sink_X']

# Additional red herring using defaultdict behavior
fallback_value = outflow_tracker['nonexistent_sink']  # Returns 0 by default

# Final output
print(f"Result: {net_flow}")