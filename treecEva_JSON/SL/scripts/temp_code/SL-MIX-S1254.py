from collections import defaultdict
from itertools import permutations

class GeneticAnalyzer:
    def __init__(self):
        self.marker_cache = defaultdict(int)
    
    def compute_permutation_product(self, markers):
        if tuple(markers) in self.marker_cache:
            return self.marker_cache[tuple(markers)]
        product = 1
        for p in permutations(markers):
            term = 1
            for elem in p:
                term *= elem
            product += term
        self.marker_cache[tuple(markers)] = product
        return product

def build_orchid_tree(orchid_data):
    tree = {}
    for idx, markers in enumerate(orchid_data):
        tree[idx] = {'markers': markers, 'children': []}
        if idx > 0:
            parent_idx = (idx - 1) // 2
            tree[parent_idx]['children'].append(idx)
    return tree

analyzer = GeneticAnalyzer()
orchid_batch = [
    [1, 2, 3],
    [2, 3],
    [1, 4, 2],
    [3, 1]
]

orchid_tree = build_orchid_tree(orchid_batch)
orchid_diversity_score = 0

for node_id in orchid_tree:
    markers = orchid_tree[node_id]['markers']
    score_contribution = analyzer.compute_permutation_product(markers)
    child_count = len(orchid_tree[node_id]['children'])
    if child_count > 0:
        score_contribution //= child_count
    orchid_diversity_score += score_contribution

print(f"Result: {orchid_diversity_score}")