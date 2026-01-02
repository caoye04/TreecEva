import itertools

def analyze_sensor_array(data_stream):
    # Irrelevant sensor analysis (dead-end function)
    filtered = [x for x in data_stream if x > 0]
    return sum(filtered) // len(filtered) if filtered else 0

def validate_checksum(sequence):
    # Distractor: checksum validation not used in main logic
    return sum(sequence) % 7 == 0

def compute_thermal_output(state, eff):
    base = 0
    for cycle in range(3):
        for phase in state['phases']:
            if phase['active']:
                base += phase['power'] * eff['level']
                # Red herring: modifying unused variable
                phase['diagnostics'] = (phase['power'] + eff['level']) % 11
    # Complex but relevant transformation
    adjustment = len([p for p in state['phases'] if p['active']])
    scaling = eff.get('scaling', 1.0)
    result = base * scaling / (adjustment if adjustment != 0 else 1)
    return int(result)

def monitor_reactor_health(metrics):
    # Decoy function with misleading intermediate calculations
    stress_levels = [m['temp'] ** 0.5 for m in metrics if m['temp'] > 300]
    avg_stress = sum(stress_levels) / len(stress_levels) if stress_levels else 0
    threshold = 25.0
    status = 'STABLE' if avg_stress < threshold else 'CRITICAL'
    # This function does nothing for the final answer
    return status

# Main execution begins
sensor_data = [120, -5, 98, 0, 203, 178, -45]
average_signal = analyze_sensor_array(sensor_data)  # Dead-end computation

checksum_sequence = [1, 3, 2, 5, 4]
is_valid = validate_checksum(checksum_sequence)  # Unused boolean

# Real input structures
reactor_state = {
    'phases': [
        {'power': 125, 'active': True, 'diagnostics': 0},
        {'power': 200, 'active': False, 'diagnostics': 0},
        {'power': 175, 'active': True, 'diagnostics': 0},
        {'power': 90, 'active': True, 'diagnostics': 0}
    ],
    'core_temp': 567.3
}

efficiency_factor = {
    'level': 4,
    'scaling': 1.25,
    'degradation': 0.93
}

# Critical distractor block: complex but irrelevant list processing
metrics_log = [{'temp': 450}, {'temp': 320}, {'temp': 510}]
health_status = monitor_reactor_health(metrics_log)  # No impact on result

# Key computation path buried among distractions
baseline_power = 0
for p in reactor_state['phases']:
    if p['active']:
        baseline_power += p['power']
efficiency_ratio = efficiency_factor['level'] * 0.25
intermediate_yield = baseline_power * efficiency_ratio

# Real target computation
thermal_capacity = compute_thermal_output(reactor_state, efficiency_factor)

# Additional red herring using itertools
combinations = list(itertools.combinations([p['power'] for p in reactor_state['phases'] if p['active']], 2))
mean_combo = sum(sum(c) for c in combinations) / len(combinations) if combinations else 0

# Final output
print(f"Result: {thermal_capacity}")