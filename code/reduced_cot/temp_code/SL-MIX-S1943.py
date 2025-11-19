import math
from collections import deque

def calculate_bearing_angle(dx, dy):
    angle = math.atan2(dy, dx)
    return angle if angle >= 0 else angle + 2 * math.pi

def normalize_angle(angle):
    while angle > 2 * math.pi:
        angle -= 2 * math.pi
    while angle < 0:
        angle += 2 * math.pi
    return angle

# Initialize data structures
sensor_queue = deque([3+4j, -1+2j, 5-3j, 2+7j])
correction_stack = [0b1010, 0b1100, 0b0011]
waypoint_map = {
    'alpha': 1+1j,
    'beta': -2+3j,
    'gamma': 4-1j
}

# Process sensor data
processed_vectors = []
while sensor_queue:
    vector = sensor_queue.popleft()
    magnitude = abs(vector)
    if magnitude > 5.0:
        # Apply correction from stack if available
        if correction_stack:
            correction = correction_stack.pop()
            # Bitwise AND with 0xF to limit correction range
            limited_correction = correction & 0xF
            # Convert to float adjustment factor
            adjustment = limited_correction / 16.0
            # Apply correction to vector
            corrected_vector = complex(vector.real * (1 + adjustment), vector.imag * (1 + adjustment))
            processed_vectors.append(corrected_vector)
        else:
            processed_vectors.append(vector)
    else:
        processed_vectors.append(vector)

# Calculate bearing angles
bearing_angles = list(map(lambda v: calculate_bearing_angle(v.real, v.imag), processed_vectors))

# Statistical processing - calculate mean bearing
mean_bearing = sum(bearing_angles) / len(bearing_angles)

# Geometry processing - find centroid of waypoints
waypoint_positions = list(waypoint_map.values())
centroid_x = sum(pos.real for pos in waypoint_positions) / len(waypoint_positions)
centroid_y = sum(pos.imag for pos in waypoint_positions) / len(waypoint_positions)
centroid = complex(centroid_x, centroid_y)

# Calculate angle to centroid
angle_to_centroid = calculate_bearing_angle(centroid_x, centroid_y)

# Final heading adjustment calculation
# XOR the mean bearing (in degrees) with a constant
mean_bearing_deg = int(math.degrees(mean_bearing)) & 0xFF
constant_factor = 0b10110110
xored_component = mean_bearing_deg ^ constant_factor

# Combine with angle to centroid using bitwise operations
angle_to_centroid_deg = int(math.degrees(angle_to_centroid)) & 0xFF
shifted_angle = angle_to_centroid_deg << 2
combined_value = xored_component | shifted_angle

# Apply final normalization with floating point precision
final_heading_adjustment = normalize_angle(combined_value / 100.0)

print(f"Result: {final_heading_adjustment}")