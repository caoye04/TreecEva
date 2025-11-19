import math
from collections import namedtuple
from statistics import mean, variance

def transform_coordinates(point):
    x, y, z = point
    radius = math.sqrt(x**2 + y**2 + z**2)
    theta = math.acos(z / radius) if radius != 0 else 0
    phi = math.atan2(y, x)
    return (radius, theta, phi)

def altitude_adjustment(spherical_coords):
    r, theta, phi = spherical_coords
    adjusted_altitude = r * math.sin(theta) * math.cos(phi)
    return adjusted_altitude

# Monitoring station data: (x, y, z) coordinates
stations = [
    (3.5, 4.2, 2.1),
    (-1.2, 5.8, 3.3),
    (0.0, -2.7, 4.1),
    (6.1, -3.3, 1.9),
    (-4.4, 0.0, 5.5)
]

# Transform coordinates and calculate adjusted altitudes
transformed_stations = [transform_coordinates(station) for station in stations]
adjusted_altitudes = [altitude_adjustment(coord) for coord in transformed_stations]

# Calculate mean and variance of adjusted altitudes
mean_altitude = mean(adjusted_altitudes)
variance_altitude = variance(adjusted_altitudes)

# Compute modular mean deviation
mod_base = 7.5
modular_deviations = [(abs(alt - mean_altitude) % mod_base) for alt in adjusted_altitudes]
mean_modular_deviation = mean(modular_deviations)

# Apply floating-point precision adjustment
precision_factor = 1000.0
final_metric = round(mean_modular_deviation * precision_factor) / precision_factor

print(f"Result: {final_metric}")