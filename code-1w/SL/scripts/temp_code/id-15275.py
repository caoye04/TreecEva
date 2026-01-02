from collections import defaultdict

# Sensor data simulation with calibration offsets
temperature_offsets = [0.1, -0.3, 0.2, 0.0, -0.1]
pressure_readings = [101.2, 103.5, 98.7, 102.1, 99.4]

correction_factor = 1.05
base_threshold = 100.0
diagnostic_log = defaultdict(int)

# Analyze pressure deviations above threshold
for i, reading in enumerate(pressure_readings):
    if reading > base_threshold:
        diagnostic_log['above_threshold'] += 1
    else:
        diagnostic_log['below_threshold'] += 1

# Key computational statement
total_load = sum(pressure_readings) * correction_factor

# Additional logging (irrelevant to final result)
status_flag = 'OK' if diagnostic_log['above_threshold'] >= 3 else 'CALIBRATE'

print(f"Result: {total_load}")