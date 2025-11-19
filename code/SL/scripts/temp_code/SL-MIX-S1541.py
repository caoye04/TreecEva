import math
from collections import deque
from dataclasses import dataclass
from statistics import variance

def calculate_slope(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    if dx == 0:
        return float('inf')
    return abs(dy / dx)

def is_stable_region(elevations):
    if len(elevations) < 3:
        return False
    try:
        var = variance(elevations)
        return var < 15.0
    except:
        return False

class TerrainNode:
    def __init__(self, region_id, elevations, left=None, right=None):
        self.region_id = region_id
        self.elevations = elevations
        self.left = left
        self.right = right

def build_terrain_tree():
    # Leaf nodes
    node_a = TerrainNode('A', [100, 102, 98, 101])
    node_b = TerrainNode('B', [110, 115, 108, 112])
    node_c = TerrainNode('C', [95, 97, 93, 96])
    node_d = TerrainNode('D', [120, 125, 118, 122])
    
    # Internal nodes
    node_ab = TerrainNode('AB', node_a.elevations + node_b.elevations, node_a, node_b)
    node_cd = TerrainNode('CD', node_c.elevations + node_d.elevations, node_c, node_d)
    
    # Root
    root = TerrainNode('ROOT', node_ab.elevations + node_cd.elevations, node_ab, node_cd)
    return root

tree_root = build_terrain_tree()
queue = deque([tree_root])
valid_landing_zones = 0
region_centers = {
    'A': (0, 0),
    'B': (10, 5),
    'C': (0, 10),
    'D': (10, 15)
}

while queue:
    current_node = queue.popleft()
    
    # Early return for leaf nodes without sufficient data
    if not current_node.left and not current_node.right:
        if len(current_node.elevations) < 4:
            continue
    
    # Check statistical stability
    if not is_stable_region(current_node.elevations):
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
        continue
    
    # For leaf nodes, apply geometric checks
    if not current_node.left and not current_node.right:
        center = region_centers.get(current_node.region_id, (0, 0))
        
        # Lambda to check proximity to obstacles
        is_safe_from_obstacles = lambda x, y: all(math.sqrt((x-ox)**2 + (y-oy)**2) > 3.0 for ox, oy in [(2, 2), (8, 8)])
        
        # Switch-case simulation for slope classification
        avg_elevation = sum(current_node.elevations) / len(current_node.elevations)
        slope_category = ''
        if avg_elevation < 100:
            slope_category = 'low'
        elif avg_elevation < 115:
            slope_category = 'medium'
        else:
            slope_category = 'high'
        
        # Count valid zones based on category and safety
        if slope_category != 'high' and is_safe_from_obstacles(center[0], center[1]):
            valid_landing_zones += 1
    
    # Add children to queue
    if current_node.left:
        queue.append(current_node.left)
    if current_node.right:
        queue.append(current_node.right)

print(f"Result: {valid_landing_zones}")