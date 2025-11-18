from collections import defaultdict
import itertools

def calculate_mycelium_growth(max_levels):
    # Initialize root node biomass
    level_biomass = defaultdict(int)
    level_biomass[0] = 10
    
    # Growth factor for each level
    growth_factors = [1.5, 2.0, 1.8, 2.2, 1.9]
    
    # Process each level of the mycelium tree
    for level in range(1, max_levels + 1):
        # Calculate base biomass from parent level
        parent_nodes = 2 ** (level - 1)
        base_biomass = level_biomass[level-1] * growth_factors[(level-1) % len(growth_factors)]
        
        # Apply combinatorial distribution among child nodes
        combinations = list(itertools.combinations(range(parent_nodes), min(2, parent_nodes)))
        distributed_biomass = sum(len(combinations) * (base_biomass / max(1, len(combinations))))
        
        # Apply arithmetic adjustments based on tree properties
        if level % 2 == 0:
            adjusted_biomass = distributed_biomass * 1.1 - (level * 2)
        else:
            adjusted_biomass = distributed_biomass + (level ** 2) * 1.3
        
        level_biomass[level] = int(adjusted_biomass)
        
        # Early termination condition for unstable growth
        if level_biomass[level] < 0:
            break
    
    # Calculate final biomass using reduction operation
    final_biomass = sum(level_biomass.values())
    return final_biomass

# Execute the growth simulation
result = calculate_mycelium_growth(4)
print(f"Result: {result}")