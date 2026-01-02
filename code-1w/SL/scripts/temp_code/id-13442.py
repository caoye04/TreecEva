from collections import defaultdict

# Simulate sensor readings over time
time_intervals = [1, 2, 3, 4, 5]
sensor_data = defaultdict(list)
sensor_data['flow_rate'].extend([68, 72, 76, 80, 85])
sensor_data['pressure'].extend([110, 115, 118, 117, 116])

# Track stability based on small fluctuations
delta_threshold = 3
pressure_stable = []
for i in range(1, len(sensor_data['pressure'])):
    diff = abs(sensor_data['pressure'][i] - sensor_data['pressure'][i-1])
    pressure_stable.append(diff < delta_threshold)

# Initial system state
flow_rate = sensor_data['flow_rate'][-1]
pressure_variance = sum(abs(a - b) for a, b in zip(sensor_data['pressure'], sensor_data['pressure'][1:]))

# Critical decision logic
critical_mass_reached = any(x > 75 for x in sensor_data['flow_rate'])
threshold_flag = (flow_rate > 75) and (pressure_stable.count(True) > 2)

# Irrelevant tracking variable (minor distraction)
status_log = [f"Time {t}: OK" for t in time_intervals if t % 2 == 0]

Result: threshold_flag