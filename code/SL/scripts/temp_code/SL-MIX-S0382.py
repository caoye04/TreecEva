import math
from collections import defaultdict

def compute_sensor_centroid_offset(readings):
    x_components = []
    y_components = []
    weights = []
    
    for angle_deg, distance in readings.items():
        angle_rad = math.radians(angle_deg)
        x_comp = distance * math.cos(angle_rad)
        y_comp = distance * math.sin(angle_rad)
        weight = 1.0 / (1 + math.exp(-distance))
        
        x_components.append(x_comp)
        y_components.append(y_comp)
        weights.append(weight)
    
    weighted_x = sum(x * w for x, w in zip(x_components, weights))
    weighted_y = sum(y * w for y, w in zip(y_components, weights))
    total_weight = sum(weights)
    
    if total_weight == 0:
        return 0.0
    
    centroid_x = weighted_x / total_weight
    centroid_y = weighted_y / total_weight
    
    return math.sqrt(centroid_x**2 + centroid_y**2)

# Sensor readings: {angular_position_in_degrees: radial_distance}
sensor_readings_map = {
    0: 10.0,
    45: 14.14,
    90: 10.0,
    135: 14.14,
    180: 10.0,
    225: 14.14,
    270: 10.0,
    315: 14.14
}

# Processing pipeline with functional transformations
adjusted_readings = dict(map(lambda item: (item[0], item[1] * 0.9 if item[1] > 12 else item[1]), sensor_readings_map.items()))
filtered_readings = dict(filter(lambda item: item[1] >= 9.0, adjusted_readings.items()))

# Compute the centroid offset using the processed readings
offset_magnitude = compute_sensor_centroid_offset(filtered_readings)

# Calculate the final metric incorporating geometric properties
angular_span = len(filtered_readings) * 45  # Each reading covers 45 degrees
radial_displacement_index = round((offset_magnitude * angular_span) / 360.0, 2)

print(f"Result: {radial_displacement_index}")