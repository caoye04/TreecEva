def analyze_growth_potential(nutrients, moisture_level):
    if not nutrients or len(moisture_level) == 0:
        return 0
    base_score = sum([nutrients[n] * 0.3 for n in nutrients])
    adjustment = 0.5 if moisture_level['current'] > 60 else 0.2
    return base_score * adjustment

soil_data = {
    'nitrogen': 45,
    'phosphorus': 30,
    'potassium': 25,
    'organic_matter': 8
}

moisture_profile = {
    'current': 72,
    'peak': 88,
    'deficit': 12
}

historical_yields = [230, 245, 260, 238, 252]

# Distractor: irrelevant trend analysis
yield_trend = sum(historical_yields[i] - historical_yields[i-1] 
                   for i in range(1, len(historical_yields)) if historical_yields[i] > historical_yields[i-1])

projected_increase = yield_trend / len(historical_yields)

# Real computation begins
baseline_moisture_effect = moisture_profile['current'] * 0.6

if baseline_moisture_effect > 40:
    baseline_moisture_effect *= 1.15

# Simulate multiple growth cycles with varying conditions
growth_cycles = []
for cycle in range(3):
    adjusted_nutrients = {k: v + (cycle * 2) for k, v in soil_data.items()}
    stress_factor = 0.9 if cycle == 2 and moisture_profile['deficit'] < 15 else 1.0
    
    # Irrelevant string manipulation (distractor)
    cycle_label = f"Cycle-{cycle+1}"
    cycle_tag = cycle_label.lower().replace('-', '_')
    
    # Semi-relevant intermediate
    temp_yield = (sum(adjusted_nutrients.values()) * baseline_moisture_effect * 0.01) * stress_factor
    growth_cycles.append(temp_yield)

# Secondary distractor: unused helper logic
def compute_rainfall_impact(rf_mm):
    if rf_mm < 100:
        return rf_mm * 0.01
    elif rf_mm < 200:
        return rf_mm * 0.012
    else:
        return rf_mm * 0.008

rainfall_impact_estimate = compute_rainfall_impact(142)

# Core calculation with slicing distraction
recent_high_yields = sorted(historical_yields)[-2:]  # slicing used but not critical
bonus_multiplier = 1.05 if len(recent_high_yields) == 2 and recent_high_yields[0] > 240 else 1.0

# Actual yield determination
raw_total = sum(growth_cycles)

# Conditional expression used
penalty = 15 if len(soil_data.keys()) > 3 else 0
adjusted_total = raw_total - penalty

# Final step combines dictionary-derived score
aux_score = analyze_growth_potential(soil_data, moisture_profile)
final_yield = adjusted_total + (aux_score * 10)

# Introduce dead code path (distractor)
if False:
    final_yield *= 0.9

Result: final_yield