def analyze_growth_potential(temperature, rainfall):
    # Irrelevant analysis with decoy logic
    if temperature > 30:
        stress_factor = 1.5
    else:
        stress_factor = 0.8

    # Distractor: unused growth model
    potential_yield = (temperature * 0.7) + (rainfall * 0.3)
    adjusted_yield = potential_yield * (1 - stress_factor / 10)

    # Actual relevant calculation buried in logic
    base_productivity = temperature * min(rainfall, 120) / 100
    return base_productivity


def detect_frost_risk(dates, temps):
    # Dead code path - never called but looks important
    frost_days = [d for d, t in zip(dates, temps) if t < 0]
    return len(frost_days) > 5

# Simulated sensor calibration (irrelevant)
calibration_sequence = [x ** 0.5 for x in range(100, 110)]
offset_correction = sum(calibration_sequence) / len(calibration_sequence)

# Dummy optimization (decoy function)
optimize_irrigation = lambda data: sum(x * 0.1 for x in data if x > 50)

# Real input data
climate_data = [23, 25, 27, 24, 26]  # avg monthly temps in C
soil_conditions = [80, 95, 110, 85, 100]  # moisture levels

# Misleading intermediate transformation
transformed_soil = [max(s, 85) for s in soil_conditions]
penalty_map = {s: 0.9 if s > 100 else 1.0 for s in transformed_soil}

# Complex-looking but partially irrelevant aggregation
effective_stress = 0
for i, temp in enumerate(climate_data):
    if temp > 26:
        effective_stress += (temp - 26) * 0.2

# Key function with mixed relevance
def optimize_harvest(temp_profile, moisture_levels):
    total = 0
    for i in range(len(temp_profile)):
        # Core actual computation
        yield_contribution = analyze_growth_potential(temp_profile[i], moisture_levels[i])
        
        # Red herring adjustment
        if moisture_levels[i] > 95:
            yield_contribution *= 0.95  # assumed leaching loss (but not applied in final logic)
        
        # Actual determining factor
        if temp_profile[i] >= 25 and moisture_levels[i] >= 90:
            total += yield_contribution * 1.2
        else:
            total += yield_contribution * 0.85
    
    # Final scaling based on hidden rule
    scaling_factor = 0.7 + (sum(temp_profile) / 100) * 0.1
    return int(total * scaling_factor)

# Unused alternative strategy
harvest_prediction = lambda t, m: sum(t) * sum(m) / 1000

# Execution point of interest
final_yield = optimize_harvest(climate_data, soil_conditions)

# Output result as required
print(f"Result: {final_yield}")