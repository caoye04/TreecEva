def analyze_growth_conditions(conditions):
    growth_score = 0
    for temp, moisture in zip(conditions['temperature'], conditions['moisture']):
        if temp > 25 and moisture > 60:
            growth_score += 2
        elif temp > 20 and moisture > 40:
            growth_score += 1
    return growth_score

# Simulate redundant preprocessing
raw_metrics = {
    'temp_readings': [22, 27, 19, 30],
    'moisture_levels': [45, 70, 35, 80],
    'light_exposure': [12, 10, 14, 9]
}

# Irrelevant transformation (distractor)
normalized_light = [round(l / max(raw_metrics['light_exposure']), 2) for l in raw_metrics['light_exposure']]

# Misleading intermediate calculation
baseline_adjustment = sum(normalized_light) * 0.5

sensor_data = [
    {'t': 22, 'm': 45, 'l': 12},
    {'t': 27, 'm': 70, 'l': 10},
    {'t': 19, 'm': 35, 'l': 14},
    {'t': 30, 'm': 80, 'l': 9}
]

thresholds = {
    'high_yield': {'min_temp': 25, 'min_moist': 60},
    'medium_yield': {'min_temp': 20, 'min_moist': 40}
}

# Unused but plausible helper function (dead code path)
def predict_harvest_date(days_left):
    return days_left * 0.75

# Core logic obscured by structure
def calculate_optimal_yield(data, limits):
    high_count = 0
    medium_count = 0
    
    for i, entry in enumerate(data):
        temp = entry['t']
        moist = entry['m']
        
        # Simulated sensor validation (partly irrelevant)
        if temp < 0 or moist < 0:
            continue
            
        if temp >= limits['high_yield']['min_temp'] and moist >= limits['high_yield']['min_moist']:
            high_count += 1
        elif temp >= limits['medium_yield']['min_temp'] and moist >= limits['medium_yield']['min_moist']:
            medium_count += 1
    
    # Complex-looking but straightforward yield formula
    base_yield = 150 * high_count + 75 * medium_count
    adjustment_factor = 0.1 * len([x for x in data if x['l'] > 10])  # Light-based tweak
    volatility_penalty = 0
    
    # Simulated stability check (semi-relevant)
    temps = [e['t'] for e in data]
    if max(temps) - min(temps) > 10:
        volatility_penalty = 20
    
    final_yield = base_yield - volatility_penalty + (adjustment_factor * 10)
    return int(final_yield)

# Execute key statement
final_yield = calculate_optimal_yield(sensor_data, thresholds)

# Print result as required
print(f"Result: {final_yield}")