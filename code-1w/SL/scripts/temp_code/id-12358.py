from collections import Counter

# Sensor data calibration and noise filtering
temperature_readings = [23.5, 19.0, 25.3, 18.7, 24.1, 26.0, 17.5, 24.8, 25.9, 19.2]
threshold_low = 19.0
threshold_high = 25.5

# Apply range filter to isolate valid sensor readings
valid_readings = [temp for temp in temperature_readings if threshold_low <= temp <= threshold_high]

# Remove duplicates while preserving order using dict
unique_readings = list(dict.fromkeys(valid_readings))

# Count occurrences of each reading (for diagnostic purposes)
reading_frequency = Counter(temperature_readings)

diagnostic_mode = False
log_entries = 0
if diagnostic_mode:
    for reading, count in reading_frequency.items():
        print(f'{reading}: {count}')
    log_entries = len(reading_frequency)

# Final processing: extract middle three values using slicing
sorted_readings = sorted(unique_readings)
filtered_data = sorted_readings[1:4]  # Middle three after sorting

filtered_sum = sum(filtered_data)
print(f"Result: {filtered_sum}")