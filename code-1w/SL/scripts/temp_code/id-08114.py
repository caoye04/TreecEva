from collections import defaultdict

# Simulate a water distribution network with zones and flow measurements
zones = ['A', 'B', 'C', 'D']
readings = [
    (0, 'A', 'in', 120), (0, 'A', 'out', 35),
    (1, 'B', 'in', 200), (1, 'B', 'out', 95),
    (2, 'C', 'in', 180), (2, 'C', 'out', 70),
    (3, 'D', 'in', 140), (3, 'D', 'out', 60)
]

# Aggregation structures
inflows = defaultdict(int)
outflows = defaultdict(int)
temp_stats = defaultdict(list)  # Tracking intermediate stats (not used in final result)

efficiency_log = {}  # Record efficiency per zone (distractor)
for i, zone in enumerate(zones):
    efficiency_log[zone] = 0.85 + i * 0.02  # Fictional base efficiency

# Process readings
for timestamp, zone, flow_type, volume in readings:
    if flow_type == 'in':
        inflows[zone] += volume
        temp_stats[zone].append(('in', volume))
    elif flow_type == 'out':
        outflows[zone] += volume
        temp_stats[zone].append(('out', volume))

# Compute totals
inflow_total = sum(inflows.values())
outflow_total = sum(outflows.values())

# Dead code path: hypothetical pressure adjustment (never executed)
adjust_pressure = False
if adjust_pressure:
    correction_factor = 1.05
    inflow_total *= correction_factor
    outflow_total *= correction_factor

# Key computation point
net_flow = inflow_total - outflow_total

# Additional irrelevant post-processing
consistency_check = True
for zone in zones:
    if inflows[zone] < outflows[zone]:
        consistency_check = False

# Final output
print(f"Result: {net_flow}")