def analyze_growth_factors(temperature, rainfall):
    # Irrelevant metric for leaf surface area (distractor)
    leaf_area_index = (temperature * 0.3) + (rainfall * 0.05)
    
    # Core growth factor calculation
    temp_factor = 1.0 if 15 <= temperature <= 30 else 0.3
    rain_factor = min(rainfall / 200, 1.0) if rainfall > 50 else 0.4
    
    return temp_factor * rain_factor

# Simulate soil nutrient decay over time (partially relevant)
def compute_nutrient_score(base_nutrients, days):
    decay_rate = 0.01
    adjusted_nutrients = base_nutrients * (0.9 ** (days * decay_rate))
    
    # Dummy transformation (distractor)
    transformed_score = adjusted_nutrients ** 0.5 if adjusted_nutrients > 5 else adjusted_nutrients
    return min(transformed_score, 10)

# Main yield estimation function
def calculate_harvest_potential(climate_data):
    base_yield_per_plot = 120
    total_plots = 8
    cumulative_yield = 0
    
    # Tracking auxiliary statistic (not used in final result)
    peak_growth_factor = 0
    
    for entry in climate_data:
        temp = entry['temp']
        rain = entry['rainfall']
        days_elapsed = entry['days']
        soil_nutrients = entry['nutrients']
        
        # Compute growth efficiency using temperature and rainfall
        growth_efficiency = analyze_growth_factors(temp, rain)
        
        # Update peak tracker (distractor variable)
        if growth_efficiency > peak_growth_factor:
            peak_growth_factor = growth_efficiency
        
        # Nutrient contribution (only the score matters)
        nutrient_potency = compute_nutrient_score(soil_nutrients, days_elapsed)
        nutrient_factor = nutrient_potency / 10.0
        
        # Conditional yield boost based on optimal conditions
        bonus_multiplier = 1.25 if temp > 20 and rain > 100 and nutrient_potency > 7 else 1.0
        
        # Calculate plot-specific output
        expected_output = base_yield_per_plot * growth_efficiency * nutrient_factor * bonus_multiplier
        
        # Apply conditional adjustment using Python's conditional expression
        expected_output = expected_output * 0.9 if days_elapsed > 60 else expected_output * 1.1
        
        cumulative_yield += expected_output
    
    # Final aggregation across all plots
    total_estimated_yield = cumulative_yield * total_plots / len(climate_data)
    
    # Distractor computation: average_peak (unused)
    scaling_offset = peak_growth_factor * 0.1
    final_yield = int(total_estimated_yield - scaling_offset * 5)  # Rounded to nearest integer
    
    return final_yield

# Input dataset representing weekly measurements over growing season
climate_data = [
    {'temp': 22, 'rainfall': 150, 'days': 14, 'nutrients': 8.5},
    {'temp': 25, 'rainfall': 180, 'days': 28, 'nutrients': 7.2},
    {'temp': 18, 'rainfall': 200, 'days': 42, 'nutrients': 6.0},
    {'temp': 26, 'rainfall': 90,  'days': 56, 'nutrients': 9.1},
    {'temp': 31, 'rainfall': 120, 'days': 70, 'nutrients': 5.5}
]

# Execute main logic
final_yield = calculate_harvest_potential(climate_data)
print(f"Result: {final_yield}")