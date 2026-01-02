import itertools

# Simulate crop yield under environmental stress and varying exposure
def calculate_stress_modifier(age, temperature, rainfall):
    base_modifier = 0.8 if temperature > 35 else 1.0
    if rainfall < 100:
        drought_penalty = 0.6 if age > 60 else 0.9
    else:
        drought_penalty = 1.0
    
    # Irrelevant computation (distractor)
    hypothetical_rainfall = rainfall * 1.5 + 20
    unused_projection = hypothetical_rainfall ** 0.5

    return base_modifier * drought_penalty

def compute_photons_per_day(day_of_year):
    # Approximate solar cycle
    angle = 2 * 3.14159 * day_of_year / 365
    photons = 1000 + 300 * (0.5 - abs(0.5 - (day_of_year % 180) / 180))
    return int(photons)

def assess_canopy_density(leaves_per_branch, branches):
    total_leaves = leaves_per_branch * branches
    if total_leaves > 2000:
        return 0.75
    elif total_leaves > 1000:
        return 0.9
    else:
        return 1.0

def simulate_growth_cycle(days, initial_size, temp_seq):
    size = initial_size
    growth_log = []
    
    for d in range(days):
        temp = temp_seq[d % len(temp_seq)]
        daily_growth = size * 0.03 * (1 + temp / 100)
        
        # Dummy tracking (not used later)
        if d % 10 == 0:
            snapshot = {"day": d, "size": size, "growth": daily_growth}
            growth_log.append(snapshot)
        
        size += daily_growth
    
    # Dead code path (distractor)
    final_snapshot = None
    if False:  # Never executed
        final_snapshot = growth_log[-1] if growth_log else None
    
    return size

def harvest_results(exposures, stresses):
    cumulative_yield = 0
    peak_stress = max(stresses)
    adjusted_exposures = [e * 1.2 for e in exposures if e > 5]
    
    # Use itertools to generate combinations (semi-relevant)
    pairs = list(itertools.combinations_with_replacement(adjusted_exposures[:3], 2))
    interaction_bonus = sum(abs(a - b) for a, b in pairs) * 0.05
    
    for exp, stress in zip(exposures, stresses):
        raw_yield = exp * (1 - stress / 10.0)
        if raw_yield < 0:
            raw_yield = 0
        
        # Apply canopy adjustment (irrelevant in this context)
        dummy_canopy = assess_canopy_density(150, 8)
        adjusted_yield = raw_yield * dummy_canopy
        
        cumulative_yield += adjusted_yield
    
    cumulative_yield += interaction_bonus
    
    # Final adjustment based on average exposure
    avg_exp = sum(exposures) / len(exposures)
    if avg_exp > 10:
        cumulative_yield *= 1.1
    
    return int(cumulative_yield)

# Main simulation setup
exposure_levels = [12, 15, 8, 20, 6]
stress_factors = [2.3, 3.1, 1.8, 4.0, 1.5]
temperature_profile = [25, 30, 38, 33, 28]
day_sequence = [120, 150, 180, 210, 240]

# Preliminary simulations (distractors)
projected_photons = [compute_photons_per_day(d) for d in day_sequence]
growth_prediction = simulate_growth_cycle(90, 5.0, temperature_profile)
baseline_modifier = calculate_stress_modifier(75, 36, 80)

# Key computation
final_yield = harvest_results(exposure_levels, stress_factors)

# Output result
print(f"Result: {final_yield}")