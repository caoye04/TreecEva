def analyze_crop_performance(data, threshold=0.75):
    filtered_data = [d for d in data if d['viability'] > threshold]
    total_viable = sum(item['area'] for item in filtered_data)
    return total_viable

seasonal_factors = {'spring': 1.2, 'summer': 1.5, 'autumn': 0.9, 'winter': 0.3}
growth_cycles = [23, 15, 31, 18]
area_metrics = [
    {'zone': 'A', 'area': 120, 'viability': 0.82},
    {'zone': 'B', 'area': 95, 'viability': 0.68},
    {'zone': 'C', 'area': 140, 'viability': 0.91},
    {'zone': 'D', 'area': 87, 'viability': 0.74}
]

# Extraneous computation: simulate soil pH adjustments (not used in final result)
pH_corrections = []
for i in range(len(growth_cycles)):
    correction = (growth_cycles[i] % 7) * 0.05
    pH_corrections.append(round(correction, 2))

temp_buffer = [x * 0.1 for x in growth_cycles if x > 16]
rolling_avg = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0

# Core logic with distractors
baseline = sum([g for g in growth_cycles]) / len(growth_cycles)
efficiency_map = {}
for idx, cycle in enumerate(growth_cycles):
    factor = seasonal_factors['spring'] if idx % 2 == 0 else seasonal_factors['autumn']
    adjusted = cycle * factor * (area_metrics[idx]['viability'] + 0.1)
    efficiency_map[f'cycle_{idx}'] = adjusted

# Secondary irrelevant structure: track unused diagnostics
diagnostics = {}
for zone_data in area_metrics:
    z_name = zone_data['zone']
    stress_index = (zone_data['area'] / 100) * (1 - zone_data['viability'])
    diagnostics[z_name] = round(stress_index, 3)

# Key function using list comprehension and dictionary ops
def calculate_harvest_efficiency(zones, cycles):
    viable_zones = [z for z in zones if z['viability'] >= 0.75]
    zone_names = [z['zone'] for z in viable_zones]
    
    # Real computation chain
    base_yield = 0
    for i, c in enumerate(cycles):
        if i < len(zone_names):  # prevent index error
            modifier = 1.1 if 'A' in zone_names else 1.05
            base_yield += c * modifier * zones[i]['area']
    
    # Apply non-linear scaling
    scaling_factor = len(viable_zones) ** 1.5
    intermediate = base_yield * scaling_factor
    
    # Distractor: unused transformation
    transformed = {name: intermediate / (i+1) for i, name in enumerate(zone_names)}
    
    final = intermediate / 1000
    return int(final)

# Simulate other system checks (dead code path)
current_phase = 'analysis'
if current_phase == 'calibration':
    final_yield = 0
else:
    final_yield = calculate_harvest_efficiency(area_metrics, growth_cycles)

Result: {final_yield}