def analyze_soil_quality(data):
    # Irrelevant function: processes soil data but not used in final calculation
    return sum(d * 0.3 for d in data if d > 5)


def monitor_precipitation(levels):
    # Dead code path: never called
    total = 0
    for level in levels:
        if level < 2:
            total += level * 1.5
    return total

# Sensor calibration offset (red herring)
sensor_bias = 0.07
offset_map = {i: i * 0.01 + sensor_bias for i in range(10)}

# Simulated plot data: yield factors per field section
plots = [
    {'id': 'A1', 'base': 120, 'moisture': 8, 'ph': 6.5},
    {'id': 'A2', 'base': 95, 'moisture': 6, 'ph': 5.8},
    {'id': 'B1', 'base': 135, 'moisture': 9, 'ph': 6.9},
    {'id': 'B2', 'base': 110, 'moisture': 7, 'ph': 6.2}
]

# Sensor readings with noise and irrelevant structure
sensors = [
    {'plot': 'A1', 'reading': 118, 'temp': 24, 'noise': 0.05},
    {'plot': 'A2', 'reading': 97, 'temp': 25, 'noise': 0.03},
    {'plot': 'B1', 'reading': 132, 'temp': 23, 'noise': 0.06},
    {'plot': 'B2', 'reading': 109, 'temp': 24, 'noise': 0.04}
]

# Unused transformation: creates decoy data
adjusted_sensors = [
    {**s, 'calibrated': s['reading'] * (1 - offset_map.get(i, 0))}
    for i, s in enumerate(sensors)
]

# Misleading intermediate calculation
baseline_avg = sum(p['base'] for p in plots) / len(plots)
projected_loss = baseline_avg * 0.03  # Not actually used

# Core logic disguised among distractors
def calculate_nutrient_factor(ph_level):
    return 0.8 if ph_level < 6.0 else (1.0 if ph_level <= 6.8 else 0.9)

def calculate_moisture_bonus(moisture):
    return 1.1 if 7 <= moisture <= 9 else 0.95

# Heavily nested and conditional logic path
def calculate_harvest_efficiency(plot_list, sensor_data):
    efficiency_factors = []
    
    # Complex zipped iteration with filtering
    for idx, (p, s) in enumerate(zip(plot_list, sensor_data)):
        # Distractor: unused variables
        debug_id = f"{p['id']}_idx{idx}"
        expected = p['base'] * 0.98
        deviation = abs(s['reading'] - expected)
        
        # Conditional expression (required feature)
        stability_score = 1.0 if deviation < 3 else (0.95 if deviation < 6 else 0.88)
        
        # Key factor computation buried in logic
        nutrient = calculate_nutrient_factor(p['ph'])
        moisture_bonus = calculate_moisture_bonus(p['moisture'])
        
        # Composite efficiency with red herring terms
        raw_yield = p['base'] * nutrient
        adjusted_yield = raw_yield * moisture_bonus
        final_plot_yield = adjusted_yield * stability_score  # This contributes to answer
        
        # Decoy assignment
        if final_plot_yield > 120:
            anomaly_flag = True
        else:
            anomaly_flag = False
        
        efficiency_factors.append(final_plot_yield)
    
    # Final aggregation: average of adjusted yields
    total = sum(efficiency_factors)
    count = len(efficiency_factors)
    
    # Critical result computed here
    result = total / count if count > 0 else 0
    
    # Extra obfuscation: add negligible bias (irrelevant)
    result += sensor_bias * 0.01  # Negligible effect
    
    return result

# Trigger execution
temp_debug_log = [p['id'] for p in plots]  # Dead code

final_yield = calculate_harvest_efficiency(plots, sensors)

# Output requirement
print(f"Result: {final_yield}")