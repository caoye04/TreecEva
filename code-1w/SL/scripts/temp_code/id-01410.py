from itertools import compress

# Simulate sensor readings for fluid inflow and outflow in a processing unit
time_intervals = 5
inflow_readings = [105, 96, 112, 89, 101]
outflow_readings = [98, 97, 108, 90, 99]

# Validity flags based on sensor confidence (simulated)
sensor_stable = [True, True, False, True, True]

# Filter valid inflows using sensor stability mask
valid_inflows = list(compress(inflow_readings, sensor_stable))
valid_outflows = list(compress(outflow_readings, sensor_stable))

# Calculate net fluid flow after filtering unreliable readings
net_flow = sum(valid_inflows) - sum(valid_outflows)

# Auxiliary variable (irrelevant to main computation)
total_duration = time_intervals * 60  # total monitoring time in seconds

Result: net_flow