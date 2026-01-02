def calculate_efficiency(data):
    base_efficiency = 0.85
    bonus_factor = 1.2 if sum(data) > 30 else 1.0
    return round(base_efficiency * bonus_factor * 100, 2)

# Sensor data from three monitoring stations
sensor_readings = [8, 12, 15]

# Apply scaling factor to each reading using list comprehension
target_zone = [x * 1.5 for x in sensor_readings if x >= 10]

# Transform data with offset adjustment
drift_correction = 2
target_zone_adjusted = [x + drift_correction for x in target_zone]

# Simulate secondary system state with lambda
system_status_check = lambda x: any(val > 14 for val in x)
active_status = system_status_check(target_zone_adjusted)

# Core calculation input
transformed_data = target_zone_adjusted

# Critical execution point
energy_output = calculate_efficiency(transformed_data)

print(f"Result: {energy_output}")