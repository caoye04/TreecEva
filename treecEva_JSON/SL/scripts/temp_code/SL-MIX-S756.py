import re
from dataclasses import dataclass
from itertools import combinations
class CoordinateProcessor:
    def __init__(self):
        self.coordinates = []
    
    def extract_coordinates(self, data_string):
        pattern = r'POINT\(([-+]?[0-9]*\.?[0-9]+)\s+([-+]?[0-9]*\.?[0-9]+)\)'
        matches = re.findall(pattern, data_string)
        for match in matches:
            x, y = float(match[0]), float(match[1])
            self.coordinates.append((x, y))
    
    def calculate_polygon_area(self):
        if len(self.coordinates) < 3:
            return 0.0
        area = 0.0
        n = len(self.coordinates)
        for i in range(n):
            j = (i + 1) % n
            area += self.coordinates[i][0] * self.coordinates[j][1]
            area -= self.coordinates[j][0] * self.coordinates[i][1]
        return abs(area) / 2.0

data_feed = "Survey data: POINT(0.0 0.0) POINT(4.0 0.0) POINT(4.0 3.0) POINT(0.0 3.0) Calibration: POINT(1.0 1.0) POINT(2.0 1.0)"
processor = CoordinateProcessor()
processor.extract_coordinates(data_feed)
boundary_area = processor.calculate_polygon_area()
# Apply correction factor using itertools
if len(processor.coordinates) >= 4:
    coord_pairs = list(combinations(processor.coordinates[:4], 2))
    distance_sum = sum(((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5 for p1, p2 in coord_pairs)
    boundary_area = boundary_area * (1.0 + distance_sum/100.0)
print(f"Result: {boundary_area}")