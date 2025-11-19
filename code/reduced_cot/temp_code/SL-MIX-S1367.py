from collections import defaultdict
from functools import wraps
from itertools import combinations

def step_counter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

@step_counter
def calculate_bond_strength(atoms):
    if len(atoms) < 2:
        return 0
    return sum(atoms) * len(atoms)

# Molecular stability factors
atomic_weights = [2, 3, 5, 7, 11]
bond_energies = defaultdict(int)
total_bond_energy = 0

# Process all possible molecular combinations
for r in range(2, len(atomic_weights) + 1):
    for combo in combinations(atomic_weights, r):
        if calculate_bond_strength(combo) > 15:
            bond_energies[r] += calculate_bond_strength(combo)
        else:
            bond_energies[r] -= sorted(combo)[-1]

# Calculate final energy with conditional adjustments
for bond_type, energy in sorted(bond_energies.items(), key=lambda x: x[0]):
    if energy > 0:
        total_bond_energy += energy // bond_type
    else:
        total_bond_energy += energy * bond_type

print(f"Result: {total_bond_energy}")