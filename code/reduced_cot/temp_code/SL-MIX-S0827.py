import math
from collections import defaultdict, namedtuple
from itertools import combinations

class TreeNode:
    def __init__(self, species_id, abundance):
        self.species_id = species_id
        self.abundance = abundance
        self.children = []
    
    def add_child(self, child_node):
        self.children.append(child_node)

# Construct a sample forest (tree structure)
# Layer 1
forest_root = TreeNode(0, 150)
# Layer 2
node_mammals = TreeNode(1, 80)
node_birds = TreeNode(2, 120)
forest_root.add_child(node_mammals)
forest_root.add_child(node_birds)
# Layer 3
node_deer = TreeNode(3, 45)
node_squirrel = TreeNode(4, 35)
node_eagle = TreeNode(5, 70)
node_owl = TreeNode(6, 50)
node_mammals.add_child(node_deer)
node_mammals.add_child(node_squirrel)
node_birds.add_child(node_eagle)
node_birds.add_child(node_owl)

# Trait encoding for each species (bitmask)
species_traits = {
    0: 0b1100, # Generalist
    1: 0b1010, # Warm-blooded
    2: 0b1011, # Warm-blooded, Flying
    3: 0b0001, # Herbivore
    4: 0b0101, # Omnivore
    5: 0b0011, # Carnivore
    6: 0b0011, # Carnivore
}

# Function to calculate trait diversity using XOR
def calculate_trait_diversity(node_list):
    if not node_list:
        return 0
    trait_mask = species_traits[node_list[0].species_id]
    for node in node_list[1:]:
        trait_mask ^= species_traits[node.species_id]
    return bin(trait_mask).count('1')

# Function to traverse tree and collect abundances
def get_abundances(node):
    abundances = [node.abundance]
    for child in node.children:
        abundances.extend(get_abundances(child))
    return abundances

# Get all abundances from the forest
all_abundances = get_abundances(forest_root)

# Calculate mean abundance
mean_abundance = sum(all_abundances) / len(all_abundances)

# Calculate variance of abundances
variance_abundance = sum((x - mean_abundance) ** 2 for x in all_abundances) / len(all_abundances)

# Get leaf nodes (terminal species)
leaf_nodes = []
def find_leaves(node):
    if not node.children:
        leaf_nodes.append(node)
    else:
        for child in node.children:
            find_leaves(child)

find_leaves(forest_root)

# Calculate combinatorial co-occurrence score
co_occurrence_pairs = list(combinations(leaf_nodes, 2))
trait_similarity_sum = 0
for pair in co_occurrence_pairs:
    trait_a = species_traits[pair[0].species_id]
    trait_b = species_traits[pair[1].species_id]
    # Similarity is number of matching traits (bits set to 1 in AND result)
    similarity = bin(trait_a & trait_b).count('1')
    trait_similarity_sum += similarity

# Normalize co-occurrence score
normalized_co_occurrence = trait_similarity_sum / len(co_occurrence_pairs) if co_occurrence_pairs else 0

# Calculate trait diversity for all leaves
leaf_trait_diversity = calculate_trait_diversity(leaf_nodes)

# Biodiversity index combines normalized variance, co-occurrence, and trait diversity
# Using logarithmic scaling and bit shifting for weighting
log_variance = math.log(variance_abundance + 1)  # Add 1 to avoid log(0)
weighted_variance = int(log_variance) << 2  # Shift left by 2 (multiply by 4)

biodiversity_index = (
    weighted_variance + 
    int(normalized_co_occurrence * 10) + 
    (leaf_trait_diversity << 1)  # Shift left by 1 (multiply by 2)
)

print(f"Result: {biodiversity_index}")