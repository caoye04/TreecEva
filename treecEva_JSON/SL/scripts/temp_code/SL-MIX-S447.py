from dataclasses import dataclass
from typing import List, Set

@dataclass
class HabitatData:
    species_codes: Set[int]
    habitat_id: int

# Sensor data from three different habitats
sensor_readings = [
    HabitatData({101, 102, 105, 108}, 1),
    HabitatData({102, 103, 106, 109}, 2),
    HabitatData({104, 105, 107, 110}, 3)
]

# Find common species across all habitats
common_species = sensor_readings[0].species_codes.copy()
for reading in sensor_readings[1:]:
    common_species &= reading.species_codes

# Calculate diversity index using modular arithmetic
unique_species_count = 0
for reading in sensor_readings:
    unique_species_count += len(reading.species_codes - common_species)

# Normalize using a prime modulus
prime_mod = 17
diversity_index = (unique_species_count * 7 + 3) % prime_mod

# Apply binary search-like adjustment for normalization
adjustment_values = [2, 4, 6, 8, 10, 12, 14, 16]
target = diversity_index
left, right = 0, len(adjustment_values) - 1
normalized_index = 0

while left <= right:
    mid = (left + right) // 2
    if adjustment_values[mid] <= target:
        normalized_index = mid + 1
        left = mid + 1
    else:
        right = mid - 1

# Final adjustment using set operations
if normalized_index in {1, 3, 5}:
    normalized_index = (normalized_index * 3) % 7

print(f"Result: {normalized_index}")