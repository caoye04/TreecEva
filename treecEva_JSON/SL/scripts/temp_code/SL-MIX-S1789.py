from itertools import permutations
from math import factorial

# Simulated particle interaction data
interaction_log = [
    ('P1', 'P2'), ('P2', 'P1'), ('P3', 'P4'), 
    ('P4', 'P3'), ('P1', 'P3'), ('P5', 'P6'),
    ('P6', 'P5'), ('P7', 'P8'), ('P8', 'P7'),
    ('P2', 'P3'), ('P9', 'P10')
]

# Convert log to sets for efficient lookup
forward_interactions = set(interaction_log)
reverse_interactions = {tuple(reversed(pair)) for pair in interaction_log}

# Find bidirectional interactions (both (a,b) and (b,a) exist)
stable_pairs = forward_interactions & reverse_interactions
bidirectional_count = len(stable_pairs) // 2  # Each pair counted twice

# Find particles involved in any interaction
all_particles = {p for pair in interaction_log for p in pair}

# Count particles that only participate in unidirectional interactions
unidirectional_particles = set()
for pair in interaction_log:
    if pair not in stable_pairs and tuple(reversed(pair)) not in stable_pairs:
        unidirectional_particles.update(pair)

# Calculate factorial of unidirectional particle count
unidirectional_factorial = factorial(len(unidirectional_particles))

# Compute final stability index
stability_index = bidirectional_count * unidirectional_factorial

print(f'Result: {stability_index}')