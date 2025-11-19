from collections import deque
import math

def calculate_polygon_area(vertices):
    n = len(vertices)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    return abs(area) / 2.0

class ZoneProcessor:
    def __init__(self):
        self.zone_stack = []
        self.overlap_areas = set()
    
    def add_zone(self, polygon_coords):
        area = calculate_polygon_area(polygon_coords)
        self.zone_stack.append(area)
        
    def compute_overlaps(self):
        temp_areas = []
        while self.zone_stack:
            current_area = self.zone_stack.pop()
            if current_area > 100:
                adjusted_area = current_area * 0.85
                temp_areas.append(adjusted_area)
            else:
                temp_areas.append(current_area)
        
        for idx, area in enumerate(temp_areas):
            if idx % 2 == 0:
                self.overlap_areas.add(math.floor(area))
            else:
                self.overlap_areas.add(math.ceil(area))
        
        return sum(self.overlap_areas)

def main():
    processor = ZoneProcessor()
    
    # Define urban planning zones as polygon coordinates
    zone_a = [(0, 0), (0, 20), (20, 20), (20, 0)]      # Square zone
    zone_b = [(10, 10), (10, 30), (30, 30), (30, 10)]  # Overlapping square
    zone_c = [(5, 5), (5, 15), (15, 15), (15, 5)]      # Smaller internal zone
    zone_d = [(25, 25), (25, 35), (35, 35), (35, 25)]  # Non-overlapping zone
    
    # Process zones
    processor.add_zone(zone_a)
    processor.add_zone(zone_b)
    processor.add_zone(zone_c)
    processor.add_zone(zone_d)
    
    # Compute overlaps and get total
    total_overlap_index = processor.compute_overlaps()
    
    print(f"Result: {total_overlap_index}")

if __name__ == "__main__":
    main()