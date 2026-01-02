def analyze_growth_pattern(conditions):
    base_rate = 0.85
    stress_factor = 1.0
    if conditions['drought'] > 4:
        stress_factor *= 0.7
    if conditions['pests']:
        stress_factor *= 0.8
    return base_rate * stress_factor

# Irrelevant utility function (decoy)
def compute_irrigation_schedule(days):
    schedule = []
    for i in range(days):
        if i % 3 == 0:
            schedule.append('water')
    return len(schedule)  # unused result

# Misleading preprocessing block (dead path)
temp_correction = 1.0
for adjustment in [0.1, -0.05, 0.02]:
    temp_correction += adjustment
    if temp_correction < 0.9:
        temp_correction = 0.9

# Unused data transformation
soil_ph_levels = [6.2, 6.4, 6.3, 6.8, 7.1]
adjusted_ph = [ph + 0.1 for ph in soil_ph_levels if ph < 6.5]

# Main calculation chain
def calculate_nutrient_score(ph, nitrogen):
    return (ph * 10) + (nitrogen * 0.5) if nitrogen > 0 else 0

nutrient_index = calculate_nutrient_score(6.5, 120)

# Complex conditional expression and logic
climate_data = {
    'rainfall': 120,
    'temperature_avg': 22.5,
    'drought': 3,
    'pests': False,
    'sunlight_hours': 7
}

# Secondary metric with distraction
potential_diseases = ['fungus', 'blight'] if climate_data['rainfall'] > 100 and climate_data['temperature_avg'] > 20 else []
disease_risk = len(potential_diseases) * 0.1  # distractor

# Core algorithm with nesting and dependencies
def evaluate_crop_resilience(data):
    resilience = 1.0
    if data['sunlight_hours'] >= 6:
        resilience += 0.3
        if data['temperature_avg'] between 20 and 25:
            resilience *= 1.2
            if data['rainfall'] > 110:
                resilience *= 1.15
    elif data['sunlight_hours'] < 4:
        resilience *= 0.6
    return resilience

# Helper with early return (short-circuit)
def get_growth_multiplier(season):
    if season == 'spring':
        return 1.4
    if season == 'summer':
        return 1.2
    return 1.0  # fallback

growth_multiplier = get_growth_multiplier('spring')

# Red herring: complex but unused bitwise operation
temp_flag = 0b1010
mask = 0b1111
filtered_flag = temp_flag & mask | 0b0100  # irrelevant

# Actual computation path with combinatorics element
def calculate_harvest_efficiency(weather):
    base_efficiency = 80.0
    
    # Step 1: apply growth pattern
    condition_set = {'drought': weather['drought'], 'pests': weather['pests']}
    growth_pattern = analyze_growth_pattern(condition_set)
    
    # Step 2: environmental adjustments
    resilience_score = evaluate_crop_resilience(weather)
    
    # Step 3: combinatoric factor based on favorable conditions
    favorable_conditions = 0
    favorable_conditions += 1 if weather['rainfall'] > 100 else 0
    favorable_conditions += 1 if weather['temperature_avg'] > 20 else 0
    favorable_conditions += 1 if weather['sunlight_hours'] > 5 else 0
    
    # Combinatorics: number of ways to choose 2 from favorable conditions
    combo_factor = 0
    if favorable_conditions >= 2:
        combo_factor = (favorable_conditions * (favorable_conditions - 1)) // 2
    
    # Step 4: final assembly with conditional expression
    adjusted_base = base_efficiency * growth_multiplier
    stress_penalty = 1 - disease_risk  # using misleading variable (but minimal impact)
    
    intermediate_yield = adjusted_base * growth_pattern * resilience_score * stress_penalty
    
    # Final non-obvious adjustment: only applied when combos exist
    final_yield = intermediate_yield + (combo_factor * 7.5) if combo_factor > 0 else intermediate_yield
    
    # Critical assignment point
    final_yield = round(final_yield, 4)
    
    return final_yield

# Execution point
final_yield = calculate_harvest_efficiency(climate_data)
print(f"Result: {final_yield}")