temperature = 80
humidity = 55
base_level = 12.5
correction_factor = 1.6
adjustment_factor = 20

# Determine energy threshold based on environmental conditions
energy_threshold = adjustment_factor if (temperature > 75 and humidity < 60) else base_level * correction_factor

Result: energy_threshold