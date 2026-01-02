from collections import defaultdict

# Simulate sensor data with some noise
raw_readings = [105, 98, -999, 102, 97, -999, 100, 101, 99]

# Placeholder for cleaned and adjusted values
adjusted_readings = []
sensor_offset = 2
disregard_flag = -999

# Clean data: remove invalid readings and apply calibration
for reading in raw_readings:
    if reading != disregard_flag:
        adjusted_readings.append(reading + sensor_offset)

# Categorize readings by magnitude band using defaultdict
magnitude_bins = defaultdict(list)
for val in adjusted_readings:
    if val < 100:
        magnitude_bins['low'].append(val)
    elif val == 100:
        magnitude_bins['normal'].append(val)
    else:
        magnitude_bins['high'].append(val)

# Apply filtering logic: only keep 'normal' and 'high' categories
filtered_data = []
for key in ['normal', 'high']:
    filtered_data.extend(magnitude_bins[key])

# Further process: square values above 102
processing_func = lambda x: x**2 if x > 102 else x
processed_data = [processing_func(x) for x in filtered_data]

# Final computation step
filtered_sum = sum(processed_data)
print(f"Result: {filtered_sum}")