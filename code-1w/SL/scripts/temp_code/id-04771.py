import math
from itertools import combinations

# System configuration parameters
def calculate_entropy(values):
    return -sum(p * math.log2(p) for p in values if p > 0)

# Simulate subsystem probabilities
distribution_a = [0.25, 0.25, 0.5]
distribution_b = [0.1, 0.3, 0.6]

temp_buffer = [1, 2, 3]  # Irrelevant data structure (minimal distraction)

# Compute individual entropies
entropy_a = calculate_entropy(distribution_a)
entropy_b = calculate_entropy(distribution_b)

# Generate interaction terms between subsystem states
interactions = list(combinations([0.25, 0.25, 0.5], 2))
interaction_entropies = [calculate_entropy(pair) for pair in interactions]

# Aggregate all entropy components
entropies = [entropy_a, entropy_b] + interaction_entropies

# Key statement
total_entropy = sum(entropies)

Result: {total_entropy}