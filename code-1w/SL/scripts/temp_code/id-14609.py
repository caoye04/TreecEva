def analyze_growth_potential(temperature, rainfall):
    # Irrelevant helper function (dead code path)
    return sum(temperature) / len(temperature) if temperature else 0

soil_conditions = [0.8, 0.9, 0.75, 0.88, 0.65]
climate_data = [23, 18, 25, 20, 22]  # Daily average temps in Celsius
precipitation_log = [12, 5, 18, 0, 22]  # mm of rain per day (distractor)

# Misleading intermediate calculations
temp_bias_correction = [t - 20 for t in climate_data]
rainfall_weighted_score = sum([r ** 0.5 for r in precipitation_log if r > 0])

# Core logic with moderate nesting and list comprehension
def calculate_harvest_efficiency(temps, soils):
    base_yield = 0
    adjustment_factor = 0.0
    
    for i, temp in enumerate(temps):
        # Conditional expression + zip usage
        moisture_level = next((p for d, p in zip(climate_data, precipitation_log) if d == temp), 0)
        ideal_temp_range = 18 <= temp <= 24
        sufficient_moisture = moisture_level > 10
        
        # Complex conditional expression with nested conditions
        growth_boost = 1.2 if ideal_temp_range and sufficient_moisture else (0.8 if not ideal_temp_range else 1.0)
        
        # Destructuring assignment (tuple unpacking)
        current_soil, next_soil = (soils[i], soils[i+1] if i+1 < len(soils) else soils[-1])
        
        # Relevant computation chain
        adjusted_soil = (current_soil + next_soil) * 0.5
        daily_yield = (temp / 10) * adjusted_soil * growth_boost
        
        # State tracking with interference from irrelevant modifier
        weather_risk = 0.1 if temp > 23 else 0.05
        base_yield += daily_yield * (1 - weather_risk)
        
        # Accumulate adjustment factor (semi-relevant)
        adjustment_factor += growth_boost if sufficient_moisture else 0
    
    # Final calculation using list comprehension (core answer)
    efficiency_multiplier = sum([s**2 for s in soils]) / len(soils)
    final_output = base_yield * efficiency_multiplier
    
    # Red herring: unused complex structure
    detailed_analysis = {
        'peak_temp': max(temps),
        'avg_rainfall': sum(precipitation_log)/len(precipitation_log),
        'growth_credits': adjustment_factor
    }
    
    return round(final_output, 4)

# Unused variable (distractor)
optimal_rotation_cycle = [3, 7, 4]

# Key execution point
final_yield = calculate_harvest_efficiency(climate_data, soil_conditions)

print(f"Result: {final_yield}")