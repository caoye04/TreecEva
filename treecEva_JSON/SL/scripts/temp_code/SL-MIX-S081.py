import math
from collections import defaultdict

def calculate_diversity_index(species_data):
    return int(math.log(sum(species_data)) * 100)

# Observation data from three monitoring zones
primary_zone_observations = {12, 15, 19, 23, 29}
secondary_zone_observations = {7, 11, 13, 17, 19}
tertiary_zone_observations = {5, 7, 11, 13, 17}

# Calculate zone-specific metrics
primary_metrics = frozenset({x**2 for x in primary_zone_observations})
secondary_metrics = frozenset({x*2 for x in secondary_zone_observations})
tertiary_metrics = frozenset({x+3 for x in tertiary_zone_observations})

# Determine shared species between zones
shared_species = primary_metrics.intersection(secondary_metrics, tertiary_metrics)

# Build species frequency map
frequency_map = defaultdict(int)
for zone_data in [primary_metrics, secondary_metrics, tertiary_metrics]:
    for value in zone_data:
        frequency_map[value] += 1

# Identify endemic species (appearing in only one zone)
endemic_species = {k for k, v in frequency_map.items() if v == 1}

# Apply diversity transformation
transformed_endemic = {calculate_diversity_index({x}) for x in endemic_species if x > 20}

# Compute final index using logarithmic scaling
if transformed_endemic:
    endemic_richness_index = int(math.exp(len(transformed_endemic) / len(endemic_species)) * 1000)
else:
    endemic_richness_index = 0

print(f"Result: {endemic_richness_index}")