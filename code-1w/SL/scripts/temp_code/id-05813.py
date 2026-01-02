import itertools

# Simulated agricultural field data with noise and irrelevant metrics
def generate_field_data():
    base_yield = [85, 90, 78, 92, 88]
    pest_levels = [0.4, 0.6, 0.3, 0.8, 0.5]  # unused distractor
    rainfall_mm = [120, 135, 110, 150, 130]
    soil_ph = [6.2, 6.4, 5.9, 6.8, 6.3]
    temperature_avg = [22.1, 23.5, 21.8, 24.0, 22.9]  # misleading but unused
    
    # Distractor transformation
    adjusted_rainfall = [r * 0.9 for r in rainfall_mm]
    ph_ranking = sorted(enumerate(soil_ph), key=lambda x: x[1], reverse=True)
    
    # Real processing begins
    normalized_yield = [(y - min(base_yield)) / (max(base_yield) - min(base_yield)) for y in base_yield]
    return list(zip(base_yield, normalized_yield, rainfall_mm))

# Irrelevant utility function (decoy)
def calculate_irrigation_efficiency(data):
    total_flow = 0
    for i in range(len(data)):
        total_flow += data[i][2] * 0.75 + 12
    efficiency_score = total_flow / (len(data) * 100)
    return efficiency_score  # never used

# Another red herring: climate risk assessment
def assess_climate_risk(fields):
    risk_factors = []
    for idx, row in enumerate(fields):
        base, norm, rain = row
        risk = (norm * 0.3) + (rain / 200 * 0.7)
        if rain > 140:
            risk *= 1.5
        risk_factors.append((idx, risk))
    ranked_risks = sorted(risk_factors, key=lambda x: x[1], reverse=True)
    return [r[0] for r in ranked_risks]  # computed but unused

# Core logic disguised among distractions
def filter_optimal_conditions(field_data):
    selected = []
    for record in field_data:
        base_yield, norm_yield, rainfall = record
        if norm_yield >= 0.5 and 115 <= rainfall <= 145:
            selected.append(base_yield)
    return selected

# Accumulation with itertools distraction
def transform_and_accumulate(yields):
    # Use of itertools - shuffle combinations (but only one matters)
    perms = list(itertools.permutations(yields[:2]))  # limited use
    perm_sum = sum([abs(p[0] - p[1]) for p in perms])  # irrelevant calculation
    
    # Actual relevant logic
    total = sum(yields)
    penalty = len(perms) % 3  # red herring computation
    adjusted_total = total - penalty
    return adjusted_total

# Misleading intermediate transformation
def apply_fertilizer_boost(data):
    boosted = [d + 5 for d in data]
    decay_factor = 0.95
    decayed = [b * (decay_factor ** i) for i, b in enumerate(boosted)]
    return [round(x, 2) for x in decayed]  # looks important, not used

# Real optimization path
def optimize_harvest(fields):
    filtered = filter_optimal_conditions(fields)
    accumulated = transform_and_accumulate(filtered)
    
    # Secondary check: exclude small yields
    if len(filtered) > 1:
        accumulated -= min(filtered)
    
    # Final adjustment based on pattern matching
    pattern_match = False
    for a, b in itertools.combinations(filtered, 2):
        if (a + b) % 7 == 0:
            pattern_match = True
            break
    bonus = 17 if pattern_match else 0
    result = accumulated + bonus
    return result

# Execution flow with multiple diversions
if __name__ == '__main__':
    raw_fields = generate_field_data()
    
    # Distractor calls
    _ = calculate_irrigation_efficiency(raw_fields)
    _ = assess_climate_risk(raw_fields)
    
    processed_fields = raw_fields  # appears transformed, but not yet
    temporary_boost = apply_fertilizer_boost([f[0] for f in raw_fields])  # dead end
    
    # Key execution point
    final_yield = optimize_harvest(processed_fields)
    
    print(f"Result: {final_yield}")