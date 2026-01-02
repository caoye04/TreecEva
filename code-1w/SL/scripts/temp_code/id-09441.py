from itertools import compress

# Simulate sensor data readings for system load over time
raw_sensor_data = [98, 102, 110, 95, 120, 125, 130, 118, 140, 138, 150]

time_of_day_flags = [True, True, False, True, False, True, True, False, True, True, False]  # Irregular sampling

# Filter valid readings taken during calibration windows
system_loads_filtered = list(compress(raw_sensor_data, time_of_day_flags))

# Apply dynamic threshold adjustment based on operational mode
if sum(system_loads_filtered) > 600:
    system_loads_filtered = [x * 0.95 for x in system_loads_filtered]

# Critical assessment point
peak_capacity = max(system_loads_filtered)

# Output result
print(f"Result: {peak_capacity}")