from collections import defaultdict

# Simulate sensor readings across multiple zones over time
zones = ['A', 'B', 'C', 'D']
timestamps = range(10)
sensor_data = [
    {'A': 12, 'B': 8,  'C': 15, 'D': 3},
    {'A': 10, 'B': 9,  'C': 14, 'D': 5},
    {'A': 13, 'B': 7,  'C': 16, 'D': 4},
    {'A': 11, 'B': 10, 'C': 15, 'D': 6},
    {'A': 14, 'B': 6,  'C': 13, 'D': 2},
    {'A': 12, 'B': 8,  'C': 14, 'D': 5},
    {'A': 10, 'B': 9,  'C': 15, 'D': 3},
    {'A': 13, 'B': 7,  'C': 16, 'D': 4},
    {'A': 11, 'B': 10, 'C': 14, 'D': 6},
    {'A': 14, 'B': 6,  'C': 13, 'D': 2}
]

# Accumulate total readings per zone
zone_totals = defaultdict(int)
for record in sensor_data:
    for zone, value in record.items():
        zone_totals[zone] += value

# Compute high-frequency fluctuations (distraction)
fluctuations = {}
for zone in zones:
    values = [r[zone] for r in sensor_data]
    fluctuations[zone] = max(values) - min(values)

# Identify peak activity window (not used in final answer)
peak_window = None
max_total = 0
for i, record in enumerate(sensor_data):
    total = sum(record.values())
    if total > max_total:
        max_total = total
        peak_window = i

# Categorize zones by average level (semi-relevant)
avg_levels = {z: round(zone_totals[z] / len(sensor_data), 2) for z in zones}
high_activity = [z for z, v in avg_levels.items() if v >= 10]
low_activity = [z for z, v in avg_levels.items() if v < 10]

# Destructuring assignment with irrelevant components
inflow_zones, outflow_zones = ['A', 'C'], ['B', 'D']

# Sum inflows and outflows using list comprehensions and enumerate
inflow_sum = sum(zone_totals[z] for z in inflow_zones)
outflow_sum = sum(zone_totals[z] for z in outflow_zones)

# Introduce distracting calculation: weighted fluctuation index
weight_map = {'A': 1.1, 'B': 0.9, 'C': 1.2, 'D': 0.8}
weighted_fluctuation = sum(fluctuations[z] * weight_map[z] for z in zones)

# Core computation embedded among distractions
net_flow = inflow_sum - outflow_sum

# Additional red herring: transform data to uppercase keys (useless)
transformed_data = [{k.upper(): v for k, v in record.items()} for record in sensor_data]

# Print result as required
Result: {net_flow}