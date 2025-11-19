from collections import defaultdict
import math

class TaxonNode:
    def __init__(self, name, priority=0):
        self.name = name
        self.priority = priority
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def calculate_branch_priority(node):
    if not node.children:
        return node.priority
    child_priorities = [calculate_branch_priority(child) for child in node.children]
    return node.priority + sum(child_priorities)

def custom_sort_key(node):
    return (-calculate_branch_priority(node), node.name)

def process_tracking_data(root_node, movement_counts):
    # Build a lookup table for nodes
    node_lookup = {}
    def build_lookup(current):
        node_lookup[current.name] = current
        for child in current.children:
            build_lookup(child)
    build_lookup(root_node)
    
    # Update priorities based on movement counts
    for species, count in movement_counts.items():
        if species in node_lookup:
            node_lookup[species].priority += count
    
    # Traverse and sort each level
    priority_score = 0
    traversal_queue = [root_node]
    
    while traversal_queue:
        current = traversal_queue.pop(0)
        if not current.children:
            continue
            
        # Sort children using custom algorithm
        current.children.sort(key=custom_sort_key)
        
        # Calculate weighted score for top 2 children only
        top_children = current.children[:2]
        for i, child in enumerate(top_children):
            weight = 1.0 / (i + 1)  # Higher weight for higher ranked children
            branch_priority = calculate_branch_priority(child)
            priority_score += int(weight * branch_priority * 10)  # Scale for integer result
            
            # Early termination if priority score exceeds threshold
            if priority_score > 1000:
                return priority_score
        
        # Add children to queue for further processing
        traversal_queue.extend(current.children)
    
    return priority_score

# Construct taxonomic tree
mammals = TaxonNode("Mammals")
birds = TaxonNode("Birds")
reptiles = TaxonNode("Reptiles")

# Mammal species
wolf = TaxonNode("Wolf")
bear = TaxonNode("Bear")
deer = TaxonNode("Deer")
mammals.add_child(wolf)
mammals.add_child(bear)
mammals.add_child(deer)

# Bird species
eagle = TaxonNode("Eagle")
sparrow = TaxonNode("Sparrow")
owl = TaxonNode("Owl")
birds.add_child(eagle)
birds.add_child(sparrow)
birds.add_child(owl)

# Reptile species
snake = TaxonNode("Snake")
turtle = TaxonNode("Turtle")
reptiles.add_child(snake)
reptiles.add_child(turtle)

# Root node
animals = TaxonNode("Animals")
animals.add_child(mammals)
animals.add_child(birds)
animals.add_child(reptiles)

# Movement data (species: count)
movement_data = {
    "Wolf": 25,
    "Bear": 18,
    "Deer": 42,
    "Eagle": 33,
    "Sparrow": 12,
    "Owl": 28,
    "Snake": 15,
    "Turtle": 8
}

priority_score = process_tracking_data(animals, movement_data)
print(f"Result: {priority_score}")