from collections import defaultdict

# Simulate water flow monitoring across zones and timestamps
zones = ['A', 'B', 'C']
timestamps = [1, 2, 3, 4]

# Raw sensor data: (zone, time, flow_type, volume)
sensor_data = [
    ('A', 1, 'in', 15), ('A', 1, 'out', 8),
    ('A', 2, 'in', 20), ('A', 2, 'out', 12),
    ('B', 1, 'in', 10), ('B', 1, 'out', 5),
    ('B', 3, 'in', 25), ('B', 3, 'out', 18),
    ('C', 2, 'in', 30), ('C', 2, 'out', 22),
    ('C', 4, 'in', 17), ('C', 4, 'out', 9)
]

# Aggregation structures
inflows = defaultdict(float)
outflows = defaultdict(float)
total_events = 0
fake_accumulator = 0  # Distractor: used in dead logic

# Process all sensor readings
for zone, time, flow_type, volume in sensor_data:
    total_events += 1
    if flow_type == 'in':
        inflows[(zone, time)] += volume
    elif flow_type == 'out':
        outflows[(zone, time)] += volume

# Misleading secondary pass: computes unused metric
for (zone, time), vol in inflows.items():
    fake_accumulator += vol * 0.1  # Irrelevant computation

# Compute total inflow and outflow per zone-time, then aggregate
inflow_sum = sum(inflows.values())
outflow_sum = sum(outflows.values())

# Key computation point
net_flow = inflow_sum - outflow_sum

# Dead code path with unused helper
if False:
    def adjust_flow(x):
        return x * 1.05

# Print result for verification
print(f"Result: {net_flow}")