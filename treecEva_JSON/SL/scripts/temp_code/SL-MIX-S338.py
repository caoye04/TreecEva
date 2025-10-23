from dataclasses import dataclass
from typing import Optional, Tuple
import math

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, x: float, y: float, width: float, height: float):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def contains(self, point: Point) -> bool:
        return (self.x <= point.x < self.x + self.width and 
                self.y <= point.y < self.y + self.height)

@dataclass
class QuadTree:
    boundary: Rectangle
    capacity: int = 1
    points: list = None
    divided: bool = False
    northeast: Optional['QuadTree'] = None
    northwest: Optional['QuadTree'] = None
    southeast: Optional['QuadTree'] = None
    southwest: Optional['QuadTree'] = None
    
    def __post_init__(self):
        if self.points is None:
            self.points = []
    
    def subdivide(self):
        x = self.boundary.x
        y = self.boundary.y
        w = self.boundary.width / 2
        h = self.boundary.height / 2
        
        ne = Rectangle(x + w, y, w, h)
        self.northeast = QuadTree(ne, self.capacity)
        
        nw = Rectangle(x, y, w, h)
        self.northwest = QuadTree(nw, self.capacity)
        
        se = Rectangle(x + w, y + h, w, h)
        self.southeast = QuadTree(se, self.capacity)
        
        sw = Rectangle(x, y + h, w, h)
        self.southwest = QuadTree(sw, self.capacity)
        
        self.divided = True
    
    def insert(self, point: Point) -> bool:
        if not self.boundary.contains(point):
            return False
        
        if len(self.points) < self.capacity and not self.divided:
            self.points.append(point)
            return True
        
        if not self.divided:
            self.subdivide()
            for p in self.points:
                self.northeast.insert(p) or \
                self.northwest.insert(p) or \
                self.southeast.insert(p) or \
                self.southwest.insert(p)
            self.points = []
        
        return (self.northeast.insert(point) or
                self.northwest.insert(point) or
                self.southeast.insert(point) or
                self.southwest.insert(point))

    def count_leaf_nodes(self) -> int:
        if not self.divided and len(self.points) <= self.capacity:
            return 1
        
        count = 0
        if self.northeast:
            count += self.northeast.count_leaf_nodes()
        if self.northwest:
            count += self.northwest.count_leaf_nodes()
        if self.southeast:
            count += self.southeast.count_leaf_nodes()
        if self.southwest:
            count += self.southwest.count_leaf_nodes()
        
        return count

# Initialize the quadtree with a large boundary
boundary = Rectangle(0, 0, 100, 100)
quadtree = QuadTree(boundary, capacity=1)

# Tree planting coordinates
planting_sites = [
    Point(25, 25),
    Point(75, 25),
    Point(25, 75),
    Point(75, 75),
    Point(50, 50),
    Point(10, 10),
    Point(90, 90),
    Point(10, 90),
    Point(90, 10)
]

# Insert all trees
for site in planting_sites:
    quadtree.insert(site)

# Count leaf nodes
leaf_node_count = quadtree.count_leaf_nodes()
print(f"Result: {leaf_node_count}")