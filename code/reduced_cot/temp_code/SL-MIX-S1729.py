import heapq
from itertools import combinations

def calculate_bond_strength(energy_tuple):
    e1, e2, e3 = energy_tuple
    return (e1 * e2) + (e2 * e3) + (e1 * e3)

def validate_bond_configuration(strength):
    return strength > 150 and strength % 7 == 0

def get_top_bonding_configurations(atom_energies):
    triangular_configs = combinations(atom_energies, 3)
    valid_configs_heap = []
    
    for config in triangular_configs:
        bond_strength = calculate_bond_strength(config)
        if validate_bond_configuration(bond_strength):
            heapq.heappush(valid_configs_heap, -bond_strength)  # Max heap using negative values
    
    top_count = 0
    while valid_configs_heap and -valid_configs_heap[0] > 200:
        heapq.heappop(valid_configs_heap)
        top_count += 1
    
    return top_count

atom_interaction_energies = [12, 15, 18, 9, 21, 24, 6, 30]
total_valid_configurations = get_top_bonding_configurations(atom_interaction_energies)
print(f"Result: {total_valid_configurations}")