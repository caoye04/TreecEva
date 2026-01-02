from itertools import compress

# Simulate sensor readings for pressure calibration
temperature_readings = [23.5, 24.1, 22.9, 25.0, 23.8]
base_pressure = 101.3
altitude_factor = 0.987
correction_factor = round(altitude_factor ** (temperature_readings[0] / 10), 2)

# Forces from directional sensors (left, right, top, bottom, center)
forces_applied = (85, 42, 77, 38, 91)

# Filter even-indexed forces and apply scaling
equilibrium_pressure = sum(forces_applied[::2]) * correction_factor  # indices 0, 2, 4

# Irrelevant filtering (distractor)
valid_readings = list(compress(temperature_readings, [t > 23 for t in temperature_readings]))

# Output result
print(f"Result: {equilibrium_pressure}")