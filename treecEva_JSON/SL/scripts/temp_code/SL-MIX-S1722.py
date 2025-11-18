from collections import deque

class QuadTreeNode:
    def __init__(self, x, y, width, height, depth=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.depth = depth
        self.children = []
        self.hash_value = (x << 8) ^ (y << 4) ^ depth
    
    def subdivide(self):
        if self.width <= 1 or self.depth >= 3:
            return
        half_width = self.width // 2
        half_height = self.height // 2
        
        # Create four quadrants: NW, NE, SW, SE
        nw = QuadTreeNode(self.x, self.y, half_width, half_height, self.depth + 1)
        ne = QuadTreeNode(self.x + half_width, self.y, half_width, half_height, self.depth + 1)
        sw = QuadTreeNode(self.x, self.y + half_height, half_width, half_height, self.depth + 1)
        se = QuadTreeNode(self.x + half_width, self.y + half_height, half_width, half_height, self.depth + 1)
        
        self.children = [nw, ne, sw, se]
        
        # Recursively subdivide some children based on geometric condition
        if (self.x * self.y) % 3 == 0:
            nw.subdivide()
        if (self.x + self.y) % 5 < 3:
            ne.subdivide()
        if self.width * self.height > 4:
            sw.subdivide()
        if (self.x ^ self.y) & 1:
            se.subdivide()

def dfs_even_children_xor(node):
    if not node:
        return 0
    
    cumulative_xor = 0
    stack = [node]
    
    while stack:
        current = stack.pop()
        
        # Only process nodes with even number of children
        if len(current.children) % 2 == 0:
            cumulative_xor ^= current.hash_value
        
        # Add children to stack (reversed for DFS order preservation)
        for child in reversed(current.children):
            stack.append(child)
    
    return cumulative_xor

def calculate_park_layout_hash():
    root = QuadTreeNode(0, 0, 8, 8)
    root.subdivide()
    
    # Apply a statistical adjustment to one quadrant
    if root.children:
        ne_quadrant = root.children[1]  # NE child
        if ne_quadrant.children:
            # Modify hash based on mean coordinate of grandchildren
            grandchild_coords = [(gc.x, gc.y) for gc in ne_quadrant.children]
            if grandchild_coords:
                mean_x = sum(x for x, y in grandchild_coords) // len(grandchild_coords)
                mean_y = sum(y for x, y in grandchild_coords) // len(grandchild_coords)
                ne_quadrant.hash_value = (mean_x << 6) ^ (mean_y << 2) ^ 0xFF
    
    return dfs_even_children_xor(root)

park_hash_result = calculate_park_layout_hash()
print(f"Result: {park_hash_result}")