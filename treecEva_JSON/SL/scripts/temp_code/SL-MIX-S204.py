import re
from collections import defaultdict
from math import sqrt, acos, pi

def calculate_velocity_magnitude(vx, vy, vz):
    return sqrt(vx**2 + vy**2 + vz**2)

def compute_vector_angle(v1, v2):
    dot_product = sum(a*b for a, b in zip(v1, v2))
    magnitudes = [sqrt(sum(x**2 for x in v)) for v in [v1, v2]]
    if magnitudes[0] == 0 or magnitudes[1] == 0:
        return 0
    cos_angle = dot_product / (magnitudes[0] * magnitudes[1])
    # Clamping to avoid numerical errors
    cos_angle = max(-1, min(1, cos_angle))
    return acos(cos_angle) * (180 / pi)

# Raw telemetry data: drone_id -> [(timestamp, x, y, z, vx, vy, vz)]
drone_telemetry_data = {
    'DRN-7A': [
        (1000, 15.2, 22.8, 5.1, 2.1, -1.3, 0.5),
        (1001, 17.3, 21.5, 5.6, 3.2, -0.9, 0.7),
        (1002, 20.5, 20.6, 6.3, 1.8, -0.4, 0.3)
    ],
    'DRN-BX4': [
        (1000, 30.1, 15.7, 10.2, -1.2, 2.8, -0.4),
        (1001, 28.9, 18.5, 9.8, -2.1, 3.1, -0.6),
        (1002, 26.8, 21.6, 9.2, -1.5, 2.4, -0.3)
    ],
    'DRN-Z9Q': [
        (1000, 5.4, 40.3, 2.7, 0.8, -3.2, 1.1),
        (1001, 6.2, 37.1, 3.8, 1.1, -4.1, 1.3),
        (1002, 7.3, 33.0, 5.1, 0.9, -3.8, 1.0)
    ]
}

# Process telemetry data
drone_metrics = defaultdict(dict)
for drone_id, telemetry_points in drone_telemetry_data.items():
    velocities = [calculate_velocity_magnitude(*point[3:]) for point in telemetry_points]
    positions = [(point[1], point[2], point[3]) for point in telemetry_points]
    
    # Compute average velocity
    avg_velocity = sum(velocities) / len(velocities)
    
    # Compute total displacement
    start_pos, end_pos = positions[0], positions[-1]
    displacement = sqrt(sum((end_pos[i] - start_pos[i])**2 for i in range(3)))
    
    # Compute directional consistency (average angle deviation)
    vectors = [(positions[i][0]-positions[i-1][0], positions[i][1]-positions[i-1][1], positions[i][2]-positions[i-1][2]) 
               for i in range(1, len(positions))]
    angles = [compute_vector_angle(vectors[i], vectors[i+1]) for i in range(len(vectors)-1)]
    avg_angle_deviation = sum(angles) / len(angles) if angles else 0
    
    drone_metrics[drone_id] = {
        'avg_velocity': avg_velocity,
        'displacement': displacement,
        'direction_stability': 100 - avg_angle_deviation  # Invert so higher is better
    }

# Apply pattern matching to drone IDs to create weights
pattern_weights = {
    r'^DRN-[A-Z]\d$': 1.2,      # Standard model
    r'^DRN-[A-Z]{2}\d$': 1.5,    # Advanced model
    r'^DRN-[A-Z]\d[A-Z]$': 1.0   # Basic model
}

weighted_scores = {}
for drone_id, metrics in drone_metrics.items():
    weight = 1.0
    for pattern, w in pattern_weights.items():
        if re.match(pattern, drone_id):
            weight = w
            break
    score = (metrics['avg_velocity'] * 0.4 + 
             metrics['displacement'] * 0.3 + 
             metrics['direction_stability'] * 0.3) * weight
    weighted_scores[drone_id] = score

# Find drone with highest weighted score
top_drone = max(weighted_scores, key=weighted_scores.get)

# Create index mapping
drone_index_map = {drone: idx for idx, drone in enumerate(sorted(drone_metrics.keys()))}

# Calculate final drone index with geometric adjustment
final_drone_index = (drone_index_map[top_drone] * 3) + int(sqrt(weighted_scores[top_drone]))

# TARGET OUTPUT VARIABLE
print(f"Result: {final_drone_index}")