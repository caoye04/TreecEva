from collections import defaultdict

# Simulate hourly fluid flow measurements in a processing plant
inflow_readings = [120, 150, 130, 160, 140]
outflow_readings = [110, 135, 145, 130, 120]

daily_stats = defaultdict(int)
daily_stats['total_in'] = sum(inflow_readings)
daily_stats['total_out'] = sum(outflow_readings)

temperature_offset = 2.5  # Minor sensor calibration factor (irrelevant to main logic)
pressure_factor = 1.02   # Another sensor adjustment (distractor)

inflows = [val for val in inflow_readings if val > 125]
outflows = [val for val in outflow_readings if val < 140]

net_flow = sum(inflows) - sum(outflows)
Result: net_flow