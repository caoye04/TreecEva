import math
from functools import reduce

def build_tree(values):
    if not values:
        return None
    nodes = [TreeNode(val) for val in values]
    while len(nodes) > 1:
        new_level = []
        for i in range(0, len(nodes), 2):
            if i + 1 < len(nodes):
                parent_val = nodes[i].val ^ nodes[i+1].val
                parent = TreeNode(parent_val)
                parent.left = nodes[i]
                parent.right = nodes[i+1]
                new_level.append(parent)
            else:
                new_level.append(nodes[i])
        nodes = new_level
    return nodes[0] if nodes else None

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Satellite image data represented as a 2D matrix
satellite_image = [
    [15, 23, 37, 42],
    [58, 64, 71, 89],
    [92, 106, 113, 127],
    [134, 145, 159, 168]
]

# Flatten the matrix and apply transformations
pixel_values = [item for sublist in satellite_image for item in sublist]
transformed_pixels = list(map(lambda x: (x << 2) & 255, pixel_values))
filtered_pixels = list(filter(lambda x: x % 7 != 0, transformed_pixels))
statistical_modifier = int(math.sqrt(reduce(lambda a, b: a + b, filtered_pixels)) % 16)
adjusted_pixels = [(p ^ statistical_modifier) for p in filtered_pixels]

# Build binary tree from adjusted pixel values
root_node = build_tree(adjusted_pixels)

print(f"Result: {root_node.val}")