def analyze_growth_potential(conditions):
    """ Irrelevant analysis function (dead code path) """
    return sum(c * 0.3 for c in conditions if c > 5)

soil_profiles = [0.4, 0.7, 0.5, 0.9, 0.6]
climate_data = [22, 18, 25, 19, 24]

# Distractor variables (irrelevant computations)
temperature_baseline = sum(climate_data) / len(climate_data)
moisture_index = max(soil_profiles) * 100
phantom_score = temperature_baseline * moisture_index * 0.01

# Unused transformation map
data_weights = {i: w for i, w in enumerate([0.1, 0.3, 0.2, 0.3, 0.1])}

# Real processing begins — key logic hidden among distractions
def evaluate_stress_factor(temp_seq):
    stress = 0
    for t in temp_seq:
        if t < 20:
            stress += 0.1
        elif t > 23:
            stress += 0.05
    return stress

# Lambda-based adaptive response (relevant)
adapt_rate = lambda x: 0.8 + (x / 100) if x < 1 else 0.9

# Decoy accumulation loop (misleading intermediate result)
accumulated_risk = 0
for i in range(len(climate_data)):
    accumulated_risk += abs(climate_data[i] - temperature_baseline) * 0.1

# Core optimization with nested logic and distractors
def optimize_harvest(temps, soils):
    base_yield = 0.0
    stress_penalty = evaluate_stress_factor(temps)
    
    # Real yield calculation — 3 levels of nesting
    for idx, (t, s) in enumerate(zip(temps, soils)):
        adjustment = 1.0
        if t >= 20 and t <= 23:
            if s > 0.6:
                adjustment = 1.25
            else:
                adjustment = 1.1
        else:
            adjustment = 0.85
            
        # Bit manipulation red herring (irrelevant but plausible)
        encoded = idx ^ 5
        if encoded & 1:
            adjustment *= 0.98  # Minor decoy reduction
        
        contribution = (t * 0.4 + s * 50) * adjustment
        base_yield += contribution
    
    # Final nonlinear scaling (relevant)
    normalized = base_yield / len(temps)
    resilience_factor = adapt_rate(moisture_index)  # Uses distractor variable but only as pass-through
    
    # Misdirection: phantom_score appears to be used, but isn't
    dummy_influence = phantom_score * 0.001  # Never applied
    
    final = normalized * resilience_factor
    return round(final, 4)

# Execution point of interest
final_yield = optimize_harvest(climate_data, soil_profiles)

# Print required output
print(f"Result: {final_yield}")