from itertools import compress

# Sensor readings from environmental monitoring stations
temperature_readings = [23.5, 19.0, 27.3, 30.1, 18.9, 24.2, 26.8, 22.4]

# Step 1: Filter out readings below freezing using list comprehension (distractor)
frozen_mask = [temp < 0 for temp in temperature_readings]
valid_readings = [temp for temp in temperature_readings if temp >= 0]

# Step 2: Apply correction factor to account for calibration drift
calibrated_readings = [round(temp * 1.02, 1) for temp in valid_readings]

# Step 3: Identify anomalous spikes above critical threshold
spike_detection = list(map(lambda x: x > 29.0, calibrated_readings))
filtered_readings = list(compress(calibrated_readings, [not spike for spike in spike_detection]))

# Step 4: Compute dynamic reference as median of stable readings (simplified)
sorted_readings = sorted(filtered_readings)
mid = len(sorted_readings) // 2
reference = (sorted_readings[mid] + sorted_readings[~mid]) / 2

# Step 5: Count how many readings exceed the adaptive threshold
deviation_flags = [abs(x - reference) > 2.0 for x in filtered_readings]
thresh_product = sum([a * b for a, b in zip(deviation_flags, [1]*len(deviation_flags))])

# Key statement: Count readings above reference level
threshold_count = sum(map(lambda x: x > reference, filtered_readings))

print(f"Result: {threshold_count}")