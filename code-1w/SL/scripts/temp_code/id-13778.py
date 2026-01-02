from collections import defaultdict

# Simulate sensor data processing for fluid dynamics monitoring
tank_readings = [
    ('A1', 45.2), ('B2', 30.1), ('A1', 15.8), ('C3', 40.0),
    ('B2', 19.9), ('D4', 50.5), ('C3', 10.0), ('A1', 25.0)
]

# Track cumulative readings per sensor
reading_count = defaultdict(int)
sensor_totals = defaultdict(float)
for sensor_id, value in tank_readings:
    reading_count[sensor_id] += 1
    sensor_totals[sensor_id] += value

# Compute average per sensor (distraction: not directly used)
sensor_averages = {}
for sensor in sensor_totals:
    sensor_averages[sensor] = sensor_totals[sensor] / reading_count[sensor]

# Classify flow direction based on prefix (A,C = inflow; B,D = outflow)
inflow_sensors = [s for s in sensor_totals.keys() if s[0] in 'AC']
outflow_sensors = [s for s in sensor_totals.keys() if s[0] in 'BD']

# Sum total contributions
inflow_sum = sum(sensor_totals[s] for s in inflow_sensors)
outflow_sum = sum(sensor_totals[s] for s in outflow_sensors)

# Key computation point
net_flow = inflow_sum - outflow_sum

# Red herring: normalize by number of unique sensors (not affecting net_flow)
unique_sensor_count = len(sensor_totals)
normalized_flow = net_flow / unique_sensor_count if unique_sensor_count else 0

# Irrelevant transformation using enumerate and zip
index_labels = [f'Sensor_{i}' for i in range(len(sensor_averages))]
combined_data = list(zip(index_labels, sorted(sensor_averages.keys()), enumerate([round(v, 2) for v in sorted(sensor_averages.values())])))

# Final result output
print(f"Result: {net_flow}")