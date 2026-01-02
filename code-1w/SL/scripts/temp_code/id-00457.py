def compute_route_length(waypoints, step_distances):
    total_distance = 0
    index_map = {name: i for i, name in enumerate(waypoints)}
    route = ['home', 'market', 'park', 'library', 'home']
    
    # Unrelated tracking variables (minor interference)
    visit_count = {point: 0 for point in waypoints}
    current_time = 8  # Starting at 8 AM

    for i in range(len(route) - 1):
        start = route[i]
        end = route[i + 1]
        idx1 = index_map[start]
        idx2 = index_map[end]
        segment_key = tuple(sorted([idx1, idx2]))
        if idx1 == idx2:
            continue
        distance = step_distances.get(segment_key, 0)
        total_distance += distance
    
    # Linear search to adjust for detour
    detour_penalty = 0
    for i, loc in enumerate(waypoints):
        if loc == 'park':
            detour_penalty = i * 0.5
    
    total_distance -= detour_penalty
    return total_distance

# Main execution
locations = ['home', 'market', 'park', 'library']
distances = {
    (0, 1): 3.0,  # home -> market
    (1, 2): 2.5,  # market -> park
    (2, 3): 4.0,  # park -> library
    (0, 3): 6.0   # home -> library (direct)
}

# Compute final result
total_distance = compute_route_length(locations, distances)
print(f"Result: {total_distance}")