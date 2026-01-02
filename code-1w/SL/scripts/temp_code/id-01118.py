from itertools import compress

# Sensor readings from three air quality monitors (in μg/m³)
monitor_a_readings = [45, 32, 58, 29, 61]
monitor_b_readings = [48, 30, 55, 33, 59]
monitor_c_readings = [44, 34, 57, 31, 63]

# Compute average particulate levels across all monitors per time interval
time_avg_levels = [(a + b + c) / 3 for a, b, c in zip(monitor_a_readings, monitor_b_readings, monitor_c_readings)]

# Determine valid intervals where system pressure is stable (simulated condition)
pressure_stable = [True, True, False, True, False]

# Filter readings using stable pressure intervals
filtered_readings = list(compress(time_avg_levels, pressure_stable))

# Calculate overall filtration efficiency as inverse ratio of average filtered level to baseline
baseline_pollution = 50.0
avg_filtered_level = sum(filtered_readings) / len(filtered_readings)
filt_ratio = avg_filtered_level / baseline_pollution
filtration_efficiency = int((1 - filt_ratio) * 100)  # Percentage efficiency

Result: filtration_efficiency