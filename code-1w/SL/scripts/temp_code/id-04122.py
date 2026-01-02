from collections import defaultdict

# Sensor data collection over multiple zones
sensor_readings = defaultdict(list)
sensor_readings['zone_A'].extend([23.5, 24.1, 22.9, 24.0])
sensor_readings['zone_B'].extend([25.6, 26.1, 25.8])
sensor_readings['zone_C'].append(21.3)

# Irrelevant metadata (minimal distraction)
deployment_date = '2023-11-05'
firmware_version = 'v2.1.0'

# Compute average temperature from valid zones
valid_zones = ['zone_A', 'zone_B']
all_temps = []
for zone in valid_zones:
    all_temps.extend(sensor_readings[zone])

raw_avg = sum(all_temps) / len(all_temps)
adjusted_avg = round(raw_avg, 1)

# Anomaly detection using simple lambda threshold filter
high_readings = list(filter(lambda x: x > 25.0, all_temps))
anomaly_count = len(high_readings)
anomaly_correction = anomaly_count * 0.3

# Final adjustment
final_temperature = adjusted_avg + anomaly_correction
print(f"Result: {final_temperature}")