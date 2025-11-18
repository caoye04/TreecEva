from collections import defaultdict
import itertools

class MoleculeNode:
    def __init__(self, bond_energy):
        self.bond_energy = bond_energy
        self.next = None

def create_molecular_ring(energies):
    if not energies:
        return None
    head = MoleculeNode(energies[0])
    current = head
    for energy in energies[1:]:
        current.next = MoleculeNode(energy)
        current = current.next
    current.next = head  # Complete the ring
    return head

def extract_energies_from_ring(head, length):
    if not head:
        return []
    energies = []
    current = head
    for _ in range(length):
        energies.append(current.bond_energy)
        current = current.next
    return energies

# Molecular structure with 6 atoms
ring_energies = [2, 3, 5, 7, 11, 13]
molecular_ring = create_molecular_ring(ring_energies)
extracted_energies = extract_energies_from_ring(molecular_ring, 6)

# Calculate stability index
stability_index = 0
for cycle in itertools.combinations(extracted_energies, 3):
    product = 1
    for energy in cycle:
        product *= energy
    stability_index += product

print(f"Result: {stability_index}")