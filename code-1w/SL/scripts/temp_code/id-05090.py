from itertools import compress, cycle

def analyze_soil_ph(levels):
    # Irrelevant helper: analyzes pH but not used in final result
    return [round(7.0 + 0.5 * i, 2) for i, lvl in enumerate(levels)]

def calculate_harvest_efficiency(areas, factors):
    # Core logic with distractors
    base_scores = [a * 1.5 for a in areas]
    adjusted_factors = [f + 0.1 for f in factors]
    
    # Distractor: unused transformation
    inverted_factors = [round(1/f, 3) for f in factors if f > 0]
    
    # Semi-relevant: prepares mask but only one part is used
    valid_areas = [a > 0.5 for a in areas]
    masked_factors = list(compress(adjusted_factors, valid_areas))
    
    # Key computation chain (5-8 steps)
    trend_cycle = cycle([1, -1])
    oscillation = [next(trend_cycle) * af for af in masked_factors[:len(areas)]]
    growth_trend = sum(oscillation) * 0.5
    
    # Apply lambda-based weighting
    weight_fn = lambda x: x ** 0.5 if x > 0 else 0
    weighted_areas = sum(weight_fn(a) for a in base_scores)
    
    # Final formula
    efficiency_score = weighted_areas * (1 + growth_trend / 10)
    return round(efficiency_score, 4)

# Simulation parameters (distractor)
ph_levels = [6.2, 6.8, 7.1, 6.5]
unused_diagnostic = analyze_soil_ph(ph_levels)

# Main data inputs
area_metrics = [0.8, 1.2, 0.9, 1.5]
growth_factors = [0.7, 0.9, 0.6, 1.1]

# Dead code path (distractor)
decay_rates = [0.05, 0.03, 0.07]
if len(decay_rates) > 5:
    growth_factors = [g * 0.9 for g in growth_factors]

# Key statement
final_yield = calculate_harvest_efficiency(area_metrics, growth_factors)

# Output
print(f"Result: {final_yield}")