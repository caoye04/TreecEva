def analyze_growth_potential(conditions):
    """Irrelevant analysis function (dead code path)"""
    score = 0
    for c in conditions:
        if c > 0.5:
            score += c ** 2
    return score

# Irrelevant global constants (distractors)
MAX_CAPACITY = 98765
BASE_THRESHOLD = 42
TEMPORARY_BUFFER = [0] * 100

soil_composition = {
    'clay': [0.2, 0.3, 0.25, 0.35, 0.4],
    'silt': [0.3, 0.2, 0.35, 0.25, 0.3],
    'sand': [0.5, 0.5, 0.4, 0.4, 0.4]
}

# Misleading intermediate calculation (red herring)
average_nutrients = []
for i in range(5):
    avg = (soil_composition['clay'][i] + soil_composition['silt'][i] + soil_composition['sand'][i]) / 3
    average_nutrients.append(avg * 10)

# Unused but plausible function (decoy)
def compute_erosion_risk(profiles):
    risk = 0
    for key in profiles:
        for val in profiles[key]:
            risk += val * 0.1
    return risk

# Real data inputs
climate_data = [22.5, 18.3, 25.1, 19.8, 23.0]
soil_profiles = [0.6, 0.4, 0.7, 0.5, 0.8]

# Distractor list with slicing that seems important but isn't used in final logic
temporal_trends = climate_data[1:4] + [x * 0.9 for x in climate_data[::2]]
baseline_ref = temporal_trends[-5:]

# Simulate false dependency on unused structures
aggregated = 0
for i in range(len(soil_composition['clay'])):
    aggregated += soil_composition['clay'][i] * climate_data[i]

# Critical function with relevant logic buried among distractions
def optimize_harvest(weather, soil):
    # Initialize accumulator (key variable)
    total_yield = 0
    
    # Real logic begins: weighted sum based on conditions
    weights = [0.3, 0.5, 0.7, 0.4, 0.6]
    
    # Primary computation loop (4 levels of nesting here)
    for i in range(len(weather)):
        temp_effect = 0
        if weather[i] > 20:
            temp_effect = 1.2
        else:
            temp_effect = 0.8
            
        # Nested conditional with bit manipulation red herring
        adjusted_soil = soil[i]
        if i % 2 == 0:
            # Bitwise operation that looks complex but is just obfuscation
            adjusted_soil = soil[i] ^ 0.1
            adjusted_soil = abs(adjusted_soil)  # Ensure positive

        # Core formula (hidden among distractions)
        contribution = (weights[i] * temp_effect * adjusted_soil) + (weather[i] / 100)
        
        # Accumulation with early termination check (real control flow)
        if contribution > 0.5:
            total_yield += contribution
        else:
            break  # Early exit possibility (not triggered here)
    
    # Secondary adjustment using slicing on a derived list (actual use)
    history_log = [total_yield * 0.9, total_yield * 0.95, total_yield, total_yield * 1.05, total_yield * 1.1]
    recent = history_log[2:]  # Slice to get last three values
    refined_yield = sum(recent) / len(recent)  # Average of recent projections
    
    # Final transformation
    return int(refined_yield * 100) / 100  # Round to two decimals

# Dead code assignment (misdirection)
initial_projection = analyze_growth_potential(climate_data)

# Key statement — answer depends on this execution
def final_yield():
    return optimize_harvest(climate_data, soil_profiles)

# Actual output
final_yield_value = final_yield()
print(f"Result: {final_yield_value}")