def calculate_harvest_potential(climate_data):
    base_yield = 100
    temperature_factor = 1.0
    rainfall_factor = 1.0
    sunlight_factor = 1.0
    stress_count = 0
    ideal_days = 0

    # Irrelevant tracking variables (distractors)
    cumulative_windspeed = 0
    outlier_events = []
    daily_fluctuations = [abs(day['temp_max'] - day['temp_min']) for day in climate_data]

    for day in climate_data:
        temp = day['temp_avg']
        rain = day['rainfall']
        sun = day['sunlight']

        # Cumulative wind (not used in final calculation)
        cumulative_windspeed += day.get('windspeed', 0)

        # Detect outliers (dead code path)
        if day['temp_max'] > 40 or day['temp_min'] < -10:
            outlier_events.append(True)

        # Real logic: temperature impact
        if 20 <= temp <= 30:
            temperature_factor *= 1.05
            ideal_days += 1
        else:
            stress_count += 1

        # Rainfall logic with short-circuiting
        if rain > 5 and sun > 6:
            rainfall_factor *= 0.9  # Waterlogging risk
        elif rain < 2:
            rainfall_factor *= 0.85  # Drought stress
        else:
            rainfall_factor *= 1.1  # Optimal moisture

        # Sunlight with conditional expression
        sunlight_factor *= 1.08 if sun > 7 else (0.95 if sun < 4 else 1.0)

    # Secondary distraction: analyze fluctuation trend (unused)
    avg_fluctuation = sum(daily_fluctuations) / len(daily_fluctuations)
    high_variance_days = [f for f in daily_fluctuations if f > 10]

    # Core yield formula (depends only on temp, rain, sun factors)
    adjusted_yield = base_yield * temperature_factor * rainfall_factor * sunlight_factor
    
    # Apply stress penalty
    if stress_count > 5:
        adjusted_yield *= 0.7
    
    # Final adjustment based on ideal days (only matters if > 10)
    final_yield = int(adjusted_yield + (ideal_days * 2)) if ideal_days > 10 else int(adjusted_yield)
    
    return final_yield

# Simulated 15-day climate data
climate_data = [
    {'temp_avg': 25, 'temp_max': 28, 'temp_min': 22, 'rainfall': 3, 'sunlight': 8, 'windspeed': 12},
    {'temp_avg': 27, 'temp_max': 31, 'temp_min': 23, 'rainfall': 1, 'sunlight': 9, 'windspeed': 10},
    {'temp_avg': 23, 'temp_max': 26, 'temp_min': 20, 'rainfall': 12, 'sunlight': 5, 'windspeed': 15},
    {'temp_avg': 28, 'temp_max': 33, 'temp_min': 24, 'rainfall': 0, 'sunlight': 7, 'windspeed': 8},
    {'temp_avg': 26, 'temp_max': 29, 'temp_min': 23, 'rainfall': 4, 'sunlight': 6, 'windspeed': 9},
    {'temp_avg': 24, 'temp_max': 27, 'temp_min': 21, 'rainfall': 3, 'sunlight': 4, 'windspeed': 11},
    {'temp_avg': 29, 'temp_max': 34, 'temp_min': 25, 'rainfall': 2, 'sunlight': 8, 'windspeed': 7},
    {'temp_avg': 22, 'temp_max': 25, 'temp_min': 19, 'rainfall': 6, 'sunlight': 3, 'windspeed': 13},
    {'temp_avg': 31, 'temp_max': 36, 'temp_min': 27, 'rainfall': 1, 'sunlight': 9, 'windspeed': 6},
    {'temp_avg': 20, 'temp_max': 24, 'temp_min': 16, 'rainfall': 5, 'sunlight': 7, 'windspeed': 10},
    {'temp_avg': 18, 'temp_max': 22, 'temp_min': 14, 'rainfall': 4, 'sunlight': 5, 'windspeed': 14},
    {'temp_avg': 33, 'temp_max': 38, 'temp_min': 29, 'rainfall': 0, 'sunlight': 10, 'windspeed': 5},
    {'temp_avg': 27, 'temp_max': 30, 'temp_min': 24, 'rainfall': 3, 'sunlight': 6, 'windspeed': 8},
    {'temp_avg': 25, 'temp_max': 28, 'temp_min': 22, 'rainfall': 7, 'sunlight': 4, 'windspeed': 12},
    {'temp_avg': 26, 'temp_max': 29, 'temp_min': 23, 'rainfall': 2, 'sunlight': 5, 'windspeed': 9}
]

# Execute
final_yield = calculate_harvest_potential(climate_data)
print(f"Result: {final_yield}")