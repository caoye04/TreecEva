import math
from itertools import combinations

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Species data: id -> abundance
species_abundance = {i: fibonacci(i+3) for i in range(7)}
abundance_threshold = 10

# Filter species with abundance above threshold
viable_species = {k: v for k, v in species_abundance.items() if v > abundance_threshold}

# Calculate pairwise interaction potential
interaction_pairs = list(combinations(viable_species.keys(), 2))

# Biodiversity index calculation
ecological_index = 0
for s1, s2 in interaction_pairs:
    # Only consider pairs where at least one species has prime abundance
    abundance1, abundance2 = viable_species[s1], viable_species[s2]
    if is_prime(abundance1) or is_prime(abundance2):
        # Ternary operator to determine weighting factor
        weight_factor = 2 if abundance1 > abundance2 else (1 if abundance1 < abundance2 else 0)
        # Short-circuit evaluation for efficiency
        ecological_index += (abundance1 * abundance2) if weight_factor else 0

# Final adjustment using set operations
prime_abundances = {v for v in viable_species.values() if is_prime(v)}
composite_abundances = {v for v in viable_species.values() if not is_prime(v) and v > 1}

# Adjust index based on set cardinality relationship
if len(prime_abundances) and len(composite_abundances):
    ecological_index *= len(prime_abundances) // len(composite_abundances) if len(composite_abundances) != 0 else 1
else:
    ecological_index = 0

print(f"Result: {ecological_index}")