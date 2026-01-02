def analyze_growth_pattern(sequence):
    if len(sequence) < 3:
        return 0
    count = 0
    for i in range(1, len(sequence) - 1):
        if sequence[i-1] < sequence[i] > sequence[i+1]:
            count += 1
    return count

# Irrelevant helper function (decoy)
def compute_nutrient_index(plant_data):
    total = 0
    for item in plant_data:
        if item % 4 == 0:
            total += item * 0.3
    return total + 11.5  # misleading constant

# Unused transformation map (distractor)
nutrient_map = {i: (i**2 + 3*i) // 2 for i in range(1, 20)}

# Simulated environmental readings (mostly irrelevant)
sensor_readings = [127, 83, 91, 104, 76, 133, 145, 67]
adjusted_readings = [r // 2 for r in sensor_readings if r > 80]

# Core data structure with meaningful and noise elements
area_metrics = {
    'plots': [
        {'id': 'A1', 'size': 12, 'crop': 'wheat', 'yield_base': 4.2, 'conditions': [3, 1, 4]},
        {'id': 'B2', 'size': 8, 'crop': 'corn', 'yield_base': 3.8, 'conditions': [1, 5, 2]},
        {'id': 'C3', 'size': 15, 'crop': 'wheat', 'yield_base': 5.1, 'conditions': [4, 4, 3]},
        {'id': 'D4', 'size': 10, 'crop': 'barley', 'yield_base': 3.5, 'conditions': [2, 3, 5]}
    ],
    'soil_health': [78, 85, 72, 90],
    'rainfall': [120, 110, 135, 100],  # unused field
    'temperature_avg': 22.5  # decoy scalar
}

# Fake optimization pass (dead code path)
def optimize_layout(areas):
    sorted_areas = sorted(areas['plots'], key=lambda x: x['size'], reverse=True)
    score = 0
    for plot in sorted_areas:
        score += len(plot['crop']) * plot['size']
    return score // 10

# Unused but plausible-looking computation
baseline_score = optimize_layout(area_metrics)

# Actual logic buried among distractions
def calculate_harvest_efficiency(farm_data):
    efficiency_factors = []
    
    # Real processing: assess each plot's condition peaks
    for plot in farm_data['plots']:
        peak_stress = analyze_growth_pattern(plot['conditions'])
        adjusted_yield = plot['yield_base'] * (1 + (plot['size'] / 100))
        if plot['crop'] == 'wheat':
            adjusted_yield *= 1.15  # wheat bonus
        efficiency_factors.append(adjusted_yield - 0.3 * peak_stress)
    
    # Aggregate using list comprehension (core relevant step)
    normalized = [val * 100 for val in efficiency_factors]
    
    # Apply soil health weighting (only first four plots matter)
    total = 0
    for i in range(len(normalized)):
        total += normalized[i] * (farm_data['soil_health'][i] / 80)
    
    # Final adjustment based on size distribution entropy (combinatorics flavor)
    sizes = [p['size'] for p in farm_data['plots']]
    avg_size = sum(sizes) / len(sizes)
    variance_ratio = sum((s - avg_size)**2 for s in sizes) / (avg_size ** 2)
    
    return int(total - (variance_ratio * 50))

# Critical execution point
final_yield = calculate_harvest_efficiency(area_metrics)

# Red herring: fake reporting function
report_data = []
for entry in area_metrics['plots']:
    report_data.append({
        'ref': entry['id'],
        'value': (entry['size'] * entry['yield_base']) % 7
    })

# Only this output matters
print(f"Target result: {final_yield}")