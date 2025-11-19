import heapq
from itertools import combinations

def calculate_interaction_energy(mol1, mol2):
    return (mol1 ^ mol2) & 0xFF

molecular_ids = {42, 18, 73, 29, 55}
interaction_threshold = 30
valid_bonds = []
total_bond_score = 0

for mol_a, mol_b in combinations(molecular_ids, 2):
    energy = calculate_interaction_energy(mol_a, mol_b)
    if energy > interaction_threshold:
        heapq.heappush(valid_bonds, -energy)

bond_counter = 0
max_bonds = 3
while valid_bonds and bond_counter < max_bonds:
    bond_energy = -heapq.heappop(valid_bonds)
    total_bond_score += bond_energy
    bond_counter += 1

priority_adjustment = lambda x: x + sum(filter(lambda y: y % 2 == 0, molecular_ids))
total_bond_score = priority_adjustment(total_bond_score)

print(f"Result: {total_bond_score}")