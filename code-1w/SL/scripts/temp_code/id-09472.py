def analyze_growth_factors(temperature, rainfall):
    # Analyze temperature and rainfall patterns for crop viability
    growth_score = 0
    stress_factor = 0

    for temp in temperature:
        if temp > 35:
            stress_factor += (temp - 35) * 0.3
        elif temp < 15:
            stress_factor += (15 - temp) * 0.2

    avg_rainfall = sum(rainfall) / len(rainfall)
    if avg_rainfall < 50:
        drought_penalty = (50 - avg_rainfall) * 0.4
    else:
        drought_penalty = 0

    base_score = 100 - stress_factor - drought_penalty
    adjusted_score = base_score * (0.8 if avg_rainfall > 120 else 1.0)
    return max(adjusted_score, 10)


def calculate_nutrient_index(nutrients):
    # Calculate nutrient balance score (distractor function - not used in final result)
    weights = {'nitrogen': 0.4, 'phosphorus': 0.3, 'potassium': 0.3}
    score = sum(nutrients[elem] * weights[elem] for elem in nutrients)
    return score * 0.5


def calculate_harvest_potential(climate_data, soil_quality):
    # Core logic with mixed concepts and distractions
    temperature, rainfall = climate_data
    
    # Irrelevant data structure manipulation
    daily_logs = [{'day': i, 'temp': t, 'rain': r} for i, (t, r) in enumerate(zip(temperature, rainfall))]
    valid_days = [log for log in daily_logs if log['temp'] >= 10 and log['rain'] <= 200]
    efficiency_map = {i: min(1.0, log['temp'] / 30) for i, log in enumerate(valid_days)}

    base_yield = analyze_growth_factors(temperature, rainfall)
    
    # Complex conditional expression with misleading branches
    soil_bonus = 1.1 if all(soil_quality[key] > 6.0 for key in ['ph', 'organic']) else 0.9
    
    # Destructuring assignment (tuple unpacking)
    primary, secondary = soil_quality['texture'], soil_quality.get('drainage', 'moderate')
    texture_modifier = 1.05 if primary in ['loam', 'silt'] else 0.95
    
    # Multiple nested conditions with red herring variables
    legacy_yield_trend = [base_yield * 0.95, base_yield * 0.98, base_yield]
    predicted_improvement = False
    improvement_rate = 0.0
    if legacy_yield_trend[-1] > legacy_yield_trend[0]:
        improvement_rate = (legacy_yield_trend[-1] - legacy_yield_trend[0]) / legacy_yield_trend[0]
        if improvement_rate > 0.05:
            predicted_improvement = True

    # Final computation chain
    preliminary_yield = base_yield * soil_bonus * texture_modifier
    
    # Simulate seasonal adjustment factor using list comprehension
    seasonal_factors = [1.0 + 0.1 * (30 - t)/15 for t in temperature]
    avg_factor = sum(seasonal_factors) / len(seasonal_factors)
    
    final_yield = int(preliminary_yield * avg_factor)
    
    # Dead code path - never executed but adds distraction
    if False:
        fallback_model = calculate_nutrient_index({'nitrogen': 7, 'phosphorus': 5, 'potassium': 6})
        final_yield = int(fallback_model * 15)

    return final_yield

# Input data
climate_data = ([25, 28, 32, 27, 23], [45, 60, 55, 70, 50])
soil_quality = {
    'ph': 6.8,
    'organic': 7.2,
    'texture': 'loam',
    'drainage': 'good'
}

# Execution
final_yield = calculate_harvest_potential(climate_data, soil_quality)
print(f"Result: {final_yield}")