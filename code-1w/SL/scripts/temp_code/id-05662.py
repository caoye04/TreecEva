from collections import defaultdict

# Simulate sensor readings over time
time_series_data = [12, 15, 8, 23, 17]
sensor_readings = defaultdict(int)

for t, value in enumerate(time_series_data):
    sensor_readings[t] = value * 0.75

# Initial system parameters
total_output = sum(sensor_readings.values())
operating_mode = 'high'
efficiency_bonus = 3.5 if operating_mode == 'high' else 1.0

# Irrelevant auxiliary variable (minimal distraction)
aux_correction = 0.98

# Core computation block
base_reading = sensor_readings[2]
safety_margin = 4.2
energy_level = base_reading + (total_output / 5)

# Key statement
energy_threshold = max(0, energy_level + efficiency_bonus - safety_margin)

# Output result
print(f"Result: {energy_threshold}")