def analyze_structural_loads(load_profile, material_yield_strength):
    tolerance = 0.001 * material_yield_strength
    cumulative_moment = 0
    total_load = sum(load_profile)
    peak_load = max(load_profile)
    normalized_stress = [load / material_yield_strength for load in load_profile]
    
    # Track potential equilibrium points
    equilibrium_candidates = []
    temp_buffer = []
    
    for i, load in enumerate(load_profile):
        left_segment = load_profile[:i]
        right_segment = load_profile[i+1:]
        
        left_moment = sum([val * (i - idx) for idx, val in enumerate(left_segment)])
        right_moment = sum([val * (idx + 1) for idx, val in enumerate(right_segment)])
        
        net_force = abs(left_moment - right_moment)
        stress_gradient = 0
        if i > 0 and i < len(normalized_stress):
            stress_gradient = abs(normalized_stress[i] - normalized_stress[i-1])
        
        dummy_calc = (left_moment + right_moment) % 7  # Irrelevant but distracting
        
        pivot_point = i
        equilibrium_index = pivot_point if net_force < tolerance else -1
        
        if equilibrium_index != -1:
            equilibrium_candidates.append(equilibrium_index)
            temp_buffer.append((i, net_force))
    
    # Secondary validation pass (not affecting main result)
    valid_peaks = []
    for idx, val in enumerate(load_profile):
        if val == peak_load:
            valid_peaks.append(idx)
    
    # Final decision based on first pass
    if len(equilibrium_candidates) > 0:
        equilibrium_index = equilibrium_candidates[0]
    else:
        equilibrium_index = -1
    
    # Extra unused computations to increase cognitive load
    avg_stress = sum(normalized_stress) / len(normalized_stress)
    moment_variance = sum((x - avg_stress) ** 2 for x in normalized_stress)
    
    return equilibrium_index

# Input data
efficiency_ratings = [120, 240, 360, 240, 120]
limit_strength = 1200

# Execute function
result = analyze_structural_loads(efficiency_ratings, limit_strength)
print(f"Result: {result}")