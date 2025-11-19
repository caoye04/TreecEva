from itertools import combinations
import math

def calculate_terrain_gradient(points):
    x1, y1, z1 = points[0]
    x2, y2, z2 = points[1]
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return (z2-z1) / distance if distance != 0 else 0

def process_elevation_data():
    # Simulated elevation points (x, y, elevation)
    survey_points = [
        (0.0, 0.0, 150.5),
        (3.0, 4.0, 180.2),
        (6.0, 8.0, 210.7),
        (9.0, 12.0, 195.3)
    ]
    
    # Calculate gradients between consecutive points
    gradients = [calculate_terrain_gradient([survey_points[i], survey_points[i+1]]) 
                 for i in range(len(survey_points)-1)]
    
    # Bitwise encoding of gradient patterns
    gradient_flags = [int(g*100) & 0xFF for g in gradients]
    encoded_pattern = 0
    for i, flag in enumerate(gradient_flags):
        encoded_pattern |= (flag << (i*8))
    
    # Geometric adjustment using hexagonal grid concept
    hex_radius = 2.5
    hex_area = (3 * math.sqrt(3) / 2) * (hex_radius ** 2)
    
    # Combine bitwise pattern with geometric factor
    adjusted_value = encoded_pattern ^ int(hex_area * 1000)
    
    # Extract specific bit segments
    segment_a = (adjusted_value >> 8) & 0xFF
    segment_b = adjusted_value & 0xFF
    
    # Final elevation marker calculation
    final_elevation_marker = (segment_a * segment_b) % 256
    return final_elevation_marker

final_elevation_marker = process_elevation_data()
print(f"Result: {final_elevation_marker}")