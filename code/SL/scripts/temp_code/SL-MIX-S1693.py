from functools import reduce

class QuadTreeNode:
    def __init__(self, value=None):
        self.value = value
        self.children = []
    
    def is_leaf(self):
        return len(self.children) == 0

# Initialize 4x4 grid with biodiversity indices
grid_indices = [
    [3, 7, 2, 5],
    [1, 8, 4, 6],
    [9, 0, 3, 7],
    [2, 5, 1, 4]
]

# Create leaf nodes for the grid
leaf_nodes = [[QuadTreeNode(grid_indices[i][j]) for j in range(4)] for i in range(4)]

# Build second level (4 2x2 regions)
level2_regions = []
for i in range(0, 4, 2):
    row = []
    for j in range(0, 4, 2):
        node = QuadTreeNode()
        node.children = [
            leaf_nodes[i][j], leaf_nodes[i][j+1],
            leaf_nodes[i+1][j], leaf_nodes[i+1][j+1]
        ]
        row.append(node)
    level2_regions.append(row)

# Calculate values for second level nodes
for i in range(2):
    for j in range(2):
        children_values = [child.value for child in level2_regions[i][j].children]
        # Apply special rule: if any child is 0, contribute -1 instead
        if 0 in children_values:
            level2_regions[i][j].value = reduce(lambda x, y: x ^ y, [v if v != 0 else -1 for v in children_values])
        else:
            level2_regions[i][j].value = reduce(lambda x, y: x ^ y, children_values)

# Build root node with level2 regions as children
root_node = QuadTreeNode()
root_node.children = [level2_regions[0][0], level2_regions[0][1], level2_regions[1][0], level2_regions[1][1]]

# Calculate root value using same rules
children_values = []
for child in root_node.children:
    children_values.append(child.value)

# Apply special rule for root
if 0 in children_values:
    root_biodiversity = reduce(lambda x, y: x ^ y, [v if v != 0 else -1 for v in children_values])
else:
    root_biodiversity = reduce(lambda x, y: x ^ y, children_values)

print(f"Result: {root_biodiversity}")