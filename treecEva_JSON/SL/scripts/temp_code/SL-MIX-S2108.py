from itertools import combinations
from math import sqrt

class AtomNode:
    def __init__(self, weight, next_node=None):
        self.weight = weight
        self.next = next_node

def build_molecular_chain(weights):
    if not weights:
        return None
    head = AtomNode(weights[0])
    current = head
    for w in weights[1:]:
        current.next = AtomNode(w)
        current = current.next
    return head

def extract_weights(chain_head):
    weights = []
    current = chain_head
    while current:
        weights.append(current.weight)
        current = current.next
    return weights

def compute_pairwise_potentials(weight_list):
    potentials = []
    for a, b in combinations(weight_list, 2):
        # Interaction potential formula: sqrt(a*b) / (a+b)
        if a + b != 0:
            potential = sqrt(a * b) / (a + b)
            potentials.append(potential)
    return potentials

def aggregate_interactions(potential_values):
    total = 0.0
    for p in potential_values:
        total += p
    return total

# Molecular structure definition
atom_weights = [16.0, 1.0, 14.0, 12.0, 1.0]  # Oxygen, Hydrogen, Nitrogen, Carbon, Hydrogen

# Build the molecular chain
molecular_structure = build_molecular_chain(atom_weights)

# Extract weights from the chain
extracted_weights = extract_weights(molecular_structure)

# Compute pairwise interaction potentials
interaction_potentials = compute_pairwise_potentials(extracted_weights)

# Aggregate all interaction potentials
final_interaction_energy = aggregate_interactions(interaction_potentials)

print(f"Result: {final_interaction_energy}")