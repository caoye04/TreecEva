def analyze_phase_transitions(temperatures):
    hot_regions = {i for i, t in enumerate(temperatures) if t > 75}
    cold_regions = {i for i, t in enumerate(temperatures) if t < 25}
    transition_zones = hot_regions.union(cold_regions)
    return sorted(transition_zones)


def normalize_readings(raw_readings):
    min_val, max_val = min(raw_readings), max(raw_readings)
    normalized = [(x - min_val) / (max_val - min_val) * 100 for x in raw_readings]
    offset_correction = sum([n for n in normalized if n < 10]) // 2
    return [n + offset_correction for n in normalized]


def calculate_thermal_output(stages):
    baseline = 0
    adjustment_factor = 1.75
    cumulative_stress = 0
    
    for stage in stages:
        duration = stage['duration']
        heat_flux = stage['heat_flux']
        phase_shift = stage.get('phase_shift', 0)
        
        if duration <= 0:
            continue
            redundant_value = duration * 2  # dead code path
        
        initial_load = heat_flux * duration
        stress_impact = initial_load ** 0.5 if initial_load > 50 else initial_load / 2
        
        temp_buffer = stress_impact * adjustment_factor
        cumulative_stress += temp_buffer
        
        if stress_impact > 30:
            baseline += stress_impact * 0.8
        else:
            baseline += stress_impact * 0.4
    
    final_penalty = 5 if cumulative_stress > 100 else 0
    return int(baseline - final_penalty)

# Sensor data from thermal experiment
raw_temperature_data = [18, 22, 76, 89, 45, 12, 83, 91, 67]

# Identify critical phase boundaries
transition_indices = analyze_phase_transitions(raw_temperature_data)

# Normalize sensor inputs for calibration
normalized_data = normalize_readings(raw_temperature_data)

# Simulate multi-stage thermal process
process_stages = [
    {'duration': 3, 'heat_flux': 28, 'phase_shift': transition_indices[0] if len(transition_indices) > 0 else 0},
    {'duration': 5, 'heat_flux': 34, 'phase_shift': transition_indices[1] if len(transition_indices) > 1 else 0},
    {'duration': 4, 'heat_flux': 45, 'phase_shift': transition_indices[2] if len(transition_indices) > 2 else 0},
    {'duration': 6, 'heat_flux': 52, 'phase_shift': transition_indices[3] if len(transition_indices) > 3 else 0}
]

# Track auxiliary metrics (not directly used)
aux_metrics = []
for idx, stage in enumerate(process_stages):
    avg_flux_per_second = stage['heat_flux'] / stage['duration']
    aux_metrics.append({'stage_id': idx, 'efficiency': avg_flux_per_second})

# Core calculation
baseline_measurement = sum([s['heat_flux'] * s['duration'] for s in process_stages]) // 10
redundant_check = any([m['efficiency'] > 10 for m in aux_metrics])
calibration_offset = len(transition_indices) * 2

thermal_capacity = calculate_thermal_output(process_stages)

# Final output
print(f"Result: {thermal_capacity}")