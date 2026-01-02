from itertools import compress

# Sensor readings from a thermal array
temperature_data = [23.4, 19.8, 27.3, 21.0, 30.2, 25.1, 18.9, 22.7]

# Identify valid sensors (above baseline noise level)
valid_sensors = [temp > 20.0 for temp in temperature_data]

# Filtered energy levels from active sensors
filtered_energy = list(compress(temperature_data, valid_sensors))

# Normalization function using lambda
normalize = lambda values: round(sum(values) / len(values), 3) if values else 0.0

# Compute final threshold
energy_threshold = normalize(filtered_energy)

print(f"Result: {energy_threshold}")