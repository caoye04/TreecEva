from collections import defaultdict
import itertools

def validate_angles(angles):
    return sum(angles) == 180 and all(angle > 0 for angle in angles)

def generate_triangles(angle_pool):
    valid_configs = set()
    for combo in itertools.combinations_with_replacement(angle_pool, 3):
        if validate_angles(combo):
            valid_configs.add(tuple(sorted(combo)))
    return valid_configs

# Angular measurements available for triangle formation
angular_measurements = [30, 60, 90, 45, 120, 15]

# Generate all valid triangle configurations
triangle_configurations = generate_triangles(angular_measurements)

# Count occurrences of each angle in all valid configurations
angle_usage = defaultdict(int)
for config in triangle_configurations:
    for angle in config:
        angle_usage[angle] += 1

# Determine valid_triangle_count based on angle usage frequencies
valid_triangle_count = 0
for config in triangle_configurations:
    if all(angle_usage[angle] >= 2 for angle in config):
        valid_triangle_count += 1
    elif any(angle == 90 for angle in config):  # Right triangles given priority
        valid_triangle_count += 1

print(f"Result: {valid_triangle_count}")