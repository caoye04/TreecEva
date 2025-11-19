import math
from collections import defaultdict

temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.2, 24.9, 23.7, 22.5, 21.9, 23.3]

# Step 1: Calculate overall mean
mean_temp = sum(temperature_readings) / len(temperature_readings)

# Step 2: Calculate standard deviation
variance = sum((t - mean_temp) ** 2 for t in temperature_readings) / len(temperature_readings)
std_dev = math.sqrt(variance)

# Step 3: Normalize temperatures
normalized_temps = [(t - mean_temp) / std_dev for t in temperature_readings]

# Step 4: Compute absolute differences between consecutive normalized temps
abs_diffs = [abs(normalized_temps[i] - normalized_temps[i+1]) for i in range(len(normalized_temps)-1)]

# Step 5: Compute stability index (mean of absolute differences)
stability_index = sum(abs_diffs) / len(abs_diffs)

print(f"Result: {stability_index}")