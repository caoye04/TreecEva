def analyze_soil_composition(samples):
    base_nutrients = [s['nitrogen'] * 0.3 + s['phosphorus'] * 0.2 + s['potassium'] * 0.5 for s in samples]
    adjusted_levels = []
    for level in base_nutrients:
        if level < 20:
            adjusted_levels.append(level * 1.8)
        elif level > 50:
            adjusted_levels.append(level * 0.9)
        else:
            adjusted_levels.append(level)
    avg_adjusted = sum(adjusted_levels) / len(adjusted_levels)
    return avg_adjusted


def assess_rainfall_pattern(daily_rain):
    wet_days = [r for r in daily_rain if r >= 5]
    dry_streaks = 0
    current_streak = 0
    for rain in daily_rain:
        if rain < 2:
            current_streak += 1
        else:
            if current_streak >= 7:
                dry_streaks += 1
            current_streak = 0
    if current_streak >= 7:
        dry_streaks += 1
    total_rain = sum(daily_rain)
    effective_rain = total_rain * (1 - dry_streaks * 0.05)
    return max(effective_rain, 0)


def calculate_harvest_potential(regions):
    cumulative_score = 0
    penalty_factor = 0
    
    for region in regions:
        soil_quality = analyze_soil_composition(region['soil_samples'])
        rainfall_effectiveness = assess_rainfall_pattern(region['rain_mm'])
        
        # Distractor: temperature tracking (not used in final formula)
        temps = region['temps_c']
        heat_days = len([t for t in temps if t > 35])
        cold_days = len([t for t in temps if t < 5])
        avg_temp = sum(temps) / len(temps)
        
        # Irrelevant health metric
        pest_incidence = region.get('pest_level', 0) * 0.3
        
        # Core calculation
        region_base = soil_quality * 0.6 + (rainfall_effectiveness / 10) * 0.4
        
        # Modifier based on region size
        area_multiplier = 1.0
        if region['area_km2'] > 200:
            area_multiplier = 1.1
        elif region['area_km2'] < 50:
            area_multiplier = 0.9
        
        region_yield = region_base * area_multiplier
        
        # Accumulate
        cumulative_score += region_yield
        
        # Distractor: unused state update
        if region_yield > 40:
            penalty_factor += 0.02
        
    # Final transformation
    adjustment_ratio = 0.85 + (penalty_factor * 0.5)  # No real impact due to small variation
    final_yield = int(cumulative_score * adjustment_ratio)
    
    # Unused debugging trace
    debug_log = f'Final yield before truncation: {cumulative_score * adjustment_ratio}'
    redundant_copy = final_yield
    
    return final_yield

# Input data
region_data = [
    {
        'soil_samples': [
            {'nitrogen': 25, 'phosphorus': 15, 'potassium': 40},
            {'nitrogen': 30, 'phosphorus': 20, 'potassium': 35}
        ],
        'rain_mm': [3, 7, 12, 0, 0, 4, 2, 1, 0, 8, 15, 20, 2, 0],
        'temps_c': [18, 22, 25, 28, 33, 36, 38, 37, 32, 28, 24, 20, 17, 15],
        'area_km2': 120,
        'pest_level': 10
    },
    {
        'soil_samples': [
            {'nitrogen': 40, 'phosphorus': 30, 'potassium': 50},
            {'nitrogen': 35, 'phosphorus': 25, 'potassium': 45}
        ],
        'rain_mm': [0, 0, 0, 0, 0, 0, 0, 12, 18, 5, 0, 0, 0, 2],
        'temps_c': [20, 23, 26, 29, 31, 34, 37, 39, 38, 35, 30, 25, 22, 19],
        'area_km2': 300,
        'pest_level': 5
    },
    {
        'soil_samples': [
            {'nitrogen': 20, 'phosphorus': 10, 'potassium': 30},
            {'nitrogen': 18, 'phosphorus': 12, 'potassium': 28}
        ],
        'rain_mm': [5, 8, 10, 12, 0, 0, 3, 7, 9, 11, 14, 0, 0, 0],
        'temps_c': [16, 18, 20, 23, 26, 29, 32, 35, 36, 34, 30, 25, 21, 17],
        'area_km2': 80,
        'pest_level': 15
    }
]

final_yield = calculate_harvest_potential(region_data)
print(f"Target result: {final_yield}")