import math
from functools import reduce
from itertools import combinations

def calculate_geometric_mean(deviations):
    product = reduce(lambda x, y: x * y, deviations)
    return product ** (1/len(deviations))

def validate_within_polygon(point, vertices):
    x, y = point
    n = len(vertices)
    inside = False
    p1x, p1y = vertices[0]
    for i in range(1, n + 1):
        p2x, p2y = vertices[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside

def process_sonar_data(raw_readings):
    # State machine for processing pipeline
    state = 'INIT'
    filtered_deviations = []
    boundary_vertices = [(0,0), (10,0), (10,10), (0,10)]  # Square boundary
    
    for reading in raw_readings:
        if state == 'INIT':
            if reading['confidence'] > 0.8:
                state = 'FILTERING'
            else:
                continue
        
        if state == 'FILTERING':
            position = (reading['x'], reading['y'])
            if validate_within_polygon(position, boundary_vertices):
                deviation = math.sqrt((reading['x'] - reading['expected_x'])**2 + 
                                    (reading['y'] - reading['expected_y'])**2)
                if deviation < 5.0:  # Early return condition
                    filtered_deviations.append(deviation)
            if len(filtered_deviations) >= 10:
                state = 'ANALYZING'
        
        if state == 'ANALYZING':
            break
    
    return filtered_deviations

# Raw sonar data with confidence scores and expected positions
sonar_readings = [
    {'x': 2.1, 'y': 3.2, 'expected_x': 2.0, 'expected_y': 3.0, 'confidence': 0.9},
    {'x': 5.5, 'y': 4.8, 'expected_x': 5.0, 'expected_y': 5.0, 'confidence': 0.85},
    {'x': 8.2, 'y': 7.1, 'expected_x': 8.0, 'expected_y': 7.0, 'confidence': 0.7},  # Low confidence
    {'x': 1.8, 'y': 2.9, 'expected_x': 2.0, 'expected_y': 3.0, 'confidence': 0.92},
    {'x': 6.3, 'y': 5.2, 'expected_x': 6.0, 'expected_y': 5.0, 'confidence': 0.88},
    {'x': 3.7, 'y': 4.1, 'expected_x': 4.0, 'expected_y': 4.0, 'confidence': 0.91},
    {'x': 9.1, 'y': 8.9, 'expected_x': 9.0, 'expected_y': 9.0, 'confidence': 0.87},
    {'x': 4.2, 'y': 3.8, 'expected_x': 4.0, 'expected_y': 4.0, 'confidence': 0.89},
    {'x': 7.5, 'y': 6.7, 'expected_x': 7.0, 'expected_y': 7.0, 'confidence': 0.93},
    {'x': 2.9, 'y': 5.3, 'expected_x': 3.0, 'expected_y': 5.0, 'confidence': 0.86},
    {'x': 5.8, 'y': 4.2, 'expected_x': 6.0, 'expected_y': 4.0, 'confidence': 0.94},
    {'x': 1.2, 'y': 1.1, 'expected_x': 1.0, 'expected_y': 1.0, 'confidence': 0.95}
]

# Process the data through our pipeline
processed_deviations = process_sonar_data(sonar_readings)

# Calculate statistical measures
if len(processed_deviations) > 1:
    mean_deviation = sum(processed_deviations) / len(processed_deviations)
    variance = sum((d - mean_deviation) ** 2 for d in processed_deviations) / (len(processed_deviations) - 1)
    std_deviation = math.sqrt(variance)
    
    # Apply geometric correction factor
    geometric_mean = calculate_geometric_mean(processed_deviations)
    
    # Dynamic programming approach to find optimal adjustment
    dp_table = [0] * (len(processed_deviations) + 1)
    for i in range(1, len(processed_deviations) + 1):
        dp_table[i] = max(dp_table[i-1], dp_table[i-1] + processed_deviations[i-1] - mean_deviation)
    
    validated_avg_deviation = dp_table[-1] + geometric_mean
else:
    validated_avg_deviation = 0

print(f"Result: {round(validated_avg_deviation, 4)}")