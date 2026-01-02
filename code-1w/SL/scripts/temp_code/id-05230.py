def analyze_component_health(health_log, threshold):
    cumulative_score = 0
    peak_stress = -1
    stress_events = []
    temp_buffer = []
    for entry in health_log:
        if 'stress_level' in entry:
            stress = entry['stress_level']
            temp_buffer.append(stress * 0.85)  # Irrelevant transformation
            if stress > threshold:
                stress_events.append(stress)
                cumulative_score += stress // 2
    if len(stress_events) > 3:
        return sum(stress_events) // len(stress_events)
    return cumulative_score // 2 if cumulative_score else 0

# Distractor function - never called
def compute_residual_load(inputs, factor=1.3):
    total = 0
    for x in inputs:
        total += (x ** 0.5) * factor
    adjustment = total % 7
    return int(total - adjustment)

# Another decoy: irrelevant data structure
maintenance_schedule = {
    'calibration': {'interval_days': 14, 'priority': 'high'},
    'diagnostics': {'interval_days': 7, 'priority': 'critical'},
    'backup': {'interval_days': 1, 'priority': 'low'}
}

# System monitoring simulation
log_data = [
    {'timestamp': 1001, 'stress_level': 42, 'temp': 67},
    {'timestamp': 1002, 'stress_level': 55, 'temp': 70},
    {'timestamp': 1003, 'stress_level': 61, 'temp': 72},
    {'timestamp': 1004, 'stress_level': 49, 'temp': 69},
    {'timestamp': 1005, 'stress_level': 73, 'temp': 75},
    {'timestamp': 1006, 'stress_level': 58, 'temp': 71}
]

system_thresholds = {
    'stress_baseline': 50,
    'recovery_delay': 3,
    'tolerance_window': 5
}

# Unused intermediate calculations - red herrings
baseline = system_thresholds['stress_baseline']
window = system_thresholds['tolerance_window']
adjusted_baseline = baseline * (1 + window / 100)  # Looks important, unused

# Complex-looking but irrelevant dictionary operations
summary_stats = {}
for key in ['a', 'b', 'c']:
    summary_stats[key] = {sub: 0 for sub in ['x', 'y']}
    summary_stats[key]['z'] = [i * 2 for i in range(3)]  # Dead code path

# Real processing begins here
aggregated_diagnostics = []
for i, record in enumerate(log_data):
    if record['stress_level'] > system_thresholds['stress_baseline']:
        adjusted_value = (record['stress_level'] - baseline) ** 2
        if i > 0:
            prev_stress = log_data[i-1]['stress_level']
            decay_factor = 0.9 if prev_stress > baseline else 1.1
            adjusted_value = int(adjusted_value * decay_factor)
        aggregated_diagnostics.append(adjusted_value)

# Simulate conditional early exit - not triggered
if len(aggregated_diagnostics) < 2:
    final_diagnostic = -999
    print(f"Result: {final_diagnostic}")
else:
    # Core logic embedded here
    raw_total = sum(aggregated_diagnostics)
    count_above = len([v for v in log_data if v['stress_level'] > system_thresholds['stress_baseline']])
    
    # Actual answer computation disguised among distractions
    scaling_factor = 0.75 if count_above >= 4 else 1.25
    preliminary = raw_total * scaling_factor
    
    # Decoy control flow
    mode_flag = 'enhanced' if preliminary > 1000 else 'standard'
    correction_offset = 17 if mode_flag == 'enhanced' else 0
    
    # Final calculation - only this matters
    final_diagnostic = int(preliminary - correction_offset)

    # Additional irrelevant bit manipulation
    mask = 0b1101
    masked_result = final_diagnostic & mask
    _ = [masked_result << i for i in range(4)]  # Unused list comprehension

    # Print required result
    print(f"Target result: {final_diagnostic}")