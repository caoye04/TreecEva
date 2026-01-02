import itertools

# Simulate environmental sensor readings with calibration
temperatures = [22.5, 23.0, 21.8, 24.1, 22.9]
humidity_readings = [45, 47, 46, 44, 48]

# Calibration offset from factory specs
base_calibration = 1013.25
offset_adjustment = sum([abs(t - 22.7) for t in temperatures]) * 0.1
adjusted_base = base_calibration - offset_adjustment

# Derived metrics
temperature_factor = 0.0
for t in temperatures:
    if t > 22.5:
        temperature_factor += (t - 22.5) ** 1.2

# Compression analysis from mechanical subsystem
compression_cycles = list(itertools.combinations([1, 2, 3, 4], 2))
compression_ratio = len(compression_cycles) * 0.15

# Dummy tracking variables (not used in final result)
tracking_log = []
cycle_power = 0.0
for i, cycle in enumerate(compression_cycles):
    cycle_power += (cycle[1] - cycle[0]) * 0.05
    tracking_log.append(f'Cycle {i}: {cycle}')

# Environmental interference correction (unused in final path)
humidity_index = 0
for h in humidity_readings:
    if h > 45:
        humidity_index += 1
humidity_correction = humidity_index * 0.02  # Not applied

# Final pressure calculation
final_pressure = adjusted_base + (temperature_factor * compression_ratio)

# Red herring: formatting unrelated data
device_id = 'SENSOR-XP'
status_flag = device_id.startswith('S') and len(tracking_log) > 5
metadata_summary = f"Status: {status_flag}, Cycles: {len(compression_cycles)}"

# Output result
print(f"Result: {final_pressure}")