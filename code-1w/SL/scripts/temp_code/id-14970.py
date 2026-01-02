def calculate_route_efficiency(waypoints, velocities):
    total_distance = 0.0
    total_time = 0.0
    
    # Unrelated tracking variables (minimal interference)
    segment_count = len(waypoints) - 1
    max_speed = max(velocities)
    min_speed = min(velocities)
    speed_fluctuations = 0
    
    for i in range(segment_count):
        start_point = waypoints[i]
        end_point = waypoints[i + 1]
        
        # Compute Euclidean segment distance
        segment_distance = ((end_point[0] - start_point[0])**2 + 
                           (end_point[1] - start_point[1])**2)**0.5
        
        # Accumulate total distance
        total_distance += segment_distance
        
        # Time for this segment based on corresponding velocity
        segment_time = segment_distance / velocities[i] if velocities[i] > 0 else 0
        total_time += segment_time
        
        # Track speed changes (irrelevant to final result)
        if i > 0:
            speed_fluctuations += abs(velocities[i] - velocities[i-1])
    
    # Efficiency ratio (not used in answer)
    efficiency = total_distance / total_time if total_time > 0 else 0
    
    return total_distance

# Define route data
locations = [(0, 0), (3, 4), (6, 8), (9, 12)]
speeds = [5, 10, 15]

# Main computation
result = calculate_route_efficiency(locations, speeds)
total_distance = round(result, 3)

print(f"Result: {total_distance}")