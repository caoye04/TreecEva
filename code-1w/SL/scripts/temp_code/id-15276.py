def calculate_thermal_load(points):
    total_load = 0
    temp_cache = set()
    outlier_threshold = 75
    scaling_factor = 1.8
    adjustment = 0.2

    for pt in points:
        x, y = pt
        if x < 0 or y < 0:
            continue
        
        # Irrelevant geometric calculation (distractor)
        euclidean_norm = (x**2 + y**2) ** 0.5
        if euclidean_norm > outlier_threshold:
            temp_cache.add((x, y))
            continue

        # Core logic: heat contribution based on position
        local_heat = (x + y) * scaling_factor
        
        # Conditional expression for dynamic damping
        damping = 0.9 if local_heat > 40 else (0.5 if local_heat > 20 else 0.3)
        stabilized_heat = local_heat * damping
        
        total_load += stabilized_heat

    # Secondary pass using set difference (semi-relevant)
    all_points = set(points)
    valid_points = all_points - temp_cache
    efficiency_ratio = len(valid_points) / len(all_points) if all_points else 0

    # Final adjustment with conditional expression
    final_adjustment = 1.0 if efficiency_ratio > 0.7 else 0.85
    total_load *= final_adjustment

    return int(total_load)

# Simulated sensor grid coordinates
grid_points = [(3, 5), (7, 2), (-1, 4), (6, 8), (0, 0), (9, 1), (4, 4)]

# Misleading pre-processing steps (dead computation)
duplicate_filtered = [p for p in grid_points if p[0] != p[1]]
shadow_copy = tuple(sorted(duplicate_filtered, key=lambda x: x[0]))
baseline_shift = sum(p[0] + p[1] for p in shadow_copy) // len(shadow_copy)

# Key execution point
thermal_capacity = calculate_thermal_load(grid_points)

# Output result
print(f"Result: {thermal_capacity}")