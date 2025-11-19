from itertools import combinations

electron_counts = [2, 7, 8, 9, 10]
total_bonding_score = 0

# Process all unique pairs of atoms
for atom_a, atom_b in combinations(electron_counts, 2):
    # Check if one has even and the other has odd valence electrons
    if (atom_a % 2 == 0) != (atom_b % 2 == 0):  # XOR condition for even/odd pairing
        total_bonding_score += atom_a * atom_b

print(f"Result: {total_bonding_score}")