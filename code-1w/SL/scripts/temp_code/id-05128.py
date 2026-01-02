import itertools

# Sensor data calibration and noise filtering simulation
temp_readings = [23.5, 24.1, 19.8, 22.0, 25.3, 18.7, 26.0, 20.5]
threshold = 21.5
noise_floor = 19.0

calibrated_readings = [round(x * 1.02 + 0.5, 1) for x in temp_readings]
adjusted_readings = [x for x in calibrated_readings if x > noise_floor]
sorted_readings = sorted(adjusted_readings)

# Group consecutive readings within 0.5 range
grouped_readings = [list(group) for k, group in itertools.groupby(sorted_readings, key=lambda x: x // 0.5)]
largest_group = max(grouped_readings, key=len)

filtered_readings = [x for x in largest_group if x > threshold]
filtration_score = sum(filtered_readings)

Result: {filtration_score}