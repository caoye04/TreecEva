import math
from collections import defaultdict
from statistics import variance

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def get_quadrant(point):
    x, y = point
    if x >= 0 and y >= 0:
        return 1
    elif x < 0 and y >= 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4

# Robotic arm movement sequence
movement_sequence = [(0, 0), (3, 4), (-2, 5), (-5, -1), (4, -3), (1, 1)]

# State machine for tracking operations
arm_state = {
    'current_position': (0, 0),
    'distances': [],
    'quadrant_visits': defaultdict(int),
    'operation_count': 0
}

# Process each movement
for target_position in movement_sequence[1:]:
    # Calculate distance moved
    distance = calculate_distance(arm_state['current_position'], target_position)
    arm_state['distances'].append(distance)
    
    # Update position
    arm_state['current_position'] = target_position
    
    # Update quadrant visits using modular arithmetic for cyclic tracking
    quadrant = get_quadrant(target_position)
    arm_state['quadrant_visits'][quadrant] = (arm_state['quadrant_visits'][quadrant] + 1) % 3
    
    # Increment operation counter
    arm_state['operation_count'] += 1

# Calculate efficiency using statistical variance
if len(arm_state['distances']) > 1:
    base_variance = variance(arm_state['distances'])
else:
    base_variance = 0

# Apply correction factor based on quadrant balance
quadrant_counts = [arm_state['quadrant_visits'][i] for i in range(1, 5)]
imbalance_factor = max(quadrant_counts) - min(quadrant_counts)

# Final efficiency rating calculation
efficiency_rating = (base_variance * 100 + imbalance_factor * 5) / arm_state['operation_count']

# Apply floating point precision correction
efficiency_rating = round(efficiency_rating, 2)

print(f"Result: {efficiency_rating}")