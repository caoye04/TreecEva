from itertools import compress

# Sensor readings in degrees Celsius
temperature_readings = [23.5, 19.0, 25.8, 17.2, 30.1, 28.7, 22.3, 16.8]

# Step 1: Filter valid sensor readings above minimum operational threshold
valid_mask = [temp >= 18.0 for temp in temperature_readings]
filtered_temperatures = list(compress(temperature_readings, valid_mask))

# Step 2: Calculate base reference as average of first three valid readings
base_temp = sum(filtered_temperatures[:3]) / len(filtered_temperatures[:3])

# Step 3: Count how many exceed the adaptive threshold
threshold_count = sum(1 for x in filtered_temperatures if x > base_temp)

# Irrelevant distraction: unused statistical measure
deviation_rms = (sum((x - base_temp) ** 2 for x in filtered_temperatures) / len(filtered_temperatures)) ** 0.5

print(f"Result: {threshold_count}")