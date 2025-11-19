import statistics

temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9, 24.7, 22.5]
base_variance = statistics.variance(temperature_readings)

# Apply correction factor using bitwise operations
if base_variance > 0.5:
    correction_mask = 0b1010
    adjusted_variance = int(base_variance * 10) & correction_mask
else:
    adjusted_variance = int(base_variance * 100) | 0b0101

# Calculate final stability index
stability_index = adjusted_variance ^ 0b1111
print(f'Result: {stability_index}')