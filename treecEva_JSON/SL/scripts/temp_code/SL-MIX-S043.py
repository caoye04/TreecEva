from functools import reduce
from itertools import combinations

def calculate_bond_energy(atoms):
    return reduce(lambda x, y: x * y, atoms, 1)

def get_molecular_stability(molecule_configs):
    dp_table = {}
    
    def stabilize(subset):
        if subset in dp_table:
            return dp_table[subset]
        if len(subset) <= 1:
            dp_table[subset] = sum(subset)
            return dp_table[subset]
        
        # Combinatorial analysis of pair interactions
        pairwise_interactions = [
            calculate_bond_energy(pair) 
            for pair in combinations(subset, 2)
        ]
        
        # Dynamic programming with functional reduction
        interaction_sum = sum(pairwise_interactions)
        base_energy = reduce(lambda acc, val: acc + val**2, subset, 0)
        
        dp_table[subset] = interaction_sum + base_energy
        return dp_table[subset]
    
    total_stability = 0
    for config in molecule_configs:
        sorted_config = tuple(sorted(config))
        total_stability += stabilize(sorted_config)
    
    return total_stability

# Molecular configuration data representing atomic bonds
organic_compounds = [
    (3, 5, 7),
    (2, 4, 6, 8),
    (1, 9),
    (5, 5, 5)
]

stability_index = get_molecular_stability(organic_compounds)
print(f"Result: {stability_index}")