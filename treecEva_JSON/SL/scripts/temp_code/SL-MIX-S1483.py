from collections import defaultdict
import statistics

class TreeNode:
    def __init__(self, name, growth_data=None):
        self.name = name
        self.growth_data = growth_data  # List of growth measurements for species
        self.children = []  # Child nodes (genus or species)

# Construct the botanical data tree
root = TreeNode('Greenhouse')

# Genus Citrus
citrus_genus = TreeNode('Citrus')
root.children.append(citrus_genus)
species_limon = TreeNode('Limon', [2.1, -0.5, 3.2, 1.8])
species_aurantium = TreeNode('Aura', [1.2, 1.0, 0.8, 2.0])
species_paradisi = TreeNode('Para', [-1.0, -0.2, 0.1, 0.3])
citrus_genus.children.extend([species_limon, species_aurantium, species_paradisi])

# Genus Rosa
rosa_genus = TreeNode('Rosa')
root.children.append(rosa_genus)
species_damask = TreeNode('Damask', [0.5, 0.7, 0.9, 0.6])
species_gallica = TreeNode('Gallica', [1.0, 1.5, -0.2, 1.3])
species_alba = TreeNode('Alba', [0.8, 0.6, 0.7, 0.9])
rosa_genus.children.extend([species_damask, species_gallica, species_alba])

# Genus Lavandula
lavandula_genus = TreeNode('Lavandula')
root.children.append(lavandula_genus)
species_angustifolia = TreeNode('Angusti', [1.5, 1.2, 1.8, 2.0])
species_viridis = TreeNode('Viridis', [-0.5, -0.3, -0.1, 0.2])
lavandula_genus.children.extend([species_angustifolia, species_viridis])

# Process tree to compute genus health scores
genius_health_scores = {}

for genus_node in root.children:
    valid_species_growth_rates = []
    total_species_count = 0
    
    for species_node in genus_node.children:
        total_species_count += 1
        growth_measurements = species_node.growth_data
        if growth_measurements:
            avg_growth = sum(growth_measurements) / len(growth_measurements)
            if avg_growth > 0:
                valid_species_growth_rates.append(avg_growth)
    
    # Check if at least 60% of species have positive average growth
    if total_species_count > 0 and (len(valid_species_growth_rates) / total_species_count) >= 0.6:
        genius_health_scores[genus_node.name] = statistics.mean(valid_species_growth_rates)

# Compute final health score as the mean of valid genus health scores
final_health_score = statistics.mean(genius_health_scores.values()) if genius_health_scores else 0.0
print(f"Result: {final_health_score}")