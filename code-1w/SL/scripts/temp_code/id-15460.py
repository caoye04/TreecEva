def calculate_reservoir_capacity():
    base_levels = [320, 450, 670, 890, 1200]
    operational_factors = [0.9, 1.1, 0.95, 1.0, 0.85]
    
    # Apply environmental adjustment factors using zip
    adjusted_levels = []
    for level, factor in zip(base_levels, operational_factors):
        adjusted_levels.append(int(level * factor))
    
    # Minor irrelevant computation (distractor at intervention level 5)
    avg_level = sum(base_levels) // len(base_levels)
    peak_index = base_levels.index(max(base_levels))
    
    total_capacity = sum(adjusted_levels)
    
    # Additional unrelated but harmless variable
    status_flags = {i: 'normal' if x > 500 else 'low' for i, x in enumerate(adjusted_levels)}
    
    print(f"Result: {total_capacity}")

calculate_reservoir_capacity()