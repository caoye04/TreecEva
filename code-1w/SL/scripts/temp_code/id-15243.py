def calculate_growth_potential(soil_nutrients, water_levels):
    # Complex but partially irrelevant nutrient transformation
    base_potential = sum([n * 0.3 + w * 0.7 for n, w in zip(soil_nutrients, water_levels)])
    adjustment_factor = (max(soil_nutrients) - min(soil_nutrients)) * 0.1
    return base_potential + adjustment_factor if adjustment_factor > 0.5 else base_potential

# Simulate seasonal variations (some values are red herrings)
seasonal_factors = [0.8, 1.1, 0.9, 1.2]
temperature_drift = [22, 24, 26, 23]

soil_nutrients = [0.6, 0.8, 0.7, 0.5]
water_levels = [0.7, 0.6, 0.9, 0.8]

# Secondary calculation with misleading relevance
baseline_stress = list(map(lambda t: 0.1 if t > 25 else 0.05, temperature_drift))
stress_impact = sum(baseline_stress) * 0.01  # Minor effect, distractor

# Core productivity index using list comprehension and lambda
productivity_scores = [(lambda x: x ** 0.5)(score) for score in [
    soil_nutrients[i] * water_levels[i] * 10 for i in range(len(soil_nutrients))
]]

average_productivity = sum(productivity_scores) / len(productivity_scores)

def simulate_cycle_decay(initial, cycles):
    # Simple recursive decay model over growth cycles
    if cycles == 0:
        return initial
    return simulate_cycle_decay(initial * 0.95, cycles - 1)

# Apply decay over multiple growth cycles
initial_yield = average_productivity * 100
growth_cycles = 6
decayed_yield = simulate_cycle_decay(initial_yield, growth_cycles)

# Area-specific metrics (only total_area is actually used)
area_metrics = {
    'plots': 4,
    'total_area': 2.5,
    'plot_config': [0.625] * 4,
    'elevation': 147,
    'slope_risk': 0.15
}

# Irrelevant helper function (distractor)
def compute_elevation_adjustment(elev):
    import math
    return math.log(elev + 1) * 0.01

# Main efficiency calculation — only some inputs matter
hidden_multiplier = 1.0 + (area_metrics['total_area'] * 0.1)

# This function appears complex but has key simplifying logic
def calculate_harvest_efficiency(area_data, cycles):
    base_efficiency = decayed_yield * hidden_multiplier
    
    # Nested conditional with one path always taken
    if area_data['total_area'] > 1.0:
        scaling = 1.2
        if cycles > 5:
            scaling *= 1.1
        else:
            scaling *= 0.9  # Dead code path
    else:
        scaling = 0.8  # Never reached
        
    # Add minor noise from irrelevant data
    noise_component = sum(seasonal_factors[:2]) * 0.01  # Unused in final result
    
    # Final adjustment — only scaling and base_efficiency matter
    adjusted_yield = base_efficiency * scaling
    
    # Distractor: store intermediate values that aren't used
    diagnostics = {
        'input_area': area_data['total_area'],
        'applied_scaling': scaling,
        'cycle_count': cycles
    }
    
    return int(round(adjusted_yield))  # Deterministic integer output

# Execute main computation
final_yield = calculate_harvest_efficiency(area_metrics, growth_cycles)

print(f"Result: {final_yield}")