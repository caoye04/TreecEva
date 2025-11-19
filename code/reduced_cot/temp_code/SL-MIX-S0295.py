import math
from collections import defaultdict
from contextlib import contextmanager

class QuadNode:
    def __init__(self, x, y, width, depth=0):
        self.x = x
        self.y = y
        self.width = width
        self.depth = depth
        self.is_leaf = width <= 1
        self.children = []
        self.pollution_index = 0
        self.zone_type = 'industrial'  # industrial or residential
    
    def subdivide(self):
        if not self.is_leaf:
            half = self.width // 2
            self.children = [
                QuadNode(self.x, self.y, half, self.depth+1),
                QuadNode(self.x + half, self.y, half, self.depth+1),
                QuadNode(self.x, self.y + half, half, self.depth+1),
                QuadNode(self.x + half, self.y + half, half, self.depth+1)
            ]
    
    def set_leaf_data(self, zone_type, pollution_index):
        if self.is_leaf:
            self.zone_type = zone_type
            self.pollution_index = pollution_index

# Global tracking of residential area
residential_area_counter = 0

@contextmanager
def track_residential_area():
    global residential_area_counter
    initial_count = residential_area_counter
    try:
        yield
    finally:
        pass
    # Post-execution tracking could go here

# Initialize quadtree root for a 4x4 km city
root = QuadNode(0, 0, 4)
root.subdivide()

# Populate leaf nodes with data
# Zone format: (x, y, zone_type, pollution_index)
zoning_data = [
    (0, 0, 'residential', 12),
    (1, 0, 'industrial', 45),
    (0, 1, 'residential', 18),
    (1, 1, 'residential', 9),
    (2, 0, 'residential', 15),
    (3, 0, 'industrial', 50),
    (2, 1, 'residential', 11),
    (3, 1, 'residential', 13),
    (0, 2, 'industrial', 38),
    (1, 2, 'residential', 16),
    (0, 3, 'residential', 14),
    (1, 3, 'industrial', 42),
    (2, 2, 'residential', 10),
    (3, 2, 'residential', 17),
    (2, 3, 'industrial', 35),
    (3, 3, 'residential', 19)
]

# Assign data to leaves
leaves = []
def assign_data(node):
    if node.is_leaf:
        for data in zoning_data:
            if node.x == data[0] and node.y == data[1]:
                node.set_leaf_data(data[2], data[3])
                if data[2] == 'residential':
                    leaves.append(node)
                break
    else:
        for child in node.children:
            assign_data(child)

assign_data(root)

# Calculate residential pollution statistics
with track_residential_area():
    residential_pollution_values = [leaf.pollution_index for leaf in leaves]
    residential_area_counter = len(residential_pollution_values)
    if residential_area_counter > 0:
        mean_pollution = sum(residential_pollution_values) / residential_area_counter
        variance = sum((x - mean_pollution) ** 2 for x in residential_pollution_values) / residential_area_counter
        residential_pollution_std = math.sqrt(variance)
    else:
        residential_pollution_std = 0

print(f"Result: {residential_pollution_std}")