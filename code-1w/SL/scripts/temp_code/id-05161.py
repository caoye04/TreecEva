def analyze_growth_cycle(data):
    total_cycles = len(data)
    growth_rates = []
    for i, cycle in enumerate(data):
        rate = (cycle['end'] - cycle['start']) / cycle['duration']
        growth_rates.append(rate)
    avg_rate = sum(growth_rates) / len(growth_rates)
    return avg_rate

sensors = [
    {'id': 'A1', 'calibrated': True, 'readings': [23, 25, 22, 24]},
    {'id': 'B2', 'calibrated': False, 'readings': [19, 20, None, 21]},
    {'id': 'C3', 'calibrated': True, 'readings': [31, 33, 30, 32]}
]

plots = [
    {'soil': 'clay', 'moisture': 0.45, 'temp': 22, 'crop': 'wheat'},
    {'soil': 'loam', 'moisture': 0.65, 'temp': 24, 'crop': 'corn'},
    {'soil': 'sand', 'moisture': 0.35, 'temp': 26, 'crop': 'sorghum'}
]

# Irrelevant preprocessing: filter only calibrated sensors
valid_sensors = [s for s in sensors if s['calibrated']]

# Misleading data transformation
adjusted_readings = []
for s in valid_sensors:
    clean = [r for r in s['readings'] if r is not None]
    adjusted_readings.extend([r * 1.05 for r in clean])

# Dummy statistic
avg_adjusted = sum(adjusted_readings) / len(adjusted_readings) if adjusted_readings else 0

# Simulate growth cycles from plot moisture and temp
simulated_cycles = []
for p in plots:
    base = p['moisture'] * 100
    change = p['temp'] * 0.5
    simulated_cycles.append({
        'start': base,
        'end': base + change,
        'duration': 7
    })

# Use enumerate and zip as required
indexed_plots = list(enumerate(plots))
growth_data = analyze_growth_cycle(simulated_cycles)

# Secondary irrelevant calculation: character counting in crop names
total_chars = 0
for i, plot in indexed_plots:
    total_chars += len(plot['crop'])

# Main logic disguised among distractions
def calculate_harvest_efficiency(plot_list, sensor_list):
    efficiency = 0
    for idx, p in enumerate(plot_list):
        # Key formula: weighted combination
        moisture_factor = max(p['moisture'], 0.3)
        temp_factor = min(abs(p['temp'] - 25), 5)
        crop_weight = {'wheat': 1.2, 'corn': 1.5, 'sorghum': 1.1}.get(p['crop'], 1.0)
        
        # Real contribution to answer
        step_yield = (moisture_factor * 80) - (temp_factor * 4) + (idx * 2)
        efficiency += step_yield * crop_weight
    
    # Normalization using unrelated sensor count
    calibration_count = len([s for s in sensor_list if s['calibrated']])
    normalized = efficiency / (calibration_count if calibration_count else 1)
    
    # Add subtle influence from character count (semi-relevant)
    adjustment = total_chars * 0.1
    return normalized + adjustment

# Execute main computation
temp_tracker = [p['temp'] for p in plots]
moisture_snapshot = {i: p['moisture'] for i, p in indexed_plots}

# Critical statement
final_yield = calculate_harvest_efficiency(plots, sensors)

print(f"Result: {final_yield}")