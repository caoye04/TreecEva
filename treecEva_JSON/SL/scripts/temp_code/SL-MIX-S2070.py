import math
import re
from dataclasses import dataclass
from typing import List

def validate_coordinates(func):
    def wrapper(*args, **kwargs):
        point = args[1]  # Assuming first arg is self, second is the point
        if not (-90 <= point.latitude <= 90 and -180 <= point.longitude <= 180):
            raise ValueError("Invalid coordinates")
        return func(*args, **kwargs)
    return wrapper

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b) if a and b else 0

@dataclass
class TerrainPoint:
    latitude: float
    longitude: float
    elevation: float
    
    @validate_coordinates
    def calculate_slope_to(self, other_point: 'TerrainPoint') -> float:
        # Calculate Euclidean distance between points
        lat_diff = other_point.latitude - self.latitude
        lon_diff = other_point.longitude - self.longitude
        elev_diff = other_point.elevation - self.elevation
        
        # Calculate slope as angle in degrees
        horizontal_distance = math.sqrt(lat_diff**2 + lon_diff**2)
        if horizontal_distance == 0:
            return 0.0
        slope_radians = math.atan(elev_diff / horizontal_distance)
        return math.degrees(slope_radians)

# Terrain data
raw_data = [
    "POINT(40.7128,-74.0060,12)",
    "POINT(34.0522,-118.2437,56)",
    "POINT(41.8781,-87.6298,89)",
    "POINT(29.7604,-95.3698,32)",
    "POINT(39.9526,-75.1652,78)",
    "POINT(33.4484,-112.0740,91)",
    "POINT(35.2271,-80.8431,45)",
    "POINT(32.7765,-96.7970,23)"
]

# Parse raw data using regex
points = []
for entry in raw_data:
    match = re.match(r"POINT\(([^,]+),([^,]+),([^\)]+)\)", entry)
    if match:
        lat, lon, elev = map(float, match.groups())
        points.append(TerrainPoint(lat, lon, elev))

# Find optimal landing zones
optimal_landing_zones = 0
slope_threshold = 15.0

for i, point_a in enumerate(points):
    valid_zone = True
    adjacent_count = 0
    
    for j, point_b in enumerate(points):
        if i == j:
            continue
            
        # Calculate distance
        lat_diff = point_b.latitude - point_a.latitude
        lon_diff = point_b.longitude - point_a.longitude
        distance = math.sqrt(lat_diff**2 + lon_diff**2)
        
        # Only consider points within a certain range
        if distance > 5.0:  # Arbitrary unit
            continue
            
        adjacent_count += 1
        slope = point_a.calculate_slope_to(point_b)
        
        # If any adjacent point has too steep a slope, not a valid zone
        if abs(slope) > slope_threshold:
            valid_zone = False
            break
    
    # Apply number theory constraint
    if valid_zone and adjacent_count > 0:
        # Check if adjacent count and elevation satisfy LCM condition
        elevation_factor = int(point_a.elevation) % 10
        if elevation_factor == 0:
            elevation_factor = 10
            
        calculated_lcm = lcm(adjacent_count, elevation_factor)
        if calculated_lcm % 3 == 0:  # Additional constraint
            optimal_landing_zones += 1

print(f"Result: {optimal_landing_zones}")