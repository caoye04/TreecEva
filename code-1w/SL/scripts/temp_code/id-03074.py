def analyze_growth_cycle(conditions):
    # Irrelevant transformation: temperature normalization
    norm_temp = sum([c['temp'] for c in conditions if c['temp'] > 0]) / len(conditions)
    adjusted_ph = [c['ph'] * 1.05 for c in conditions]

    # Distractor: unused nutrient calculation
    total_nutrients = 0
    for cond in conditions:
        if cond['soil_type'] == 'clay':
            total_nutrients += 3
        elif cond['soil_type'] == 'loam':
            total_nutrients += 2
        else:
            total_nutrients += 1

    # Real computation path begins: water retention index
    retention_scores = {}
    for i, c in enumerate(conditions):
        retention_scores[f'day_{i}'] = c['moisture'] * (1 + c['humidity'] / 100)

    # Misleading intermediate: average retention (not used later)
    avg_retention = sum(retention_scores.values()) / len(retention_scores)

    # Key derived metric: flow efficiency using conditional expression
    flow_efficiency = [
        0.8 if c['wind'] > 15 else (0.95 if c['cloud_cover'] < 30 else 0.7)
        for c in conditions
    ]

    # Bit manipulation red herring: cycle masking (unused)
    cycle_mask = 0
    for i in range(len(conditions)):
        cycle_mask ^= (i << 2)

    # Real logic: stress factor accumulation over days
    stress_factor = 0
    for c in conditions:
        if c['temp'] > 35:
            stress_factor += (c['temp'] - 35) * 1.5
        if c['pest_count'] > 5:
            stress_factor += c['pest_count'] * 0.8

    # Critical data structure: flow metrics with dictionary operations
    flow_metrics = {
        'efficiency': sum(flow_efficiency) / len(flow_efficiency),
        'duration': len(conditions),
        'peak_moisture': max(c['moisture'] for c in conditions),
        'decline_phase': any(conditions[i]['moisture'] > conditions[i+1]['moisture'] 
                            for i in range(len(conditions)-1))
    }

    # Conditional expression to determine growth impulse
    growth_impulse = 1.2 if flow_metrics['peak_moisture'] > 60 and not flow_metrics['decline_phase'] else 0.85

    # Hidden decoy function that looks important but isn't called
    def predict_pest_outbreak(data):
        outbreak_risk = 0
        for d in data:
            outbreak_risk += d['temp'] * d['humidity'] * d['pest_count']
        return outbreak_risk / 1000

    # Another distractor: unused recursive function
    def calc_root_depth(depth, day):
        if day == 0 or depth > 50:
            return depth
        return calc_root_depth(depth * 1.1, day - 1)

    return flow_metrics, stress_factor, growth_impulse, norm_temp, adjusted_ph


def calculate_harvest(metrics, stress):
    # Simulate yield based on efficiency and duration
    base_yield = metrics['efficiency'] * metrics['duration'] * 100
    
    # Apply stress penalty using conditional expression
    stress_penalty = 0.7 if stress > 20 else (0.85 if stress > 10 else 1.0)
    
    # Bonus for high moisture peak
    moisture_bonus = 1.1 if metrics['peak_moisture'] >= 70 else 1.0
    
    # Final calculation
    final_yield = base_yield * stress_penalty * moisture_bonus
    
    # Dead code: potential disease adjustment (never reached)
    if False:
        disease_factor = 0.6
        final_yield *= disease_factor
    
    # Red herring: bit shifting that computes irrelevant statistic
    diagnostic_flag = (int(final_yield) >> 4) & 7
    
    return int(final_yield)

# Main execution
climate_data = [
    {'temp': 32, 'humidity': 45, 'moisture': 65, 'wind': 10, 'cloud_cover': 25, 'ph': 6.8, 'soil_type': 'loam', 'pest_count': 3},
    {'temp': 36, 'humidity': 50, 'moisture': 70, 'wind': 8,  'cloud_cover': 40, 'ph': 6.5, 'soil_type': 'clay', 'pest_count': 7},
    {'temp': 38, 'humidity': 40, 'moisture': 60, 'wind': 18, 'cloud_cover': 10, 'ph': 7.0, 'soil_type': 'loam', 'pest_count': 2},
    {'temp': 34, 'humidity': 60, 'moisture': 80, 'wind': 5,  'cloud_cover': 50, 'ph': 6.3, 'soil_type': 'sand', 'pest_count': 8},
    {'temp': 30, 'humidity': 65, 'moisture': 75, 'wind': 12, 'cloud_cover': 30, 'ph': 6.9, 'soil_type': 'clay', 'pest_count': 1}
]

results = analyze_growth_cycle(climate_data)
flow_metrics, stress_index, impulse, _, _ = results
final_yield = calculate_harvest(flow_metrics, stress_index)
print(f"Target result: {final_yield}")