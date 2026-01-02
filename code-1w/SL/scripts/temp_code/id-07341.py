def calculate_system_efficiency(levels):
    baseline = 1.0
    peak_efficiency = 0.0
    adjustment_factor = 0.95
    temp_cache = [0] * len(levels)

    for idx, (power, heat) in enumerate(zip(levels, levels[1:])):
        load_ratio = power / (heat + 1)
        adjusted_ratio = load_ratio * adjustment_factor
        
        efficiency = lambda x, y: (x * y) ** 0.5 if x > 0 and y > 0 else 0
        current_efficiency = efficiency(power, adjusted_ratio)

        temp_cache[idx] = round(current_efficiency, 3)
        
        if current_efficiency > peak_efficiency:
            peak_efficiency = current_efficiency
        
        # Early termination on threshold
        if power > 40 and heat > 35:
            break  # Key execution point
            
    return peak_efficiency

# Input data
capacity_levels = [12, 25, 30, 45, 52]
result = calculate_system_efficiency(capacity_levels)
print(f"Result: {result}")