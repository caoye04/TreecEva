from collections import defaultdict

# Simulated sensor data processing for underwater drone diagnostics
telemetry_data = [3, 5, 2, 8, 5]
flow_rate = sum(telemetry_data) * 0.4
calibration_offset = 1.2

# System status tracking
depth = 78  # meters below surface
status_flags = defaultdict(bool)
status_flags['pump'] = True
status_flags['valve'] = (depth > 75)
status_flags['leak'] = False

# Irrelevant diagnostic counters (minimal distraction)
diag_counter_a = 0
for reading in telemetry_data:
    if reading % 2 == 0:
        diag_counter_a += 1

# Core computation with conditional logic and modular arithmetic
pressure_index = flow_rate * (depth // 10) + (status_flags['valve'] and depth % 10)

Result: pressure_index