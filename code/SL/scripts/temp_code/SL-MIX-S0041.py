import math
from functools import reduce

def pressure_adjustment_factor(depth):
    return math.cos(depth / 100) + 1.5

def energy_between_stations(start_depth, end_depth):
    depth_change = abs(end_depth - start_depth)
    horizontal_distance = 50  # Assumed constant for this mission phase
    base_energy = math.sqrt(depth_change**2 + horizontal_distance**2)
    adjusted_energy = base_energy * pressure_adjustment_factor((start_depth + end_depth) / 2)
    return adjusted_energy

# AUV navigation sequence through monitoring stations (depth in meters)
stations_depth = [200, 185, 220, 190, 250, 210, 240]

# Calculate energy consumption between each pair of consecutive stations
segment_energies = list(map(
    lambda i: energy_between_stations(stations_depth[i], stations_depth[i+1]),
    range(len(stations_depth)-1)
))

# Apply additional environmental factor for deep-sea currents
environmental_factors = [1.1, 0.95, 1.05, 0.98, 1.02, 1.07]
adjusted_energies = [
    e * f for e, f in zip(segment_energies, environmental_factors)
]

# Total energy with system efficiency correction (92% efficiency)
total_energy_consumption = reduce(lambda x, y: x + y, adjusted_energies) / 0.92

print(f"Result: {round(total_energy_consumption, 2)}")