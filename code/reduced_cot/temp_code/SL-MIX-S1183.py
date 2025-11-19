import math
from itertools import combinations

# Regional biodiversity datasets represented as frozen sets
forest_species = frozenset({'Oak', 'Pine', 'Deer', 'Wolf', 'Eagle'})
park_species = frozenset({'Oak', 'Maple', 'Squirrel', 'Deer', 'Robin'})
wetland_species = frozenset({'Willow', 'Duck', 'Frog', 'Fish', 'Reed'})
meadow_species = frozenset({'Grass', 'Rabbit', 'Deer', 'Butterfly', 'Robin'})

# Calculate pairwise intersections
region_pairs = [forest_species, park_species, wetland_species, meadow_species]
pairwise_intersections = [len(a & b) for a, b in combinations(region_pairs, 2)]

# Compute weighted overlap metric using lambda transformation
weight_function = lambda x: math.log(x + 1) if x > 0 else 0
weighted_overlaps = list(map(weight_function, pairwise_intersections))

# Biodiversity mapping table
bio_map = {0: 1.0, 1: 1.5, 2: 2.1, 3: 2.8}
scaled_scores = [bio_map.get(int(round(w)), 1.0) for w in weighted_overlaps]

# Calculate final ecological index through floating-point aggregation
ecological_index = round(sum(scaled_scores) / len(scaled_scores), 3)

print(f'Result: {ecological_index}')