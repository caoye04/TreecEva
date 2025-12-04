def calculate_route():
    # Base coordinates for the hiking trail segments
    trail_segments = [(0, 0), (3, 4), (7, 2), (10, 8)]
    
    # Weather conditions affect which path we take
    weather_factor = 1.5  # Clear day factor
    rain_chance = 30  # Percent chance of rain (not used in calculation)
    
    # Alternative trail segments (not used in final route)
    scenic_detour = [(3, 4), (5, 7), (8, 6), (10, 8)]
    
    # Function to calculate Euclidean distance between points
    distance_calc = lambda p1, p2: ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5
    
    # Calculate direct distances between consecutive points
    distances = [distance_calc(trail_segments[i], trail_segments[i+1]) 
                for i in range(len(trail_segments)-1)]
    
    # Track elevation changes (not used in final calculation)
    elevation_changes = [10, -5, 15]
    elevation_strain = sum(abs(e) for e in elevation_changes) / 10
    
    # Compute terrain difficulty factor
    terrain_type = "rocky"  # Could be "rocky", "flat", or "mixed"
    difficulty_multiplier = 1.2 if terrain_type == "rocky" else 1.0
    
    # Final distance calculation with adjustments
    raw_distance = sum(distances)
    adjusted_distance = raw_distance * (1.0 if raw_distance < 10 else 0.9)
    
    # Apply the weather and terrain factors to the parts that matter
    actual_distance = adjusted_distance * (difficulty_multiplier if raw_distance > 15 else 1.0)
    
    return actual_distance

# Calculate the hiking trail distance
actual_distance = calculate_route()
print(f"Result: {actual_distance}")