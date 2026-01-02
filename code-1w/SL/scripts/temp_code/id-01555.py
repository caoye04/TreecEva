from collections import defaultdict

# Simulate a water distribution network with zones and flow measurements
zones = ['A', 'B', 'C', 'D']
readings = [
    ('A', 'in', 120), ('A', 'out', 45),
    ('B', 'in', 89), ('B', 'out', 34),
    ('C', 'in', 150), ('C', 'out', 67),
    ('D', 'in', 200), ('D', 'out', 98),
    ('A', 'in', 55), ('B', 'in', 41)
]

# Aggregates for flow analysis
flow_data = defaultdict(lambda: {'in': 0, 'out': 0})
temp_buffer = []  # Unused buffer (distractor)

# Process readings into structured flow data
for zone, direction, volume in readings:
    if direction in ['in', 'out']:
        flow_data[zone][direction] += volume

# Compute totals with intermediate tracking
inflow_total = 0
outflow_total = 0
loss_report = []  # Logged anomalies (semi-relevant)
consistency_check = True  # Placeholder for validation (not used later)

for zone in zones:
    inflow_total += flow_data[zone]['in']
    outflow_total += flow_data[zone]['out']
    
    # Calculate theoretical loss per zone (not directly used in final answer)
    theoretical_loss = flow_data[zone]['in'] * 0.05  # 5% expected evaporation
    actual_loss = flow_data[zone]['in'] - flow_data[zone]['out']
    if actual_loss > theoretical_loss * 1.5:
        loss_report.append((zone, actual_loss))

# Key statement: compute net flow into the system
net_flow = inflow_total - outflow_total

# Additional irrelevant computation (distractor)
dummy_scaling = 1.0
for i in range(2):
    dummy_scaling *= 0.95
scaled_net = net_flow * dummy_scaling  # Not printed or used

# Final output
print(f"Result: {net_flow}")