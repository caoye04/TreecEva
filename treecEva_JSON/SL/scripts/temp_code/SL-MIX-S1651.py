import math
from collections import defaultdict

def compute_triangle_area(a, b, c):
    # Using Heron's formula for triangle area
    s = (a + b + c) / 2.0
    try:
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area
    except ValueError:
        return 0.0  # Invalid triangle

def law_of_cosines_side(b, c, angle_A_rad):
    # a^2 = b^2 + c^2 - 2bc*cos(A)
    a_squared = b*b + c*c - 2*b*c*math.cos(angle_A_rad)
    return math.sqrt(max(0, a_squared))

# Sensor positions relative to vessel (x,y) in meters
sensor_positions = {
    'S1': (0.0, 0.0),
    'S2': (100.0, 0.0),
    'S3': (0.0, 150.0)
}

# Sonar measurements to seabed feature (distances in meters)
sonar_measurements = {
    'S1': 120.5,
    'S2': 98.7,
    'S3': 160.2
}

# Calculate distances between sensors
side_lengths = defaultdict(float)
s1_s2 = math.sqrt((sensor_positions['S2'][0] - sensor_positions['S1'][0])**2 + 
                   (sensor_positions['S2'][1] - sensor_positions['S1'][1])**2)
s2_s3 = math.sqrt((sensor_positions['S3'][0] - sensor_positions['S2'][0])**2 + 
                   (sensor_positions['S3'][1] - sensor_positions['S2'][1])**2)
s1_s3 = math.sqrt((sensor_positions['S3'][0] - sensor_positions['S1'][0])**2 + 
                   (sensor_positions['S3'][1] - sensor_positions['S1'][1])**2)

side_lengths['S1_S2'] = s1_s2
side_lengths['S2_S3'] = s2_s3
side_lengths['S1_S3'] = s1_s3

# Calculate angle at S1 using law of cosines
# cos(A) = (b^2 + c^2 - a^2) / (2bc)
cos_angle_S1 = (s1_s2**2 + s1_s3**2 - s2_s3**2) / (2 * s1_s2 * s1_s3)
angle_S1_rad = math.acos(max(-1, min(1, cos_angle_S1)))

# Use divide and conquer approach to process measurements
processed_distances = []
for sensor in ['S1', 'S2', 'S3']:
    raw_distance = sonar_measurements[sensor]
    # Apply correction factor based on water temperature (simulated)
    corrected_distance = raw_distance * (1.0 + 0.0002 * 15.0)  # 15°C water temp
    processed_distances.append(corrected_distance)

# Compute virtual triangle side using law of cosines
virtual_side = law_of_cosines_side(processed_distances[1], processed_distances[2], angle_S1_rad)

# Calculate final triangle area
seabed_triangle_area = compute_triangle_area(processed_distances[0], processed_distances[1], virtual_side)

print(f"Result: {seabed_triangle_area:.2f}")