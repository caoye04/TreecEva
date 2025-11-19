import math
from statistics import mean, stdev

temperature_readings = [23.4, 25.1, 22.8, 31.2, 24.7, 26.3, 23.9, 25.5, 24.2, 27.8]

# Apply a noise reduction filter using list comprehension
filtered_temps = [t for t in temperature_readings if abs(t - mean(temperature_readings)) <= 2*stdev(temperature_readings)]

# Find max temperature
peak_temp = max(filtered_temps)

# Standardize using z-score
z_score = (peak_temp - mean(filtered_temps)) / stdev(filtered_temps)

# Custom weighting function using lambda
weight_func = lambda x: math.log(abs(x) + 1) * (1 if x >= 0 else -1)

# Calculate weighted normalized outlier score
normalized_outlier_score = weight_func(z_score) * 100

print(f"Result: {round(normalized_outlier_score, 2)}")