def analyze_growth_potential(temperature, humidity):
    if temperature < 20 or humidity < 30:
        return 0.0
    growth_factor = (temperature - 18) * (humidity / 100)
    adjustment = 1.2 if humidity > 60 else 0.9
    return growth_factor * adjustment

def calculate_nutrient_score(ph_level, nitrogen_content):
    score = 0
    if 6.0 <= ph_level <= 7.0:
        score += 50
    elif ph_level < 6.0:
        score -= 20
    else:
        score += 10
    
    if nitrogen_content > 80:
        score += 30
    elif nitrogen_content > 50:
        score += 15
    
    # Distractor: irrelevant nutrient calculations
    potassium_bonus = 5 if nitrogen_content > 70 else 0
    magnesium_penalty = -3 if ph_level > 7.5 else 0
    score += potassium_bonus + magnesium_penalty
    
    return max(score, 0)

def calculate_harvest(soil, water):
    base_yield = 0
    stress_factor = 0
    
    for day in range(1, 8):  # 7-day simulation
        daily_rain = water[day % len(water)]
        if daily_rain > 15:
            stress_factor += 0.3
        elif daily_rain < 5:
            stress_factor += 0.5
            
        # Simulate fluctuating micro-climate
        micro_temp = (22 + (day % 5)) * (1 + 0.1 * (day % 3))
        temp_effect = 1.1 if 20 <= micro_temp <= 25 else 0.8
        base_yield += 12 * temp_effect
    
    nutrient_score = calculate_nutrient_score(soil['ph'], soil['nitrogen'])
    growth_potential = analyze_growth_potential(23, 65)
    
    # Secondary distractor variables
    unused_buffer = [micro_temp, stress_factor, temp_effect]
    phantom_yield = base_yield * 0.1
    
    efficiency_ratio = nutrient_score / 100.0
    adjusted_yield = base_yield * efficiency_ratio * (1 - min(stress_factor / 10, 0.4))
    
    # Final conditional logic with tuple unpacking
    modifiers = (1.1, 0.95) if efficiency_ratio > 0.7 else (0.9, 0.85)
    bonus_multiplier, penalty_reduction = modifiers
    
    final_yield = int(adjusted_yield * bonus_multiplier)
    
    # Early termination check (not triggered)
    if final_yield < 0:
        return 0
        
    return final_yield

# Main execution
soil_quality = {'ph': 6.8, 'nitrogen': 85}
water_levels = [12, 4, 8, 18, 6, 3, 9, 11]

interim_analysis = analyze_growth_potential(25, 70)
nutrient_diagnostic = calculate_nutrient_score(6.8, 85)

final_yield = calculate_harvest(soil_quality, water_levels)
print(f"Result: {final_yield}")