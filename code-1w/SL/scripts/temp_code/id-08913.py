def calculate_grid_efficiency():
    # Simulate renewable energy grid outputs (in MW)
    solar_grids = [12, 15, 10, 18, 20]
    wind_grids = [14, 11, 17, 13, 19]
    
    # Irrelevant distractor: unused variable
    hydro_backup = [8, 9, 7, 10, 8]
    
    # Pair corresponding solar and wind outputs
    paired_outputs = zip(solar_grids, wind_grids)
    
    # Calculate efficiency ratio for each pair and filter high-efficiency grids
    efficient_pairs = []
    for s, w in paired_outputs:
        avg_output = (s + w) / 2
        if avg_output > 13:
            efficient_pairs.append((s, w))
    
    # Compute optimized capacity as harmonic mean of efficient pairs
    optimized_grids = []
    for s, w in efficient_pairs:
        if s > 0 and w > 0:
            harmonic_mean = 2 * (s * w) / (s + w)
            optimized_grids.append(round(harmonic_mean, 2))
    
    # Key assignment point
    total_capacity = sum(optimized_grids)
    
    # Print result for clarity
    print(f"Result: {total_capacity}")
    
    return total_capacity

# Execute function
calculate_grid_efficiency()