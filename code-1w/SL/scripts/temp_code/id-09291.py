def analyze_growth_factors(temperature, humidity):
    # Irrelevant analysis with no impact on final result
    stress_index = (temperature - 25) * (100 - humidity) / 10
    optimal_threshold = 4.5 if temperature > 30 else 3.2
    return stress_index < optimal_threshold

# Simulate environmental sensor data
temperature_readings = [22, 25, 27, 30, 33]
humidity_levels = [60, 65, 70, 55, 50]

# Misleading aggregation that isn't used later
avg_temp = sum(temperature_readings) / len(temperature_readings)
avg_humidity = sum(humidity_levels) / len(humidity_levels)

def process_soil_composition(texture, ph_level):
    # Complex but ultimately unused function
    base_score = 100 - abs(ph_level - 6.5) * 10
    adjustment = 0
    if 'clay' in texture:
        adjustment -= 15
    elif 'sandy' in texture:
        adjustment += 10
    return max(0, base_score + adjustment)

soil_profile = {'texture': 'loamy clay', 'ph': 6.8, 'nitrogen': 42}

# Distractor: Unused transformation
soil_status = 'optimal' if soil_profile['ph'] > 6 and soil_profile['nitrogen'] > 30 else 'marginal'

climate_data = list(zip(temperature_readings, humidity_levels))
soil_health = soil_profile['nitrogen']

# Key computation with embedded logic chain
def calculate_harvest_potential(weather, nutrients):
    yield_base = 0
    bonus_factor = 1.0
    
    # Relevant nested loop processing climate data
    for temp, hum in weather:
        if temp >= 25 and temp <= 30:
            yield_base += 8
            # Conditional expression usage
            bonus_factor *= 1.1 if hum > 60 else 1.0
        elif temp < 25:
            yield_base += 4
        else:
            yield_base += 2
    
    # Lambda-based nutrient efficiency
    efficiency_curve = lambda x: 0.8 + 0.4 * (x / 100)
    effective_nutrients = nutrients * efficiency_curve(nutrients)
    
    # String method distraction
    profile_str = str(soil_profile)
    contains_nitrogen = 'nitrogen' in profile_str.lower()
    
    # Core calculation using multiple concepts
    preliminary_yield = yield_base * bonus_factor
    
    # Final adjustment using boolean logic and comparison
    stress_penalty = 0
    high_temp_events = len([t for t, h in weather if t > 32])
    if high_temp_events > 1 and nutrients < 50:
        stress_penalty = 12
    
    final_yield = int(preliminary_yield - stress_penalty + effective_nutrients // 10)
    
    # Dead code path (not executed due to logic)
    if False:
        fallback = process_soil_composition(soil_profile['texture'], soil_profile['ph'])
        final_yield = max(final_yield, fallback)
    
    return final_yield

# Execution point of interest
final_yield = calculate_harvest_potential(climate_data, soil_health)
print(f"Result: {final_yield}")