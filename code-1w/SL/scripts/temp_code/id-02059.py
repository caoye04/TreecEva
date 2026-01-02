def calculate_crop_yield(weather_conditions, soil_quality):
    base_yield = 100
    adjusted_yields = []
    
    for i, condition in enumerate(weather_conditions):
        growth_factor = 1.0
        if condition == 'sunny':
            growth_factor += 0.5
        elif condition == 'cloudy':
            growth_factor += 0.2
        else:
            growth_factor -= 0.3
            
        # Apply soil bonus using zip with indexed quality
        for j, bonus in enumerate(soil_quality):
            if i == j:
                growth_factor += bonus / 10.0

        adjusted_yield = base_yield * growth_factor
        adjusted_yields.append(adjusted_yield)
    
    # Irrelevant tracking variable (minor distraction)
    max_yield = max(adjusted_yields)
    total_harvest = sum(adjusted_yields)
    return total_harvest

# Simulation data
weather = ['sunny', 'cloudy', 'rainy', 'sunny']
soil_enhancements = [3, 1, 4, 2]

result = calculate_crop_yield(weather, soil_enhancements)
total_harvest = result
print(f"Result: {total_harvest}")