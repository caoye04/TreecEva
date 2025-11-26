def calculate_navigation_path():
    import math
    
    # Navigation parameters
    total_distance = 150.0
    obstacle_detected = True
    obstacle_radius = 15.0
    
    # Initial path calculation
    path_segment = total_distance / 3
    adjusted_segment = path_segment + 2.5
    
    # Obstacle avoidance logic
    if obstacle_detected:
        obstacle_offset = obstacle_radius * 1.2
        remaining_distance = total_distance - obstacle_offset
    else:
        remaining_distance = total_distance
        obstacle_offset = 0
    
    # Final calculation
    final_distance = remaining_distance - obstacle_offset
    
    # Redundant calculations (distractors for intervention level)
    temp_angle = math.radians(45)
    unused_value = math.sin(temp_angle)
    
    print(f"Target result: {final_distance}")
    return final_distance

calculate_navigation_path()