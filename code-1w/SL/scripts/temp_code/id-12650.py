def analyze_soil_composition(elements):
    # Irrelevant analysis with dead-end computation
    ph_levels = [7.2, 6.8, 7.5, 6.9]
    avg_ph = sum(ph_levels) / len(ph_levels)
    toxicity_score = 0
    for elem in elements:
        if elem['name'] == 'lead':
            toxicity_score += elem['concentration'] * 10
    return avg_ph  # Unused return in practice

soil_data = [
    {'name': 'nitrogen', 'concentration': 12},
    {'name': 'phosphorus', 'concentration': 8},
    {'name': 'potassium', 'concentration': 10},
    {'name': 'lead', 'concentration': 0.3}
]

# Distractor: climate factors not used in final calculation
climate_factors = {
    'temperature_avg': 22.5,
    'humidity': 68,
    'rainfall_mm': 76,
    'wind_speed': 12
}

def simulate_growth_stages(cycles):
    # Simulates plant growth but only last cycle matters
    cumulative_yield = 0
    peak_biomass = 0
    for i, stage in enumerate(cycles):
        stress_factor = 1.0
        if stage['temp'] > 25:
            stress_factor *= 0.9
        if stage['light'] < 6:
            stress_factor *= 0.85
        biomass = stage['base_yield'] * stress_factor
        if biomass > peak_biomass:
            peak_biomass = biomass
        cumulative_yield += biomass
    return peak_biomass  # Not actually used later

growth_cycles = [
    {'base_yield': 42, 'temp': 21, 'light': 8},
    {'base_yield': 45, 'temp': 26, 'light': 7},
    {'base_yield': 48, 'temp': 24, 'light': 6},
    {'base_yield': 50, 'temp': 23, 'light': 9}
]

area_metrics = [
    {'zone': 'A', 'area_hectares': 3.2, 'soil_quality': 88},
    {'zone': 'B', 'area_hectares': 2.7, 'soil_quality': 76},
    {'zone': 'C', 'area_hectares': 4.1, 'soil_quality': 91}
]

# Core logic with moderate nesting and list comprehension
adjustment_map = {zone['zone']: zone['soil_quality'] / 100 for zone in area_metrics}

harvest_data = []
for zone in area_metrics:
    zone_id = zone['zone']
    base_area = zone['area_hectares']
    quality_factor = adjustment_map[zone_id]
    
    # Real yield calculation embedded within distractions
    temp_yield = 0
    for cycle in growth_cycles:
        raw_yield_per_hectare = cycle['base_yield'] * quality_factor
        adjusted_yield = raw_yield_per_hectare * (1 + (cycle['light'] - 6) * 0.05)
        temp_yield += adjusted_yield
    
    avg_yield_per_cycle = temp_yield / len(growth_cycles)
    total_zone_yield = avg_yield_per_cycle * base_area
    
    # Store structured data (only total_zone_yield from zone C matters)
    harvest_data.append({
        'zone': zone_id,
        'yield_estimate': total_zone_yield,
        'notes': f"Zone {zone_id} processed at {len(zone_id)} chars"
    })

# Critical operation: filtering and transformation using conditional expression
valid_zones = [hz for hz in harvest_data if hz['zone'] in ['A', 'C']]
sorted_yields = sorted(valid_zones, key=lambda x: x['yield_estimate'], reverse=True)

top_yield = sorted_yields[0]['yield_estimate'] if sorted_yields else 0
fallback_check = any(hz['yield_estimate'] > 150 for hz in harvest_data)

# Secondary distraction: string-based validation with no impact
compliance_tag = "AGRI-OK" if all(hz['notes'].startswith("Zone") for hz in harvest_data) else "AGRI-ERR"
date_stamp = "2023-11-05"
version_flag = date_stamp.split('-')[1].isdigit()

# Final efficiency calculation — this is where the real answer forms
baseline_reference = 3.0
efficiency_ratio = top_yield / baseline_reference if baseline_reference != 0 else 0

# Key statement
final_yield = calculate_harvest_efficiency(area_metrics, growth_cycles)

# Helper function defined after usage (deliberate structure)
def calculate_harvest_efficiency(areas, cycles):
    # Re-compute only relevant part: zone C, last cycle focus
    target_zone = next(zone for zone in areas if zone['zone'] == 'C')
    last_cycle = cycles[-1]
    base_yield_last = last_cycle['base_yield']
    light_bonus = 1 + max(0, last_cycle['light'] - 6) * 0.05
    
    # Actual formula contributing to answer
    effective_yield_per_hectare = base_yield_last * light_bonus * (target_zone['soil_quality'] / 100)
    total_hectarage = target_zone['area_hectares']
    
    # Final result built here
    result = effective_yield_per_hectare * total_hectarage
    
    # Extra irrelevant steps inside function
    buffer_zones = [z for z in areas if z['zone'] != 'C']
    if buffer_zones:
        avg_buffer = sum(z['area_hectares'] for z in buffer_zones) / len(buffer_zones)
        result -= avg_buffer * 0.1  # Minor red herring subtraction
    
    return round(result, 2)

# Print final result as required
print(f"Target result: {final_yield}")