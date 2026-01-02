from collections import Counter

# Simulate sensor readings for fluid flow analysis
tank_readings = [12, 15, 12, 18, 15, 20, 12]
flow_status = ['in', 'out', 'in', 'in', 'out', 'in', 'out']

counter = Counter(tank_readings)
inflow_values = []
outflow_values = []

for i, status in enumerate(flow_status):
    reading = tank_readings[i]
    if status == 'in':
        inflow_values.append(reading)
    else:
        outflow_values.append(reading)

inflow_sum = sum(inflow_values)
outflow_sum = sum(outflow_values)
net_flow = inflow_sum - outflow_sum

Result: net_flow