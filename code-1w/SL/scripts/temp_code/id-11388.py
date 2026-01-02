from collections import defaultdict

# Simulate a water distribution network with pressure zones and flow measurements
pressure_zones = ['A', 'B', 'C', 'D']
time_intervals = [0, 1, 2, 3, 4]

# Sensor readings (inflow in liters per minute)
sensor_data = {
    'A': [120, 135, 140, 130, 150],
    'B': [95, 100, 98, 105, 110],
    'C': [70, 72, 75, 73, 70],
    'D': [60, 65, 68, 70, 72]
}

# Fault detection flags from diagnostic system (irrelevant to final calculation)
fault_flags = defaultdict(bool)
fault_flags['sensor_A2'] = False
fault_flags['sensor_C1'] = True  # Known minor glitch, data still valid

# Historical average baseline (distractor computation)
historical_avg = {}
for zone, readings in sensor_data.items():
    historical_avg[zone] = sum(readings) / len(readings)

# Calculate peak flows for stress analysis (semi-relevant, not used in final answer)
peak_flows = {zone: max(readings) for zone, readings in sensor_data.items()}

# Identify anomalous spikes (dead code path - not used later)
anomalies = []
for zone, readings in sensor_data.items():
    for i, val in enumerate(readings):
        if val > 1.5 * historical_avg[zone]:
            anomalies.append((zone, i, val))

# Extract last recorded inflow values for real-time monitoring (distractor)
live_inflows = [readings[-1] for readings in sensor_data.values()]

# Outflow measurements from drainage subsystems (some are inactive)
drainage_data = {
    'drain_1': [50, 55, 60, 58, 65],
    'drain_2': [40, 42, 45, 44, 46],
    'drain_3': [30, 35, 38, 36, 39],
    'drain_4': [20, 22, 25, 24, 26]
}

# Compute total outflows at each interval (only last interval matters)
cumulative_outflows = [0] * len(time_intervals)
for drain_readings in drainage_data.values():
    for t in range(len(time_intervals)):
        cumulative_outflows[t] += drain_readings[t]

# System efficiency ratio (irrelevant calculation)
efficiency_ratio = sum(peak_flows.values()) / sum(cumulative_outflows)

# Active control valves status (misleading state tracking)
valve_status = {f'valve_{i}': True for i in range(1, 9)}
valve_status['valve_3'] = False  # Manually closed

# Determine effective inflows based on sensor reliability (conditionally filtered)
effective_inflows = []
reliability_scores = {'A': 1.0, 'B': 0.98, 'C': 0.95, 'D': 0.97}
for i, zone in enumerate(pressure_zones):
    weighted_contribution = sensor_data[zone][-1] * reliability_scores[zone]
    effective_inflows.append(weighted_contribution)

# Final net flow calculation at last time step
inflows = [sensor_data[zone][-1] for zone in pressure_zones]
outflows = [drain_readings[-1] for drain_readings in drainage_data.values()]
net_flow = sum(inflows) - sum(outflows)

# Additional irrelevant aggregation
weighted_net = sum(effective_inflows) - sum(outflows)

# Print result as required
Result: net_flow