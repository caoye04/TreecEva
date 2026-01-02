from collections import defaultdict

# Simulate agricultural yield prediction with noise filtering and state tracking
def analyze_growth_patterns(data, threshold=0.65):
    counts = defaultdict(int)
    trend_flags = [False] * len(data)
    cumulative_shift = 0
    
    for i, (phase, val) in enumerate(data.items()):
        if val['moisture'] > threshold:
            counts['optimal'] += 1
            trend_flags[i] = True
        else:
            counts['suboptimal'] += 1
            
        # Bitwise phase marker (irrelevant to final result)
        _ = (i ^ val['temp']) & 3
    
    return dict(counts), trend_flags

def normalize_readings(raw_values):
    # Normalize sensor inputs (some are distractors)
    base_norm = sum(raw_values) / len(raw_values)
    adjusted = [(x - base_norm) * 1.1 for x in raw_values]
    outlier_count = 0
    
    for v in adjusted:
        if abs(v) > 2.0:  # Threshold filter
            outlier_count += 1
    
    # Return only base_norm as it's used later
    scaling_factor = 1.0 + (outlier_count * 0.01)  # Not actually used
    return base_norm

def calculate_harvest_efficiency(areas, cycles):
    efficiency_log = []
    total_adjustment = 0.0
    
    for idx, (zone, metrics) in enumerate(areas.items()):
        base_area = metrics['size']
        hydration = metrics['water_stress']
        pest_level = metrics.get('pest_incidence', 0)
        
        # Real computation branch
        if hydration < 0.5:
            score = base_area * (1.5 - hydration)
        else:
            score = base_area * 0.8
        
        # Distractor: complex pest adjustment that isn't applied due to policy_override
        policy_override = False
        if pest_level > 3:
            potential_penalty = pest_level * 0.15
            temp_adj = score * (1 - potential_penalty)
            total_adjustment += temp_adj  # Dead accumulation
        
        efficiency_log.append(score)
    
    # Core logic: combine with cycle data
    cycle_influence = 0
    for cycle in cycles:
        stage_weight = cycle['maturity'] / 10.0
        health_boost = int(cycle['health'] > 7)  # Early return effect
        cycle_influence += stage_weight + 0.3 * health_boost
    
    final_yield = int(sum(efficiency_log) * (1 + cycle_influence * 0.1))
    
    # Irrelevant string processing (red herring)
    status_msg = "Harvest viable" if final_yield > 300 else "Marginal yield"
    char_count = {char: status_msg.count(char) for char in set(status_msg)}
    _ = ''.join(sorted(char_count.keys()))
    
    return final_yield

# --- Simulation Setup ---
area_metrics = {
    'north_field': {'size': 80, 'water_stress': 0.45, 'pest_incidence': 5},
    'east_ridge': {'size': 95, 'water_stress': 0.70},
    'west_plot': {'size': 60, 'water_stress': 0.35, 'pest_incidence': 2}
}

growth_cycles = [
    {'maturity': 8, 'health': 9},
    {'maturity': 6, 'health': 5},
    {'maturity': 9, 'health': 8}
]

# Preprocessing step with side distraction
raw_sensor_data = [0.67, 0.54, 0.72, 0.81, 0.43]
normalization_bias = normalize_readings(raw_sensor_data)

# Main analysis (trend not used in final calculation)
growth_trends, flags = analyze_growth_patterns({
    f'phase_{i}': {'moisture': x, 'temp': i*5+20} for i, x in enumerate([0.7, 0.68, 0.75, 0.62])
})

# Critical execution point
final_yield = calculate_harvest_efficiency(area_metrics, growth_cycles)

print(f"Result: {final_yield}")