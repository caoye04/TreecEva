import math

# Simulated agricultural yield optimization system
def analyze_soil_composition(ph, nitrogen, organic_matter):
    # Irrelevant computation path (dead code)
    if ph < 0 or nitrogen < 0:
        return -1
    quality_score = (ph * 10) + (nitrogen * 5) + (organic_matter * 3)
    return quality_score if quality_score > 50 else 50

def compute_irrigation_efficiency(water_volume, coverage_area, evaporation_rate):
    # Distractor function with misleading intermediate values
    effective_water = water_volume * (1 - evaporation_rate)
    efficiency = (effective_water / coverage_area) * 100
    if efficiency > 90:
        efficiency = 90  # Cap for no real reason (red herring)
    return efficiency

def generate_crop_rotation_plan(previous_crop, soil_type):
    # Unused function - decoy logic
    rotation_map = {'corn': 'soybean', 'wheat': 'clover', 'rice': 'barley'}
    return rotation_map.get(previous_crop, 'fallow')

def calculate_biomass_potential(heights, densities):
    # Another distractor: computes biomass but not used in final result
    total_biomass = 0
    for h, d in zip(heights, densities):
        total_biomass += h ** 2 * d * 0.45
    return round(total_biomass, 2)

def calculate_harvest_efficiency(metrics):
    base_efficiency = metrics['base']
    slope_factor = metrics['slope']
    pest_index = metrics['pests']
    rainfall_deviation = metrics['rainfall']

    # Complex conditional expression with red herrings
    adjustment = 0.95 if slope_factor > 15 else (0.85 if slope_factor > 25 else 1.0)
    
    # Meaningless transformations to distract
    dummy_calc = (pest_index * 2.3 + rainfall_deviation * -1.1)
    dummy_calc = math.sin(dummy_calc) if dummy_calc != 0 else 0

    # Real logic buried among noise
    adjusted_rainfall = 1.0
    if rainfall_deviation > 10:
        adjusted_rainfall = 0.8
    elif rainfall_deviation < -10:
        adjusted_rainfall = 1.2

    # Key logic step: multiple interdependent conditions
    if base_efficiency >= 80:
        efficiency = base_efficiency * adjustment * adjusted_rainfall
        if pest_index > 20:
            efficiency *= 0.88
    else:
        efficiency = base_efficiency * 0.75

    # List comprehension that looks important but is only used for minor adjustment
    stress_factors = [x for x in [slope_factor, pest_index, rainfall_deviation] if x > 15]
    penalty = len(stress_factors) * 0.02
    efficiency *= (1 - penalty)

    # Final clamping (real result)
    efficiency = max(50, min(efficiency, 100))
    return round(efficiency, 4)

# Main execution block
if __name__ == "__main__":
    # Input data for simulation
    area_metrics = {
        'base': 88,
        'slope': 18,
        'pests': 22,
        'rainfall': 12
    }

    # Irrelevant precomputations (distractors)
    soil_q = analyze_soil_composition(ph=6.8, nitrogen=7, organic_matter=3.2)
    irrigation_eff = compute_irrigation_efficiency(water_volume=1200, coverage_area=15, evaporation_rate=0.18)
    rotation = generate_crop_rotation_plan('corn', 'loam')
    biomass = calculate_biomass_potential([1.2, 1.5, 1.1], [0.8, 0.9, 0.7])

    # Key computation chain starts here
    preliminary_check = soil_q > 70 and irrigation_eff > 75
    if preliminary_check:
        scaling_factor = 1.05
    else:
        scaling_factor = 0.95

    # This looks like it affects result but doesn't (misleading)
    temp_yield = 88 * scaling_factor

    # ACTUAL critical calculation
    final_yield = calculate_harvest_efficiency(area_metrics)

    # Dead code path (never executed but looks plausible)
    if False:
        fallback_metrics = {k: v * 1.1 for k, v in area_metrics.items()}
        final_yield = calculate_harvest_efficiency(fallback_metrics)

    print(f"Result: {final_yield}")