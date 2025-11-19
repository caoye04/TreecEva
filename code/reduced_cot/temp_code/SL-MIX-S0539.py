from collections import defaultdict
import re

class PhyloNode:
    def __init__(self, marker, children=None):
        self.marker = marker
        self.children = children if children else []

def count_matching_lineages(root, pattern):
    def dfs(node):
        if not node:
            return []
        paths = [[node.marker]]
        for child in node.children:
            child_paths = dfs(child)
            for path in child_paths:
                paths.append([node.marker] + path)
        return paths
    
    all_paths = dfs(root)
    lineage_count = 0
    for path in all_paths:
        path_str = ''.join(path)
        if re.search(pattern, path_str):
            lineage_count += 1
    return lineage_count

# Constructing phylogenetic tree
root = PhyloNode('A', [
    PhyloNode('B', [
        PhyloNode('C'),
        PhyloNode('D', [
            PhyloNode('E')
        ])
    ]),
    PhyloNode('F', [
        PhyloNode('G'),
        PhyloNode('H')
    ]),
    PhyloNode('I', [
        PhyloNode('J', [
            PhyloNode('K')
        ])
    ])
])

pattern = r'B.*E|F.*[GH]'
lineage_count = count_matching_lineages(root, pattern)
print(f'Result: {lineage_count}')