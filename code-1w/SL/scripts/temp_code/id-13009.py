def analyze_growth_potential(temperature, rainfall):
    if temperature < 15 or rainfall < 200:
        return 0
    elif temperature > 35 or rainfall > 800:
        return 0
    else:
        return (temperature * 0.7) + (rainfall * 0.01)

soil_profiles = [
    {'type': 'clay', 'ph': 6.5, 'nutrients': 0.8},
    {'type': 'loam', 'ph': 6.8, 'nutrients': 0.9},
    {'type': 'sandy', 'ph': 5.5, 'nutrients': 0.4}
]

decision_matrix = {}
for i, profile in enumerate(soil_profiles):
    key = profile['type']
    suitability = 1 if 6.0 <= profile['ph'] <= 7.0 else 0
    decision_matrix[key] = suitability

climate_data = [
    {'temp': 22, 'rain': 300},
    {'temp': 25, 'rain': 700},
    {'temp': 38, 'rain': 500}
]

baseline_scores = []
for data in climate_data:
    score = analyze_growth_potential(data['temp'], data['rain'])
    baseline_scores.append(score)

aggregate_score = sum(baseline_scores) / len(baseline_scores) if baseline_scores else 0

# Irrelevant computation: simulating evaporation rates
evaporation_rates = [0.1 * temp for temp in [d['temp'] for d in climate_data]]
total_evap = sum(evaporation_rates)
adjusted_evap = total_evap * 0.85  # unused adjustment

# Distractor: mock sensor validation
valid_sensors = [True, True, False]
sensor_coverage = sum([1 for s in valid_sensors if s]) / len(valid_sensors)

# Core logic with dictionary and conditional expression
yield_multipliers = {}
for profile in soil_profiles:
    base_mult = profile['nutrients']
    ph_bonus = 1.2 if 6.5 <= profile['ph'] <= 7.2 else 1.0
    yield_multipliers[profile['type']] = base_mult * ph_bonus

# Complex mixed reasoning
def calculate_optimal_yield(climate_list, soils):
    total_yield = 0
    count = 0
    for climate in climate_list:
        growth_base = analyze_growth_potential(climate['temp'], climate['rain'])
        if growth_base <= 0:
            continue
        for soil in soils:
            soil_type = soil['type']
            # Conditional expression used here
            multiplier = yield_multipliers[soil_type] if soil_type in yield_multipliers else 0.5
            # Simulate interaction effect
            interaction = growth_base * multiplier
            # Artificial cap
            capped = min(interaction, 25)
            total_yield += capped
            count += 1
    average_yield = total_yield / count if count else 0
    
    # Secondary adjustment based on climate stability
    temps = [c['temp'] for c in climate_list]
    rainfalls = [c['rain'] for c in climate_list]
    temp_variance = max(temps) - min(temps)
    rain_variance = max(rainfalls) - min(rainfalls)
    
    # Stability penalty (not heavily impactful but adds distraction)
    stability_penalty = 0
    if temp_variance > 15:
        stability_penalty += 2
    if rain_variance > 400:
        stability_penalty += 3
    
    # Final adjustment
    adjusted_average = average_yield - stability_penalty
    final_value = max(adjusted_average, 0)  # ensure non-negative
    
    # Dead code: logging hypothetical irrigation needs
    irrigation_needed = []
    for rf in rainfalls:
        if rf < 300:
            irrigation_needed.append(True)
        else:
            irrigation_needed.append(False)
    # This list is never used
    
    return final_value

# Key execution point
final_yield = calculate_optimal_yield(climate_data, soil_profiles)

# Print result as required
print(f"Result: {final_yield}")