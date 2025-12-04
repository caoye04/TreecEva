import itertools

def check_sensor_data(readings, threshold):
    # Check if any reading exceeds threshold
    return any(r > threshold for r in readings)

def validate_system_status(components):
    # System is valid if more than half components are operational
    operational_count = sum(1 for c in components if c)
    total_count = len(components)
    return operational_count > (total_count / 2)

# Sensor data from different monitoring stations
sensor_a = [23, 45, 67, 42, 19]
sensor_b = [56, 78, 23, 45, 91]
sensor_c = [34, 12, 89, 67, 54]

# Component status (True = operational, False = failed)
components_x = [True, False, True, True]
components_y = [False, True, False, True]
components_z = [True, True, False, False]

# Thresholds for different sensor types
threshold_normal = 75
threshold_critical = 90
threshold_warning = 60

# Process sensor data
sensor_results = [
    check_sensor_data(sensor_a, threshold_normal),
    check_sensor_data(sensor_b, threshold_critical),
    check_sensor_data(sensor_c, threshold_warning)
]

# Process component status
system_results = [
    validate_system_status(components_x),
    validate_system_status(components_y),
    validate_system_status(components_z)
]

# Generate all combinations of sensor alerts and system status
combinations = list(itertools.product(sensor_results, system_results))

# Tracking variables
total_alerts = sum(1 for s in sensor_results if s)
total_valid_systems = sum(1 for s in system_results if s)

# Calculate priority score (not used in final result)
priority_score = (total_alerts * 10) + (total_valid_systems * 5)

# Filter results based on complex conditions
filter_results = []
for sensor_alert, system_valid in combinations:
    # First condition: sensor alert with system valid
    condition_a = sensor_alert and system_valid
    
    # Second condition: no sensor alert with invalid system
    condition_b = (not sensor_alert) and (not system_valid)
    
    # Store both conditions for each combination
    filter_results.append((condition_a, condition_b))

# Count combinations where first condition is true but second is false
valid_combinations = len([c for c in filter_results if c[0] and not c[1]])

# Additional processing (not affecting final result)
false_positives = len([c for c in filter_results if not c[0] and c[1]])
combined_metric = valid_combinations - (false_positives * 0.5)

print(f"Result: {valid_combinations}")