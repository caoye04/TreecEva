import heapq
import statistics
from math import sqrt

def calculate_euclidean_distance(point1, point2):
    return sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))

def process_sonar_data(sensor_readings):
    # Convert readings to matrix form
    matrix = [sensor_readings[i:i+5] for i in range(0, len(sensor_readings), 5)]
    
    # Calculate mean of each row using statistics
    row_means = [statistics.mean(row) for row in matrix]
    
    # Find coordinates of maximum values in each row
    max_coords = []
    for i, row in enumerate(matrix):
        max_val = max(row)
        j = row.index(max_val)
        max_coords.append((i, j))
    
    # Calculate distances between consecutive max points
    distances = []
    for i in range(len(max_coords)-1):
        dist = calculate_euclidean_distance(max_coords[i], max_coords[i+1])
        distances.append(dist)
    
    # Use heap to find 3 largest distances
    largest_distances = heapq.nlargest(3, distances)
    
    # Apply transformation using array operations
    transformed_values = list(map(lambda x: x * 2.5 if x > 3 else x * 1.2, largest_distances))
    
    # Calculate final anomaly score
    if transformed_values:
        anomaly_score = statistics.variance(transformed_values) * len(transformed_values)
    else:
        anomaly_score = 0.0
    
    return anomaly_score

# Sonar sensor readings from a 5x5 grid
sonar_readings = [
    12.4, 15.2, 18.7, 14.3, 16.8,
    22.1, 25.6, 23.4, 21.9, 24.7,
    31.5, 35.2, 33.8, 32.1, 34.6,
    42.3, 45.8, 43.7, 41.2, 44.9,
    51.6, 55.3, 53.9, 52.4, 54.8
]

anomaly_score = process_sonar_data(sonar_readings)
print(f"Result: {anomaly_score}")