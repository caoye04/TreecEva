from itertools import compress

# Sensor readings from a thermal array
temperature_readings = [23.4, 19.5, 27.8, 22.1, 18.9, 30.2, 25.6, 24.3, 20.0, 28.7]

# Apply quality mask: only valid if above minimum sensitivity threshold
good_quality = [temp > 20 for temp in temperature_readings]

# Extract high-confidence measurements
filtered_readings = list(compress(temperature_readings, good_quality))

# Sort readings to find upper quartile behavior
filtered_readings.sort()

# Calculate dynamic energy threshold based on largest valid reading
energy_threshold = filtered_readings[-1] if filtered_readings else 0

# Normalize remaining values relative to threshold (for downstream use)
normalized = [round(x / energy_threshold, 3) for x in filtered_readings]

# Output the target result
print(f"Target result: {energy_threshold}")