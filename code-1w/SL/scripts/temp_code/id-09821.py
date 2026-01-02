def calculate_efficiency(sensors, threshold):
    active_zones = {zone for zone, val in sensors.items() if val > threshold}
    adjustment_factor = len(active_zones) * 0.85
    
    # Irrelevant tracking (minor distraction)
    inactive_count = len(sensors) - len(active_zones)
    temp_log = [sensors[zone] for zone in sorted(active_zones)]
    
    aggregate = sum(sensors[zone] for zone in active_zones)
    efficiency = aggregate * adjustment_factor
    return efficiency

# Sensor data from building climate system
sensor_readings = {
    'north_a': 23.5,
    'south_b': 19.1,
    'east_c': 27.3,
    'west_d': 20.8,
    'center_e': 24.0
}
base_threshold = 21.0

# Filtering logic using dictionary and set operations
filtered_sensors = {k: v for k, v in sensor_readings.items() if 'a' in k or 'e' in k}

# Core computation
thermal_capacity = calculate_efficiency(filtered_sensors, base_threshold)

# Output result
print(f"Result: {thermal_capacity}")