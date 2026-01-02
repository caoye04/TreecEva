def analyze_growth_factors(temperature, rainfall):
    if temperature < 15:
        return 0.3
    elif temperature > 30:
        stress_factor = 0.6 if rainfall < 50 else 0.8
        return stress_factor
    else:
        return 1.0

# Simulate agricultural yield prediction based on environmental factors
def calculate_harvest_potential(climate_data, soil_quality):
    base_yield_per_hectare = 4500
    total_rainfall = sum(climate_data['rainfall'])
    avg_temp = sum(climate_data['temps']) / len(climate_data['temps'])
    
    # Irrelevant intermediate calculation (distractor)
    peak_rain_day = max(climate_data['rainfall']) if climate_data['rainfall'] else 0
    temp_buckets = {"cold": 0, "moderate": 0, "hot": 0}
    for t in climate_data['temps']:
        if t < 15:
            temp_buckets["cold"] += 1
        elif t <= 30:
            temp_buckets["moderate"] += 1
        else:
            temp_buckets["hot"] += 1
    
    # Primary growth factor computation
    growth_modifier = analyze_growth_factors(avg_temp, total_rainfall)
    
    # Soil quality adjustment with conditional expression
    soil_boost = 1.2 if soil_quality in ('rich', 'fertile') else (0.8 if soil_quality == 'poor' else 1.0)
    
    # Auxiliary irrelevant statistic
    consecutive_dry_days = 0
    max_dry_streak = 0
    for r in climate_data['rainfall']:
        if r < 5:
            consecutive_dry_days += 1
            max_dry_streak = max(max_dry_streak, consecutive_dry_days)
        else:
            consecutive_dry_days = 0
    
    # Final yield calculation (key statement)
    potential_loss = 0.1 * (temp_buckets["hot"] / len(climate_data['temps'])) if avg_temp > 25 else 0
    final_yield = base_yield_per_hectare * growth_modifier * soil_boost * (1 - potential_loss)
    
    # Dead code path (distractor)
    if False:
        final_yield *= 1.1  # Never executed
    
    return final_yield

# Input data
climate_data = {
    'temps': [18, 22, 26, 31, 29, 24, 19],
    'rainfall': [12, 8, 3, 0, 5, 15, 10]
}
soil_quality = 'fertile'

# Execute and print result
final_yield = calculate_harvest_potential(climate_data, soil_quality)
print(f"Result: {final_yield}")