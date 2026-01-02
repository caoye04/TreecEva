def analyze_crop_performance(data):
    total_yield = 0
    adjustments = []
    for record in data:
        base = record['yield'] * 0.9
        if record['pest_exposure']:
            base *= 0.85
        season_factor = 1.1 if 'spring' in record['season'].lower() else 0.95
        adjusted = base * season_factor
        adjustments.append(adjusted)
        total_yield += adjusted
    return total_yield

area_metrics = [120, 85, 95, 110]
growth_cycles = [
    {'yield': 200, 'pest_exposure': True, 'season': 'Spring'},
    {'yield': 180, 'pest_exposure': False, 'season': 'Summer'},
    {'yield': 195, 'pest_exposure': True, 'season': 'Fall'},
    {'yield': 210, 'pest_exposure': False, 'season': 'Spring'}
]

# Irrelevant preprocessing: string manipulation on season names
temp_names = [cycle['season'].upper().replace('N', 'n') for cycle in growth_cycles]
processed_names = [name[::-1] for name in temp_names if len(name) > 5]

# Dummy accumulation with slicing distraction
dummy_sum = sum([len(name) for name in processed_names])
dummy_slice = processed_names[1:3]

# Core logic obscured by wrapper
initial_projection = sum(area_metrics) * 1.5
deferred_values = [initial_projection / (i+1) for i in range(4)]

# Key function with mixed operations
def calculate_harvest_efficiency(areas, cycles):
    efficiency = 0
    for i, area in enumerate(areas):
        modifier = 0.1 * (i % 2)
        raw_yield = cycles[i]['yield']
        pest_penalty = 0.15 if cycles[i]['pest_exposure'] else 0
        season_mod = 1.1 if 'spring' in cycles[i]['season'].lower() else 0.9
        # Actual contribution
        efficiency += (raw_yield * season_mod * (1 - pest_penalty) + area * 0.01) - modifier
    return round(efficiency, 4)

interim_result = analyze_crop_performance(growth_cycles)
baseline_check = interim_result > 500  # boolean distractor

final_yield = calculate_harvest_efficiency(area_metrics, growth_cycles)
print(f"Result: {final_yield}")