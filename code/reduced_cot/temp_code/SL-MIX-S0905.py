from collections import defaultdict
import itertools

def calculate_energy(interaction):
    base_values = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
    energy = 0
    for char in interaction:
        energy += base_values.get(char, 0)
    return energy

def is_valid_interaction(perm):
    energy = calculate_energy(perm)
    return 10 <= energy <= 20

def count_valid_combinations(particles):
    valid_count = 0
    for r in range(2, len(particles) + 1):
        for combination in itertools.combinations(particles, r):
            for perm in itertools.permutations(combination):
                perm_str = ''.join(perm)
                if is_valid_interaction(perm_str):
                    valid_count += 1
    return valid_count

particle_types = ['A', 'B', 'C', 'D']
total_valid_interactions = 0

for i in range(1, len(particle_types)):
    subset = particle_types[:i+1]
    local_count = count_valid_combinations(subset)
    total_valid_interactions += local_count // (i + 1)

print(f"Result: {total_valid_interactions}")