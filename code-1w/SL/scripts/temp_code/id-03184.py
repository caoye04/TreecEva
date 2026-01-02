def calculate_harvest_potential(climate_data):
    base_yield = 0
    temperature_factor = 1.0
    rainfall_factor = 1.0
    sunlight_hours = 0
    stress_days = 0
    cumulative_rainfall = 0
    
    # Process daily climate records
    for day_data in climate_data:
        temp = day_data['temp']
        rain = day_data['rainfall']
        sun = day_data['sunlight']
        
        # Track total sunlight (distractor: not directly used in final formula)
        sunlight_hours += sun
        
        # Irrelevant stress tracking (partially used, but mostly distraction)
        if temp > 35 or temp < 10:
            stress_days += 1

        # Cumulative rainfall for drought detection (semi-relevant)
        cumulative_rainfall += rain
        
        # Temperature adjustment logic
        if 20 <= temp <= 30:
            temperature_factor *= 1.05
        elif temp > 35:
            temperature_factor *= 0.85
        else:
            temperature_factor *= 0.95

        # Rainfall impact with diminishing returns
        if 5 < rain < 20:
            rainfall_factor *= 1.1
        elif rain > 25:
            rainfall_factor *= 0.8  # Waterlogging penalty
        
    
    # Secondary computation: drought assessment (mostly irrelevant)
    drought_severity = 0
    if cumulative_rainfall < 100:
        drought_severity = (100 - cumulative_rainfall) / 100
    
    # Simulate soil nutrient decay over time (red herring)
    nutrient_level = 100.0
    for _ in range(30):
        nutrient_level *= 0.99  # Gradual decay, never used later
    
    # String-based condition classification (uses string method, semi-relevant)
    condition_flag = f"T{temperature_factor:.2f}_R{rainfall_factor:.2f}"
    if "85" in condition_flag:
        base_yield -= 5
    
    # Main yield calculation with compounded factors
    base_yield += 50
    base_yield *= temperature_factor
    base_yield *= rainfall_factor
    
    # Final adjustment based on empirical threshold
    if base_yield > 60 and stress_days < 5:
        base_yield += 10
    
    # Normalize using length of data (important correction)
    final_yield = base_yield / len(climate_data) * 30
    
    return final_yield

# Simulated 15-day climate dataset
climate_data = [
    {'temp': 25, 'rainfall': 12, 'sunlight': 7},
    {'temp': 28, 'rainfall': 8,  'sunlight': 8},
    {'temp': 32, 'rainfall': 3,  'sunlight': 9},
    {'temp': 36, 'rainfall': 0,  'sunlight': 10},
    {'temp': 24, 'rainfall': 15, 'sunlight': 6},
    {'temp': 21, 'rainfall': 18, 'sunlight': 5},
    {'temp': 19, 'rainfall': 22, 'sunlight': 4},
    {'temp': 33, 'rainfall': 5,  'sunlight': 8},
    {'temp': 29, 'rainfall': 2,  'sunlight': 9},
    {'temp': 26, 'rainfall': 7,  'sunlight': 7},
    {'temp': 23, 'rainfall': 14, 'sunlight': 5},
    {'temp': 37, 'rainfall': 0,  'sunlight': 10},
    {'temp': 27, 'rainfall': 9,  'sunlight': 6},
    {'temp': 25, 'rainfall': 6,  'sunlight': 8},
    {'temp': 22, 'rainfall': 20, 'sunlight': 5}
]

final_yield = calculate_harvest_potential(climate_data)
print(f"Result: {final_yield}")