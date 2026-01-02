def analyze_growth_factors(temperature, rainfall):
    # Irrelevant metric for leaf density (not used in final calculation)
    leaf_density_index = (temperature * 0.6) + (rainfall * 0.4)
    
    # Relevant growth window calculation
    if temperature > 15 and rainfall > 300:
        growing_days = 180
    elif temperature > 10 and rainfall > 200:
        growing_days = 120
    else:
        growing_days = 60
        
    return growing_days

# Simulate seasonal nutrient depletion (semi-relevant, only one output used)
def compute_nutrient_depletion(soil_type, ph_level):
    base_loss = 0.1 if soil_type == 'clay' else 0.2
    ph_adjustment = 0.05 if 6.0 <= ph_level <= 7.0 else 0.15
    total_depletion = base_loss + ph_adjustment
    recovery_rate = 1.2 if ph_level > 7.0 else 0.8  # Unused variable (distractor)
    return total_depletion

# Main yield model
def calculate_harvest_potential(climate_data, soil_health):
    temp = climate_data['avg_temp']
    rain = climate_data['annual_rainfall']
    
    # Extract irrelevant features (distractors)
    wind_speed = climate_data.get('wind_speed', 0)  # Not used
    humidity = climate_data.get('humidity', 50)      # Not used
    
    # Compute intermediate values
    growing_period = analyze_growth_factors(temp, rain)
    depletion_rate = compute_nutrient_depletion(soil_health['type'], soil_health['ph'])
    
    # Base productivity index
    base_yield_per_day = 10 if soil_health['fertility'] == 'high' else 6
    
    # Apply conditional boost based on optimal conditions (conditional expression)
    efficiency_factor = 1.5 if (temp >= 20 and rain >= 400) else 1.0
    
    # Simulated pest pressure reducing effective days (dead code path - never triggers without extreme heat)
    effective_days = growing_period
    if temp > 35:
        effective_days = int(growing_period * 0.7)  # Not triggered in this case

    # Destructuring assignment for crop coefficients (tuple unpacking)
    (coef_a, coef_b) = (1.2, 0.8) if soil_health['drainage'] == 'good' else (1.0, 1.0)
    
    # Core calculation
    potential_output = (base_yield_per_day * growing_period * efficiency_factor)
    
    # Apply nutrient loss over time
    net_yield = potential_output * (1 - depletion_rate)
    
    # Final adjustment using string-based rule (simulating config lookup)
    adjustment_key = "optimal" if net_yield > 1000 else "standard"
    adjustments = {"standard": 0.9, "optimal": 1.1}
    adjusted_yield = net_yield * adjustments[adjustment_key]
    
    # Final result
    final_yield = int(adjusted_yield)
    
    # Print required output
    print(f"Result: {final_yield}")
    
    return final_yield

# Input data setup
climate_conditions = {
    'avg_temp': 22,
    'annual_rainfall': 420,
    'wind_speed': 12,
    'humidity': 65
}

soil_profile = {
    'type': 'loam',
    'ph': 6.5,
    'fertility': 'high',
    'drainage': 'good'
}

# Execute
final_yield = calculate_harvest_potential(climate_conditions, soil_profile)