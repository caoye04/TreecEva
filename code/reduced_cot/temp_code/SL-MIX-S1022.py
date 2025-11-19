from functools import reduce

class QuadNode:
    def __init__(self, x_min, y_min, x_max, y_max, density=0):
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max
        self.density = density
        self.children = []
    
    def is_leaf(self):
        return len(self.children) == 0
    
    def area(self):
        return (self.x_max - self.x_min) * (self.y_max - self.y_min)
    
    def center_x(self):
        return (self.x_min + self.x_max) / 2
    
    def center_y(self):
        return (self.y_min + self.y_max) / 2

# Build quadtree structure
root = QuadNode(0, 0, 100, 100)
root.children = [
    QuadNode(0, 0, 50, 50, 3),    # SW
    QuadNode(50, 0, 100, 50, 7),  # SE
    QuadNode(0, 50, 50, 100, 2),  # NW
    QuadNode(50, 50, 100, 100, 9) # NE
]

# High density threshold
min_density = 4

# Filter high density regions using functional approach
high_density_regions = list(filter(lambda node: node.density > min_density, root.children))

# Calculate weighted centroids
weighted_points = list(map(lambda node: (node.center_x() * node.density, node.center_y() * node.density, node.density), high_density_regions))

# Aggregate using reduce
accumulator = lambda acc, point: (acc[0] + point[0], acc[1] + point[1], acc[2] + point[2])
total_weighted_x, total_weighted_y, total_density = reduce(accumulator, weighted_points, (0, 0, 0))

# Compute final centroid with ternary operator for edge case
final_x_coordinate = total_weighted_x / total_density if total_density > 0 else 0

print(f"Result: {final_x_coordinate}")