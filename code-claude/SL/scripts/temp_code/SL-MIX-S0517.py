# Analyzing sensor correlation data from temperature readings
# We need to find unique sensor reading pairs (order doesn't matter)

sensor_a = [21, 23, 22, 21, 24, 22]
sensor_b = [19, 20, 19, 19, 21, 20]

# Track total readings for reporting purposes
total_readings = len(sensor_a)

# Calculate average readings
avg_a = sum(sensor_a) / total_readings
avg_b = sum(sensor_b) / total_readings

# Find unique pairs of readings (a,b) where order doesn't matter
# For example (21,19) and (19,21) should count as the same pair
unique_pairs = len(set(map(lambda p: (min(p), max(p)), zip(sensor_a, sensor_b))))

# Count readings above average for both sensors
above_avg = sum(1 for a, b in zip(sensor_a, sensor_b) if a > avg_a and b > avg_b)

# Calculate a correlation factor (not used in this analysis)
correlation = round(sum((a % 10) * (b % 10) for a, b in zip(sensor_a, sensor_b)) / total_readings, 2)

print(f"Result: {unique_pairs}")