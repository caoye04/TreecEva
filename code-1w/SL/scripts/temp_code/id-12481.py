def analyze_growth_potential(conditions):
    """ Irrelevant deep analysis function (dead code path) """
    cumulative_stress = 0
    for i, cond in enumerate(conditions):
        if cond < 0.5:
            cumulative_stress += pow(cond, 3)
    return cumulative_stress

# Distractor: Unused but plausible-looking data transformation
def normalize_readings(data_list):
    factor = 1.0 / max(data_list)
    return [x * factor for x in data_list]

# Decoy optimization using bitwise confusion
def false_optimization(mask, values):
    result = 0
    for v in values:
        result ^= int(v * 100) & mask
    return result

# Real computational chain begins here
soil_nutrients = [0.4, 0.7, 0.9, 0.5, 0.3]
precipitation_levels = [120, 89, 102, 134, 76]
temperature_extremes = [(23, 31), (19, 28), (22, 33), (20, 29), (18, 27)]

def calculate_thermal_stress(temp_pairs):
    stress_score = 0.0
    for idx, (low, high) in enumerate(temp_pairs):
        deviation = abs(high - 30) + abs(low - 20)
        stress_score += deviation * 0.3
    return stress_score

baseline_stress = calculate_thermal_stress(temperature_extremes)

# Simulate sensor degradation (irrelevant)
sensor_age_years = 7
degradation_factor = sum([0.05 * pow(1.2, i) for i in range(sensor_age_years)])
adjusted_readings = [p * (1 - degradation_factor) for p in precipitation_levels]  # unused later

# Core logic disguised among distractors
climate_data = {
    'moisture': precipitation_levels,
    'instability': [abs(p - 100) for p in precipitation_levels],
    'thermal': [t[1] - t[0] for t in temperature_extremes]
}

soil_profiles = {
    'ph_levels': [6.2, 6.8, 7.1, 6.5, 6.0],
    'nitrogen': soil_nutrients,
    'density': [1.3, 1.4, 1.2, 1.5, 1.6]
}

# Red herring: complex but unused bit manipulation
def compute_fertility_signature(profiles):
    sig = 0
    for i, n in enumerate(profiles['nitrogen']):
        val = int(n * 100)
        sig = (sig << 3) ^ val ^ (i << 2)
    return sig & 0xFFFF

signature = compute_fertility_signature(soil_profiles)  # computed but not used

# Actual relevant logic hidden in recursion and dictionary ops
def evaluate_region_suitability(moisture_seq, nutrients):
    if len(moisture_seq) == 1:
        return moisture_seq[0] * nutrients[0] * 0.01
    mid = len(moisture_seq) // 2
    left = evaluate_region_suitability(moisture_seq[:mid], nutrients[:mid])
    right = evaluate_region_suitability(moisture_seq[mid:], nutrients[mid:])
    return left + right + (moisture_seq[0] % 7)

# Misleading aggregation
false_yield = sum([soil_profiles['ph_levels'][i] * climate_data['moisture'][i] for i in range(5)]) / 5

# Key recursive optimization with modular arithmetic and zip
def optimize_harvest(climate, soils):
    total_yield = 0.0
    
    # Use of zip and enumerate together
    for i, (moist, thermal_var) in enumerate(zip(climate['moisture'], climate['thermal'])):
        ph_val = soils['ph_levels'][i]
        nutrient_level = soils['nitrogen'][i]
        
        # Relevant condition masked by irrelevant ones
        if ph_val >= 6.0 and ph_val <= 7.0:
            base_yield = moist * nutrient_level * 0.1
            if thermal_var > 8:
                base_yield *= 0.85  # stress penalty
            total_yield += base_yield
    
    # Final adjustment using modular influence from day-of-cycle
    cycle_day = 23
    modulation = (cycle_day % 4) * 0.05
    total_yield += total_yield * modulation
    
    # Dead code branch - never reached due to structure
    if total_yield < 0:
        fallback = 0
        for k, v in soils.items():
            fallback += len(v)
        return fallback

    return total_yield

# Trigger execution
final_yield = optimize_harvest(climate_data, soil_profiles)
print(f"Target result: {final_yield}")