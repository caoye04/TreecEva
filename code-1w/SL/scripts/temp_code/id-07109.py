from collections import defaultdict

# Simulate sensor data for fluid flow in a chemical reactor
tank_flows = [
    ('in', 23.5), ('out', 5.2), ('in', 18.0), ('in', 12.3),
    ('out', 8.7), ('out', 4.1), ('in', 9.8)
]

flow_counter = defaultdict(int)
inflow_sum = 0.0
outflow_sum = 0.0

for direction, volume in tank_flows:
    flow_counter[direction] += volume
    if direction == 'in':
        inflow_sum += volume
    else:
        outflow_sum += volume

net_flow = inflow_sum - outflow_sum

# Additional unrelated metric (minor distraction)
peak_inflow = max([v for d, v in tank_flows if d == 'in'], default=0)

Result: {net_flow}