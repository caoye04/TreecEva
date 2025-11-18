from itertools import combinations
from dataclasses import dataclass

@dataclass(frozen=True)
class SpeciesRecord:
    taxon_id: int
    common_name: str

# Define species sets for different ecological zones
zone_alpha = frozenset({SpeciesRecord(1, 'Red Fox'), SpeciesRecord(2, 'Elk'), SpeciesRecord(3, 'Pine Marten')})
zone_beta = frozenset({SpeciesRecord(2, 'Elk'), SpeciesRecord(4, 'Gray Wolf'), SpeciesRecord(5, 'Brown Bear')})
zone_gamma = frozenset({SpeciesRecord(3, 'Pine Marten'), SpeciesRecord(5, 'Brown Bear'), SpeciesRecord(6, 'Mountain Goat')})

# Calculate intersections and differences
alpha_beta_intersect = zone_alpha & zone_beta
beta_gamma_difference = zone_beta - zone_gamma
combined_unique = alpha_beta_intersect | beta_gamma_difference

# Count all possible pairs of species from the combined unique set
pair_count = len(list(combinations(combined_unique, 2)))

# Create registry with pair count and species from gamma zone not in alpha
exclusive_to_gamma = zone_gamma - zone_alpha
registry_size = pair_count + len(exclusive_to_gamma)

# Final registry cardinality considers only those with taxon_id > 2
final_registry = {s for s in (combined_unique | exclusive_to_gamma) if s.taxon_id > 2}
ecosystem_registry_cardinality = len(final_registry) + registry_size

print(f'Result: {ecosystem_registry_cardinality}')