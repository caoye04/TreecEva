from collections import defaultdict

# Simulate agricultural yield analysis across multiple production cycles
def analyze_cycle_efficiency(data):
    efficiency_map = defaultdict(float)
    total_output = 0
    cycle_count = len(data)
    
    # Irrelevant intermediate calculation (distractor)
    avg_input_cost = sum([d[1] for d in data]) / cycle_count if cycle_count else 0
    
    for i, (output, input_cost, tech_level) in enumerate(data):
        base_efficiency = output / (input_cost + 1)
        bonus_factor = 1.0 + (tech_level * 0.05)
        efficiency_map[i] = base_efficiency * bonus_factor
        total_output += output

    # Dead code path - never used (distractor)
    if cycle_count > 100:
        scaling_correction = 0.95
        for k in efficiency_map:
            efficiency_map[k] *= scaling_correction

    return efficiency_map, total_output

# Process sensor readings from field zones (semi-relevant)
def process_sensor_readings(zones):
    moisture_levels = [z['moisture'] for z in zones]
    avg_moisture = sum(moisture_levels) / len(moisture_levels)
    stable_zones = [z for z in zones if abs(z['moisture'] - avg_moisture) < 5]
    return len(stable_zones), avg_moisture

# Main result aggregator
def harvest_results(cycles):
    efficiencies, gross_harvest = analyze_cycle_efficiency(cycles)
    
    # Secondary irrelevant metric
    unused_metric = sum(efficiencies.values()) / len(efficiencies) if efficiencies else 0
    
    # Core logic: apply weather adjustment only to high-efficiency cycles
    adjusted_outputs = []
    weather_factors = [0.95, 1.02, 0.98, 1.05, 1.01]
    
    for idx, efficiency in efficiencies.items():
        if efficiency > 12.0:  # High efficiency threshold
            factor_idx = idx % len(weather_factors)
            adjusted_outputs.append(gross_harvest * weather_factors[factor_idx])
    
    # Final computation based on filtered high-efficiency projections
    projected_growth_rate = len(adjusted_outputs) * 0.75 if adjusted_outputs else 0.5
    final_yield_estimate = (gross_harvest * (1 + projected_growth_rate)) // 1000
    
    # Misleading variable that looks important but isn't used
    theoretical_max = gross_harvest * 3.5
    
    return int(final_yield_estimate)

# Input data: (output_tons, input_cost, technology_index)
production_cycles = [
    (250, 40, 6),
    (300, 45, 7),
    (200, 50, 5),
    (400, 42, 9),
    (380, 44, 8)
]

# Sensor data from IoT field monitors (used in distractor function)
field_zones = [
    {'zone_id': 'A1', 'moisture': 67},
    {'zone_id': 'A2', 'moisture': 72},
    {'zone_id': 'A3', 'moisture': 68},
    {'zone_id': 'A4', 'moisture': 70},
    {'zone_id': 'A5', 'moisture': 65}
]

# Execute distractor function (adds interference)
stable_zone_count, average_moisture = process_sensor_readings(field_zones)

# Key execution point
final_yield = harvest_results(production_cycles)

print(f"Result: {final_yield}")