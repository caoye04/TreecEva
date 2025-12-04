def analyze_hiking_trail(elevation_points, trail_markers):
    # Calculate distance segments between markers
    path_segments = []
    for i in range(1, len(elevation_points)):
        # Distance formula with elevation change
        segment = ((elevation_points[i] - elevation_points[i-1]) ** 2 + 100) ** 0.5
        path_segments.append(round(segment, 2))
    
    # Find markers of interest
    rest_areas = []
    scenic_points = []
    for marker in trail_markers:
        if marker.get('type') == 'rest':
            rest_areas.append(marker.get('position', 0))
        elif marker.get('type') == 'scenic':
            scenic_points.append(marker.get('position', 0))
    
    # Calculate some statistics for the report
    total_distance = sum(path_segments)
    average_segment = sum(path_segments) / len(path_segments) if path_segments else 0
    
    # Weather adjustment factor (not used in final calculation)
    weather_factors = [1.1, 0.9, 1.05, 0.95, 1.0]
    adjusted_segments = [seg * weather_factors[i % len(weather_factors)] 
                        for i, seg in enumerate(path_segments)]
    
    # Determine optimal path between specific markers
    start_idx = 2
    end_idx = 6
    
    # Calculate alternate paths (distraction)
    alt_path_1 = sum(path_segments[1:5])
    alt_path_2 = sum(path_segments[3:8]) if len(path_segments) >= 8 else 0
    
    # Select the optimal path section
    optimal_distance = sum(path_segments[start_idx:end_idx])
    
    # Calculate difficulty rating (distraction)
    difficulty_rating = (optimal_distance * 0.3 + 
                        max(path_segments[start_idx:end_idx]) * 0.7)
    
    print(f"Result: {optimal_distance}")
    return optimal_distance

# Trail elevation points
elevation_points = [100, 150, 120, 180, 200, 210, 190, 220]

# Trail markers with position and type
trail_markers = [
    {'position': 0, 'type': 'start'},
    {'position': 2, 'type': 'rest'},
    {'position': 4, 'type': 'scenic'},
    {'position': 6, 'type': 'end'}
]

result = analyze_hiking_trail(elevation_points, trail_markers)