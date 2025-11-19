import re
from itertools import combinations
from math import sqrt, pow
class Sensor:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

def circle_intersection(circle1, circle2):
    x1, y1, r1 = circle1.x, circle1.y, circle1.radius
    x2, y2, r2 = circle2.x, circle2.y, circle2.radius
    d = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
    
    if d > r1 + r2 or d < abs(r1 - r2) or d == 0:
        return []
    
    a = (pow(r1, 2) - pow(r2, 2) + pow(d, 2)) / (2 * d)
    h = sqrt(pow(r1, 2) - pow(a, 2))
    
    x3 = x1 + a * (x2 - x1) / d
    y3 = y1 + a * (y2 - y1) / d
    
    ix1 = x3 + h * (y2 - y1) / d
    iy1 = y3 - h * (x2 - x1) / d
    ix2 = x3 - h * (y2 - y1) / d
    iy2 = y3 + h * (x2 - x1) / d
    
    return [(ix1, iy1), (ix2, iy2)]

def encode_coordinate(coord_tuple):
    x, y = coord_tuple
    return f"E{int(x*100):05d}{int(y*100):05d}"

sensors = [
    Sensor(0, 0, 5),
    Sensor(4, 0, 5),
    Sensor(2, 3, 4),
    Sensor(1, -2, 3)
]

valid_intersection_count = 0
for s1, s2 in combinations(sensors, 2):
    intersections = circle_intersection(s1, s2)
    for point in intersections:
        encoded = encode_coordinate(point)
        # Geographic constraint: encoded coordinate must match pattern for northern hemisphere and eastern meridian
        if re.match(r'^E\d{5}[0-4]\d{4}$', encoded):
            valid_intersection_count += 1

print(f"Result: {valid_intersection_count}")