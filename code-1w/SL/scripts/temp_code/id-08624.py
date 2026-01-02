import itertools

# Sensor data calibration and noise filtering simulation
time_series_data = [1.2, 3.5, 2.1, 7.8, 4.0, 9.2, 6.3, 0.5]
baseline_threshold = 3.0
noise_floor = 1.0

# Apply moving window to detect valid peaks above threshold
cyclic_shift = itertools.cycle([0.1, -0.1])
adjusted_readings = [x + next(cyclic_shift) for x in time_series_data]

# Filter measurements that are both above baseline and not in noisy range
filtered_measurements = [val for val in adjusted_readings if val > baseline_threshold and val > noise_floor]

# Final aggregation step: compute total signal strength of filtered peaks
filtration_score = sum(filtered_measurements)

print(f"Result: {filtration_score}")