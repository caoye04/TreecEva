def analyze_growth_potential(temp, rainfall):
    # Irrelevant agricultural metrics (distractors)
    ph_level = 6.5
    nutrient_score = 87
    pest_risk = temp * 0.3 + rainfall * 0.1
    
    # Core logic disguised among red herrings
    if temp < 15 or rainfall < 300:
        return 0
    elif temp > 35 or rainfall > 1200:
        return 0
    else:
        return (temp - 10) * (rainfall / 100)

# Decoy function – looks related but never used
def calculate_irrigation_cost(area, duration):
    base_rate = 2.5
    surcharge = 0.7 if duration > 60 else 0
    return area * (base_rate + surcharge)

# Simulate historical yield trends – misleading data path
historical_yields = [4.2, 4.5, 4.1, 4.8, 5.0, 4.6, 4.3]
projected_decline = sum(historical_yields) / len(historical_yields) * 0.03

# Soil composition matrix – partially relevant, mostly distraction
soil_conditions = {
    'ph': 6.8,
    'nitrogen': 220,
    'organic_matter': 3.4,
    'compaction_index': 1.3,
    'drainage_class': 'well-drained'
}

# Climate data with multiple irrelevant fields
climate_data = {
    'temperature_avg': 26,
    'rainfall_annual': 850,
    'humidity': 68,
    'wind_speed': 12.5,
    'solar_radiation': 18.4,
    'frost_days': 5
}

# Red herring: unused growth stages
growth_stages = ['germination', 'vegetative', 'flowering', 'fruiting']
stress_factors = set(['drought', 'heat', 'pests', 'lodging'])
extreme_stress = {'flood', 'frost', 'hail'}

# Conditional expression with distractor logic
is_optimal_season = 'yes' if climate_data['temperature_avg'] > 20 and climate_data['rainfall_annual'] > 700 else 'no'

# Destructuring assignment – appears important but only partially used
nitrogen, organic_matter, compaction = soil_conditions['nitrogen'], soil_conditions['organic_matter'], soil_conditions['compaction_index']

# Complex nested control flow with dead branches
adjustment_factor = 1.0
if soil_conditions['ph'] < 6.0:
    adjustment_factor *= 0.8
elif soil_conditions['ph'] > 7.5:
    adjustment_factor *= 0.7
else:
    if compaction > 1.5:
        adjustment_factor *= 0.9
    else:
        adjustment_factor *= 1.05
        # Dead branch – adjustment never used again
        adjustment_factor += 0.02

# Set operations – core relevance hidden in distraction
present_nutrients = {'nitrogen', 'phosphorus', 'potassium'}
required_nutrients = {'nitrogen', 'phosphorus', 'potassium', 'calcium', 'magnesium'}
missing_nutrients = required_nutrients - present_nutrients

# Main optimization function with recursive helper
recursive_calls = 0

def optimize_harvest(climate, soil):
    global recursive_calls
    recursive_calls += 1
    temp = climate['temperature_avg']
    rain = climate['rainfall_annual']
    
    base_yield = analyze_growth_potential(temp, rain)
    
    if base_yield == 0:
        return 0
    
    # Recursive refinement – runs once
    def refine_estimate(yld, depth=2):
        nonlocal temp, rain
        if depth <= 0:
            return yld
        # Simulated microclimate adjustment
        adjusted_yield = yld * (1 + (soil['organic_matter'] - 2.0) * 0.05)
        return refine_estimate(adjusted_yield, depth - 1)
    
    refined = refine_estimate(base_yield)
    
    # Final adjustment using conditional expression
    final_multiplier = 1.2 if 'well-drained' in climate.get('drainage_class', '') else 0.8
    
    # Critical computation step
    final_yield = refined * final_multiplier * adjustment_factor
    
    # Dead code – never executed due to logic
    if False and soil['nitrogen'] > 200:
        bonus = (soil['nitrogen'] - 200) * 0.001
        final_yield += bonus
    
    return final_yield

# Execution point of interest
final_yield = optimize_harvest(climate_data, soil_conditions)

# Print result as required
print(f"Result: {final_yield}")