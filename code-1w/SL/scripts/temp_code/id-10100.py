import itertools

# Simulate agricultural yield prediction with multiple noise factors
def analyze_soil_composition(data_points):
    # Irrelevant computation path - dead end
    transformed = [x * 1.75 for x in data_points if x > 5]
    baseline = sum(transformed) / len(transformed) if transformed else 0
    return baseline

def generate_growth_phases(cycles):
    # Distractor: looks important but unused in final calculation
    phases = []
    for i in range(cycles):
        phase = (i ** 2 + 3 * i + 1) % 7
        phases.append(phase)
    return phases

def compute_nutrient_score(ph_levels, nutrient_levels):
    # Misleading intermediate metric
    score = 0
    for p, n in zip(ph_levels, nutrient_levels):
        if p > 6.0 and p < 7.5:
            score += n * 1.5
        else:
            score -= n * 0.5
    return round(score, 3)

def calculate_biomass_index(sequence):
    # Unused recursive red herring
    if len(sequence) <= 1:
        return sequence[0] if sequence else 0
    return sequence[0] + calculate_biomass_index(sequence[1:]) // 2

def evaluate_irrigation_efficiency(flow_rates):
    # Decoy function with plausible logic
    total = 0
    for rate in flow_rates:
        if rate < 10:
            total += rate * 0.8
        elif rate < 20:
            total += rate * 1.1
        else:
            total += rate * 0.9
    return total

def calculate_harvest_efficiency(metrics, cycles):
    # Core relevant logic buried in noise
    base_area = metrics['total_hectares']
    avg_rainfall = metrics['rainfall_avg']
    tech_index = metrics['technology_index']

    # Real computation starts here
    efficiency = base_area * 0.67
    for _ in range(cycles):
        efficiency = (efficiency + avg_rainfall) / 2  # Exponential smoothing over cycles
    
    # Critical adjustment using string-based condition
    region_code = metrics['region'].upper().strip()
    if 'NORTH' in region_code:
        efficiency *= 1.25
    elif 'SOUTH' in region_code:
        efficiency *= 0.85
    
    # Final correction based on combinatorics of valid sensors
    sensor_status = metrics['sensor_array']
    active_sensors = [s for s in sensor_status if s == 'OK']
    # Use itertools to create distraction but only length matters
    from itertools import combinations
    possible_pairs = list(combinations(active_sensors, 2))
    pair_count = len(possible_pairs)
    efficiency += pair_count * 0.5

    return int(efficiency)

# Main execution block with mixed signal and noise
if __name__ == '__main__':
    # Input data setup
    area_metrics = {
        'total_hectares': 142,
        'rainfall_avg': 89.3,
        'technology_index': 8.7,
        'region': 'NORTHEAST REGION',
        'sensor_array': ['OK', 'FAILED', 'OK', 'OK', 'UNKNOWN', 'OK'],
        'calibration_version': 'v2.1'
    }

    growth_cycles = 6

    # Irrelevant preprocessing steps (distractors)
    soil_data = [4.2, 5.1, 6.3, 7.8, 6.9, 5.5, 8.2]
    ph_levels = [6.2, 7.1, 5.9, 6.8]
    nutrient_levels = [12.3, 14.1, 10.5, 13.7]
    flow_rates = [8.5, 12.3, 25.1, 18.7, 9.2]

    _ = analyze_soil_composition(soil_data)
    _ = generate_growth_phases(growth_cycles)
    _ = compute_nutrient_score(ph_levels, nutrient_levels)
    _ = evaluate_irrigation_efficiency(flow_rates)

    # Key statement - target of the question
    final_yield = calculate_harvest_efficiency(area_metrics, growth_cycles)

    # Output result as required
    print(f"Target result: {final_yield}")