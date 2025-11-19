from collections import defaultdict

class PlantNode:
    def __init__(self, name, diversity_score):
        self.name = name
        self.diversity_score = diversity_score
        self.children = []
    
    def add_child(self, child_node):
        self.children.append(child_node)

def process_mutations(node):
    if not node:
        return 0
    
    # String transformation: reverse name and take length as multiplier
    name_modifier = len(node.name[::-1])
    
    # Apply modifier to current node's diversity score
    mutated_score = node.diversity_score * name_modifier
    
    # If node has children, apply recursive processing
    child_scores = sum(process_mutations(child) for child in node.children)
    
    # Return accumulated score from this subtree
    return mutated_score + child_scores

def encode_genetic_marker(species_name):
    # Simple hash-like encoding based on character positions
    return sum(ord(c) * (i + 1) for i, c in enumerate(species_name))

# Build the botanical tree
root = PlantNode("Oak", 15)
child1 = PlantNode("Maple", 12)
child2 = PlantNode("Pine", 8)
grandchild1 = PlantNode("Cedar", 10)
grandchild2 = PlantNode("Spruce", 9)

root.add_child(child1)
root.add_child(child2)
child1.add_child(grandchild1)
child1.add_child(grandchild2)

# Initialize accumulator for seasonal processing
seasonal_accumulator = 0

# Process root and its entire subtree
seasonal_accumulator += process_mutations(root)

# Additional processing: apply genetic marker encoding to all species names
all_species = ["Oak", "Maple", "Pine", "Cedar", "Spruce"]
genetic_contributions = {species: encode_genetic_marker(species) for species in all_species}

# Merge contributions into accumulator using dictionary comprehension
marker_boost = {species: genetic_contributions[species] * len(species) for species in genetic_contributions}
seasonal_accumulator += sum(marker_boost.values())

print(f"Result: {seasonal_accumulator}")