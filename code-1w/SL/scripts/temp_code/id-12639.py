from itertools import cycle

# Simulate environmental sensor fusion with calibration logic
temperature_readings = [23.5, 24.1, 22.9, 25.0, 23.8]
humidity_readings = [45, 47, 50, 44, 46]
pressure_offsets = [0.12, -0.08, 0.15, -0.10, 0.07]

# Calibration constants
base_calibration = 1013.25
temp_sensitivity = 0.2
humidity_compensation = 0.03

# Tracking variables (some are just for logging or debugging)
avg_temp = sum(temp for temp in temperature_readings) / len(temperature_readings)
avg_humidity = sum(hum for hum in humidity_readings) / len(humidity_readings))
raw_offset_avg = sum(pressure_offsets) / len(pressure_offsets)

total_drift = 0.0
for i, offset in enumerate(pressure_offsets):
    if i % 2 == 0:
        total_drift += offset * 1.1
    else:
        total_drift -= offset * 0.9

# Intermediate derived values
adjusted_base = base_calibration + (avg_temp - 20) * temp_sensitivity
humidity_effect = (avg_humidity - 40) * humidity_compensation

# Simulate cyclic pattern matching over sensor phases
sensor_cycle = cycle([1, -1, 0])
cycle_sum = 0
for i in range(len(temperature_readings)):
    cycle_sum += next(sensor_cycle) * temperature_readings[i] % 3

# Irrelevant aggregation (distractor)
peak_fluctuation = max(pressure_offsets) - min(pressure_offsets)
stability_score = 100 - (peak_fluctuation * 10)

# Key computational chain
valid_count = 0
dynamic_offset = 0.0
for i in range(len(pressure_offsets)):
    if humidity_readings[i] > 45:
        dynamic_offset += pressure_offsets[i]
        valid_count += 1

dynamic_offset = dynamic_offset / valid_count if valid_count > 0 else 0

scaling_factor = 1.0
if avg_temp > 23:
    scaling_factor *= 1.05
if avg_humidity < 48:
    scaling_factor *= 0.98

# Critical assignment point
final_pressure = adjusted_base + dynamic_offset * scaling_factor
print(f"Result: {final_pressure}")