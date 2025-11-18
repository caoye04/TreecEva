import math
from collections import defaultdict

class SpectralNode:
    def __init__(self, frequency, energy):
        self.frequency = frequency
        self.energy = energy
        self.left = None
        self.right = None

def build_spectral_tree():
    # Root node at 1000 Hz with energy 50
    root = SpectralNode(1000, 50)
    # Left subtree
    root.left = SpectralNode(500, 30)
    root.left.left = SpectralNode(250, 15)
    root.left.right = SpectralNode(750, 20)
    # Right subtree
    root.right = SpectralNode(1500, 70)
    root.right.right = SpectralNode(2000, 40)
    return root

def compute_node_weights(node):
    if not node:
        return 0
    left_weight = compute_node_weights(node.left)
    right_weight = compute_node_weights(node.right)
    # Weight calculation combines energy with logarithmic frequency scaling
    node_weight = int(node.energy * math.log2(node.frequency / 100))
    # Apply XOR with children weights for interference modeling
    total_weight = node_weight ^ left_weight ^ right_weight
    return total_weight

def collect_energy_stats(root):
    energies = []
    def traverse(node):
        if not node:
            return
        energies.append(node.energy)
        traverse(node.left)
        traverse(node.right)
    traverse(root)
    mean_energy = sum(energies) / len(energies)
    variance = sum((e - mean_energy) ** 2 for e in energies) / len(energies)
    return mean_energy, variance

tree_root = build_spectral_tree()
node_weights = {}

def annotate_tree(node):
    if not node:
        return
    weight = compute_node_weights(node)
    node_weights[node.frequency] = weight
    annotate_tree(node.left)
    annotate_tree(node.right)

annotate_tree(tree_root)
mean_energy, variance_energy = collect_energy_stats(tree_root)

# Compute final aggregation metric
frequency_mask = 0b11110000
energy_mod_factor = int(math.exp(2))  # Approximately 7

aggregation_components = [
    node_weights[1000] & frequency_mask,
    int(mean_energy) << 2,
    int(variance_energy) >> 1,
    energy_mod_factor ** 2
]

aggregation_metric = 0
for i, component in enumerate(aggregation_components):
    aggregation_metric += component * (i + 1)

print(f"Result: {aggregation_metric}")