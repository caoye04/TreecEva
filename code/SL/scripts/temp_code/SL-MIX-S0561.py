import math
from contextlib import contextmanager
from collections import namedtuple

@contextmanager
def elevation_data_handler(filename):
    data_points = [(0, 100), (50, 120), (100, 80), (150, 90), (200, 110)]
    try:
        yield data_points
    finally:
        pass

ElevationPoint = namedtuple('ElevationPoint', ['distance', 'height'])

with elevation_data_handler('terrain.dat') as raw_data:
    points = [ElevationPoint(d, h) for d, h in raw_data]
    
    # Calculate elevation changes
    elevation_changes = []
    for i in range(1, len(points)):
        delta_distance = points[i].distance - points[i-1].distance
        delta_height = points[i].height - points[i-1].height
        elevation_changes.append(delta_height / delta_distance if delta_distance != 0 else 0)
    
    # Determine slope category based on average change
    avg_change = sum(elevation_changes) / len(elevation_changes)
    
    # Switch-like logic for slope categorization
    if avg_change > 0.5:
        slope_category = 'steep'
    elif avg_change > 0.1:
        slope_category = 'moderate'
    elif avg_change > -0.1:
        slope_category = 'flat'
    else:
        slope_category = 'declining'
    
    # Geometry calculation for optimal solar panel angle
    base_angle_radians = math.atan(avg_change)
    base_angle_degrees = math.degrees(base_angle_radians)
    
    # Adjust angle based on category
    adjustment_factor = 15  # degrees
    if slope_category == 'steep':
        optimal_angle_degrees = base_angle_degrees + adjustment_factor
    elif slope_category == 'moderate':
        optimal_angle_degrees = base_angle_degrees + adjustment_factor/2
    elif slope_category == 'flat':
        optimal_angle_degrees = base_angle_degrees
    else:  # declining
        optimal_angle_degrees = base_angle_degrees - adjustment_factor
    
    # Final adjustment for southern hemisphere
    hemisphere_adjustment = -5  # degrees
    optimal_angle_degrees = optimal_angle_degrees + hemisphere_adjustment

print(f"Result: {round(optimal_angle_degrees, 2)}")