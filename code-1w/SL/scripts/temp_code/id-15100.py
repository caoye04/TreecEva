from itertools import compress

# Sensor readings in microvolts from neural array
cellular_readings = [3.2, 4.1, 5.0, 4.8, 6.3, 7.1, 6.9, 8.2, 9.0, 8.7]

# Activation pattern based on baseline threshold
activation_mask = [(x > 5.0) for x in cellular_readings]

# Filter active signals using boolean mask
filtered_readings = list(compress(cellular_readings, activation_mask))

# Apply decay correction to last three active readings
if len(filtered_readings) >= 3:
    corrected_values = [v * 0.9 for v in filtered_readings[-3:]]
    filtered_readings[-3:] = corrected_values

# Final energy threshold determined from adjusted signal set
energy_threshold = filtered_readings[-1]

print(f"Result: {energy_threshold}")