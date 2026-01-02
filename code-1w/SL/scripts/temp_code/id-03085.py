import itertools

# Simulate environmental sensor data for temperature and altitude
temperatures = [22, 25, 19, 24, 27]
altitudes = [150, 180, 130, 160, 200]

# Initialize various system parameters
base_pressure = 1013.25
humidity_factor = 0.98
vibration_log = [0.1, 0.3, 0.2, 0.5]

# Misleading computation: vibration impact (not actually used in final result)
vibration_impact = 0
for reading in vibration_log:
    vibration_impact += reading ** 2

# Compute derived metrics using zip and enumerate
corrections = []
for i, (temp, alt) in enumerate(zip(temperatures, altitudes)):
    temp_adj = (temp - 20) * 2.5
    alt_adj = (alt - 100) * 0.12
    index_weight = i + 1
    correction = temp_adj - alt_adj
    corrections.append(correction)

# Accumulate total adjustment (only even-indexed matter)
total_adjustment = 0
for idx, corr in enumerate(corrections):
    if idx % 2 == 0:
        total_adjustment += corr

# Simulate pressure drop due to altitude and temperature drifts
adjusted_pressure = base_pressure - total_adjustment * 1.8

# Secondary distraction: process humidity sequence (dead-end path)
humidity_seq = [60, 65, 70, 62, 68]
humidity_index = 0
for h in humidity_seq:
    humidity_index += h % 10

# Efficiency factor depends on initial conditions
if len(temperatures) > 4:
    efficiency_factor = 0.92
else:
    efficiency_factor = 0.85

# Key statement
efficiency_factor += 0.03  # calibration offset
final_pressure = base_pressure * efficiency_factor

print(f"Result: {final_pressure}")