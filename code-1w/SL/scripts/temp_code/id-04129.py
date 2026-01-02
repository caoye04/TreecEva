from collections import defaultdict

# Simulate a robot's discrete movement along a planned path
def calculate_total_distance():
    path_x = [0, 1, 3, 6, 10]
    path_y = [0, 1, 2, 2, 0]
    total_distance = 0.0
    prev_x, prev_y = path_x[0], path_y[0]

    # Track direction changes using defaultdict (minor distraction)
    direction_changes = defaultdict(int)
    last_direction = None

    for i, (x, y) in enumerate(zip(path_x, path_y)):
        if i == 0:
            continue  # Skip first point
        
        # Calculate Manhattan segment distance
        segment_distance = abs(x - prev_x) + abs(y - prev_y)
        total_distance += segment_distance

        # Record direction type (irrelevant to final result)
        dx, dy = x - prev_x, y - prev_y
        if dx > 0 and dy == 0:
            curr_direction = 'right'
        elif dx < 0 and dy == 0:
            curr_direction = 'left'
        elif dy > 0 and dx == 0:
            curr_direction = 'up'
        elif dy < 0 and dx == 0:
            curr_direction = 'down'
        else:
            curr_direction = 'diagonal'
       
        if curr_direction != last_direction and last_direction is not None:
            direction_changes[curr_direction] += 1
        
        last_direction = curr_direction
        prev_x, prev_y = x, y

    # Irrelevant aggregation (distractor)
    total_changes = sum(direction_changes.values())
    
    return total_distance

result = calculate_total_distance()
print(f"Result: {result}")