import re
from collections import deque

class PlantNode:
    def __init__(self, genome_hash, left=None, right=None, parent=None):
        self.genome_hash = genome_hash
        self.left = left
        self.right = right
        self.parent = parent

def calculate_genetic_distance(ancestor, descendant):
    distance = 0
    current = descendant
    while current != ancestor and current is not None:
        distance += 1
        current = current.parent
    return distance if current == ancestor else -1

def hash_genome_sequence(sequence):
    return hash(sequence) % 1000000

def classify_species_variants(node_list):
    pattern = re.compile(r'^(ATG)([CGAT]{3})*(TAA|TAG|TGA)$')
    valid_genomes = [node for node in node_list if pattern.match(str(node.genome_hash))]
    return len(valid_genomes)

# Create plant lineage tree
root = PlantNode(hash_genome_sequence('ATGCCCTAA'))
node2 = PlantNode(hash_genome_sequence('ATGCCGTAAG'), parent=root)
node3 = PlantNode(hash_genome_sequence('ATGCCGTAAT'), parent=root)
node4 = PlantNode(hash_genome_sequence('ATGCCGTAAA'), parent=node2)
node5 = PlantNode(hash_genome_sequence('ATGCCGTACA'), parent=node2)
node6 = PlantNode(hash_genome_sequence('ATGCCGTAGA'), parent=node3)

root.left = node2
root.right = node3
node2.left = node4
node2.right = node5
node3.left = node6

# Process lineage data
all_nodes = [root, node2, node3, node4, node5, node6]
genetic_marker_sets = [
    {node.genome_hash % 100 for node in all_nodes if node.genome_hash % 3 == 0},
    {node.genome_hash % 100 for node in all_nodes if node.genome_hash % 5 == 0},
    {node.genome_hash % 100 for node in all_nodes if node.genome_hash % 7 == 0}
]

# Find common genetic markers
common_markers = set.intersection(*genetic_marker_sets)

# Calculate lineage distances using BFS
queue = deque([(root, 0)])
total_distance = 0
visited = set()

while queue:
    node, depth = queue.popleft()
    if node.genome_hash not in visited:
        visited.add(node.genome_hash)
        total_distance += depth
        if node.left:
            node.left.parent = node
            queue.append((node.left, depth + 1))
        if node.right:
            node.right.parent = node
            queue.append((node.right, depth + 1))

# Apply species classification
valid_species_count = classify_species_variants(all_nodes)

# Compute final classification score
final_classification_score = (
    len(common_markers) * 100 +
    total_distance * 10 +
    valid_species_count
) ^ (root.genome_hash % 100)

print(f'Result: {final_classification_score}')