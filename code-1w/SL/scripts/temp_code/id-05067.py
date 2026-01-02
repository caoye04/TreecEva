from itertools import cycle

# Simulate agricultural yield optimization with environmental constraints
def calculate_base_yield(area, fertility_index):
    return int(area * fertility_index * 0.85)

def apply_seasonal_modifiers(base_yield, season):
    modifiers = {'spring': 1.2, 'summer': 1.1, 'autumn': 0.9, 'winter': 0.6}
    return int(base_yield * modifiers.get(season, 1.0))

def filter_viable_cycles(yield_sequence, threshold=250):
    return [y for y in yield_sequence if y > threshold]

def compute_growth_ratio(seq):
    if len(seq) < 2:
        return 1.0
    return round(seq[-1] / seq[0], 4)

def harvest_results(cycles):
    cumulative = 0
    growth_trend = []
    peak_analysis = []  # Distractor: collected but not used
    
    for i, cycle in enumerate(cycles):
        raw_yield = calculate_base_yield(cycle['area'], cycle['fertility'])
        adjusted_yield = apply_seasonal_modifiers(raw_yield, cycle['season'])
        
        # Irrelevant transformation (distractor)
        normalized = adjusted_yield / (cycle['area'] + 1)
        efficiency_score = normalized * 0.95  # Dead computation
        
        cumulative += adjusted_yield
        growth_trend.append(adjusted_yield)
        
        # Misleading conditional that doesn't affect final result
        if adjusted_yield > 300:
            peak_analysis.append({'cycle': i, 'value': adjusted_yield})

    # Semi-relevant processing: analyze trend but only use ratio
    trend_ratio = compute_growth_ratio(growth_trend)
    baseline_projection = growth_trend[0] * len(cycles)
    
    # Actual key computation
    final_yield = cumulative // len(cycles)
    
    # Extra unrelated calculation (distractor)
    projected_loss = baseline_projection - cumulative
    stability_index = round(trend_ratio * 100, 2)
    
    return final_yield

# Experimental field data
field_configurations = [
    {'area': 120, 'fertility': 2.3, 'season': 'spring'},
    {'area': 110, 'fertility': 2.5, 'season': 'summer'},
    {'area': 130, 'fertility': 2.1, 'season': 'spring'},
    {'area': 125, 'fertility': 2.4, 'season': 'summer'},
    {'area': 115, 'fertility': 2.6, 'season': 'autumn'}
]

# Generate production cycles using itertools.cycle (slicing and iteration)
rotation_pattern = list(itertools.islice(cycle(field_configurations), 0, 7))  # Extended to 7 via cycling

# Minor irrelevant filtering
valid_rotations = [r for r in rotation_pattern if r['fertility'] > 2.2]
production_cycles = valid_rotations[:len(valid_rotations)]  # Redundant slicing

# Key execution point
final_yield = harvest_results(production_cycles)
print(f"Result: {final_yield}")