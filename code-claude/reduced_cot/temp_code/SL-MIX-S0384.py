# Wildlife Conservation Analysis
# This program analyzes species distribution across three nature parks

# Species observed in each park (represented by unique ID numbers)
park_a = {101, 105, 107, 110, 112, 115, 118, 120}
park_b = {103, 105, 107, 109, 112, 114, 118}
park_c = {102, 105, 108, 110, 114, 118, 120, 122}

# Conservation priority scores for each species
priority_scores = {
    101: 3, 102: 2, 103: 1, 105: 5, 107: 4, 108: 2,
    109: 1, 110: 3, 112: 2, 114: 4, 115: 3, 118: 5, 120: 2, 122: 1
}

# Calculate metrics for conservation planning
total_species = len(park_a.union(park_b).union(park_c))
rare_species = {species for species in park_a if species not in park_b and species not in park_c}

# Track species distribution and movement patterns
distribution = {}
for park_id, species_set in enumerate([park_a, park_b, park_c], 1):
    for species in species_set:
        if species not in distribution:
            distribution[species] = []
        distribution[species].append(f"Park {park_id}")

# Calculate biodiversity metrics
ubiquitous_species = {species for species in park_a if species in park_b and species in park_c}
park_a_exclusive = len(park_a - park_b - park_c)
park_b_exclusive = len(park_b - park_a - park_c)

# Analyze species overlap between parks
common_species = len(park_a.intersection(park_b))

# Calculate weighted conservation score based on species distribution
conservation_score = 0
for species, parks in distribution.items():
    if len(parks) == 1:  # Endemic to one park
        conservation_score += priority_scores.get(species, 0) * 3
    elif len(parks) == 2:  # Found in two parks
        conservation_score += priority_scores.get(species, 0) * 2
    else:  # Found in all three parks
        conservation_score += priority_scores.get(species, 0)

# Prepare final report
total_parks = 3
average_species = sum(len(park) for park in [park_a, park_b, park_c]) / total_parks

print(f"Result: {common_species}")