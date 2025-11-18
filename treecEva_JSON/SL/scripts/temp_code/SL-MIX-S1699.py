import math
from collections import defaultdict, deque
from itertools import combinations

class ObservationNode:
    def __init__(self, station_id, species_counts=None):
        self.station_id = station_id
        self.species_counts = species_counts if species_counts else []
        self.children = []
    
    def is_leaf(self):
        return len(self.children) == 0

def compute_species_diversity(node):
    if not node.species_counts:
        return 0
    mean_count = sum(node.species_counts) / len(node.species_counts)
    if len(node.species_counts) <= 1:
        return 0
    variance = sum((x - mean_count) ** 2 for x in node.species_counts) / (len(node.species_counts) - 1)
    return math.sqrt(variance) if variance > 0 else 0

def collect_leaf_diversities(root):
    diversities = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node.is_leaf() and node.species_counts:
            diversity = compute_species_diversity(node)
            # Short-circuit: only add if diversity is meaningful (> 0.1)
            diversity > 0.1 and diversities.append(diversity)
        else:
            queue.extend(node.children)
    return diversities

def calculate_normalized_variance(values):
    if not values or len(values) <= 1:
        return 0
    mean_val = sum(values) / len(values)
    squared_diffs = [(x - mean_val) ** 2 for x in values]
    variance = sum(squared_diffs) / len(values)
    max_possible_var = max(values) ** 2 if max(values) > 0 else 1
    return variance / max_possible_var if max_possible_var != 0 else 0

# Build observation tree
root = ObservationNode('HQ', [10, 15, 12])
node_a = ObservationNode('A', [8, 9, 11, 10])
node_b = ObservationNode('B', [12, 14, 13])
node_c = ObservationNode('C', [5, 6])
node_d = ObservationNode('D', [20, 22, 19, 21])
node_e = ObservationNode('E', [7])
node_f = ObservationNode('F', [16, 17, 18])

# Construct tree structure
root.children = [node_a, node_b]
node_a.children = [node_c, node_d]
node_b.children = [node_e, node_f]

# Process tree and calculate result
leaf_diversities = collect_leaf_diversities(root)
normalized_variance = calculate_normalized_variance(leaf_diversities)
print(f"Result: {round(normalized_variance, 6)}")