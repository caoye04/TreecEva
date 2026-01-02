from collections import defaultdict

# Simulate sensor readings over time for fluid dynamics monitoring
time_series_data = [
    (0, 'in', [23, 25, 22, 24]),
    (1, 'out', [12, 15]),
    (2, 'in', [20, 18, 21]),
    (3, 'out', [11, 13, 10, 9]),
    (4, 'in', [27]),
    (5, 'calibration', [0]),  # Irrelevant data type
    (6, 'in', [22, 23]),
    (7, 'out', [14, 16, 15])
]

inflow_readings = []
outflow_readings = []
diagnostic_log = defaultdict(int)
buffer_cache = []

# Process each time step
for timestamp, flow_type, readings in time_series_data:
    avg_reading = sum(readings) / len(readings)
    diagnostic_log[flow_type] += 1

    # Simulate buffer accumulation (only for diagnostics)
    buffer_cache.append((timestamp, avg_reading))

    if flow_type == 'in':
        inflow_readings.extend(readings)
    elif flow_type == 'out':
        outflow_readings.extend(readings)

# Misleading intermediate calculation (not used in final result)
redundant_ratio = len(inflow_readings) / (len(outflow_readings) + 1)

evaluation_scores = []
for i, val in enumerate(inflow_readings):
    score = val * (i % 3 + 1)  # Weighted scoring (distractor)
    evaluation_scores.append(score)

# Another red herring: correlation attempt between index and value
index_value_product = 0
for idx, val in enumerate(outflow_readings):
    index_value_product += idx * val

# Relevant calculations begin
inflow_total = sum(inflow_readings)
outflow_total = sum(outflow_readings)

# Key assignment point
net_flow = inflow_total - outflow_total

# Print result as required
print(f"Result: {net_flow}")