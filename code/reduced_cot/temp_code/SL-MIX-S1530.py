import math
from statistics import mean, variance

def calculate_overlap_area(sensor1_pos, sensor1_radius, sensor2_pos, sensor2_radius):
    dx = sensor1_pos[0] - sensor2_pos[0]
    dy = sensor1_pos[1] - sensor2_pos[1]
    distance = math.sqrt(dx*dx + dy*dy)
    
    if distance >= sensor1_radius + sensor2_radius:
        return 0.0
    elif distance <= abs(sensor1_radius - sensor2_radius):
        return math.pi * min(sensor1_radius, sensor2_radius)**2
    else:
        r1_sq = sensor1_radius**2
        r2_sq = sensor2_radius**2
        d_sq = distance**2
        
        part1 = r1_sq * math.acos((d_sq + r1_sq - r2_sq)/(2 * distance * sensor1_radius))
        part2 = r2_sq * math.acos((d_sq + r2_sq - r1_sq)/(2 * distance * sensor2_radius))
        part3 = 0.5 * math.sqrt((-distance + sensor1_radius + sensor2_radius) * 
                               (distance + sensor1_radius - sensor2_radius) *
                               (distance - sensor1_radius + sensor2_radius) *
                               (distance + sensor1_radius + sensor2_radius))
        return part1 + part2 - part3

# Sensor network configuration
surveillance_sensors = [
    ((0, 0), 5.0),
    ((3, 4), 3.0),
    ((6, 0), 4.0),
    ((0, 8), 6.0)
]

# Object detections with timestamps
object_detections = [
    (1, (1.0, 1.0)),
    (2, (2.5, 3.5)),
    (3, (5.0, 1.0)),
    (4, (0.5, 7.5)),
    (5, (1.0, 1.0)),
    (1, (1.1, 1.1)),
    (2, (2.4, 3.6))
]

# Validation parameters
minimum_confidence = 0.75
maximum_jitter = 0.2

# Process detections
valid_objects = []
for obj_id, position in object_detections:
    detection_positions = [pos for oid, pos in object_detections if oid == obj_id]
    if len(detection_positions) >= 2:
        positions_x = [pos[0] for pos in detection_positions]
        positions_y = [pos[1] for pos in detection_positions]
        
        avg_position = (mean(positions_x), mean(positions_y))
        pos_variance = variance(positions_x) + variance(positions_y)
        
        # Short-circuit evaluation for efficiency
        if pos_variance <= maximum_jitter and len(detection_positions) >= 2:
            valid_objects.append((obj_id, avg_position))

# Calculate coverage overlaps
coverage_overlaps = []
sensor_count = len(surveillance_sensors)
for i in range(sensor_count):
    for j in range(i+1, sensor_count):
        overlap = calculate_overlap_area(
            surveillance_sensors[i][0], surveillance_sensors[i][1],
            surveillance_sensors[j][0], surveillance_sensors[j][1]
        )
        if overlap > 0.1:  # Only consider significant overlaps
            coverage_overlaps.append(overlap)

# Determine sensor activation pattern
active_sensors = 0
for sensor_pos, sensor_radius in surveillance_sensors:
    for _, obj_pos in valid_objects:
        dx = sensor_pos[0] - obj_pos[0]
        dy = sensor_pos[1] - obj_pos[1]
        distance = math.sqrt(dx*dx + dy*dy)
        # Logical operations for validation
        if distance <= sensor_radius and distance > 0.0:
            active_sensors += 1
            break

# Compute priority score using modular arithmetic
base_priority = int(mean(coverage_overlaps) * 100) if coverage_overlaps else 0
modular_factor = (len(valid_objects) * 7 + active_sensors * 11) % 13
confidence_factor = int(minimum_confidence * 100)

priority_score = (base_priority + modular_factor * confidence_factor) % 1000

print(f"Result: {priority_score}")