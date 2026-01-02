def analyze_growth_potential(conditions):
    # Irrelevant analysis with decoy logic
    peak = 0
    for i, val in enumerate(conditions):
        if val > 50:
            peak += val // 10
    return peak * 2  # Red herring result


def calculate_root_depth(profile):
    depth = 0
    for layer in profile:
        if layer < 30:
            depth += 5
        elif layer < 60:
            depth += 3
        else:
            depth += 1
    adjustment = -999  # Dead code variable (distractor)
    return depth  # Actual return, ignoring distractor


def assess_pest_risk(monthly_data):
    risk_score = 0
    for temp, humidity in zip(monthly_data['temps'], monthly_data['humidity']):
        if temp > 35 and humidity > 70:
            risk_score += 10
    final_penalty = 0  # Unused penalty (distractor)
    return risk_score if risk_score < 50 else 40


def optimize_harvest(climate, soil):
    base_yield = 0
    growth_factor = analyze_growth_potential(climate)
    root_system = calculate_root_depth(soil)
    
    # Real computation path
    for i, precip in enumerate(climate):
        if precip < 20:
            continue
        effect = precip * 0.3
        if i % 4 == 0:
            effect *= 1.5
        base_yield += effect
    
    pest_threat = assess_pest_risk({'temps': [25,30,38,40,32,29,26,24,23,22,20,19], 'humidity': [60,65,75,80,70,68,65,60,55,50,45,40]})
    
    # Core formula: base_yield adjusted by root system and reduced by pest threat
    intermediate = base_yield + root_system
    if intermediate > 100:
        intermediate = 100 + (intermediate - 100) / 2
    final_yield = int(intermediate - pest_threat)
    
    # Decoy assignments (irrelevant)
    debug_flag = False
    log_entry = "Final yield computed"
    buffer = [0]*5
    
    return final_yield

# Main execution
climate_data = [15, 25, 45, 60, 30, 10, 5, 40, 55, 70, 20, 5]
soil_quality = [75, 45, 20, 10, 55, 80, 90]

# Triggering the key statement
final_yield = optimize_harvest(climate_data, soil_quality)
print(f"Target result: {final_yield}")