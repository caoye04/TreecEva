def calculate_thermal_output(stages):
    base_factor = 1.75
    adjustment = 0.92
    cumulative_heat = 0
    peak_moment = None
    decay_rate = 0.98
    temp_buffer = []

    for i, stage in enumerate(stages):
        if stage['type'] == 'heating':
            energy_input = stage['duration'] * stage['intensity']
            efficiency = stage.get('efficiency', 0.85)
            heat_contribution = energy_input * efficiency
            
            # Conditional expression to cap excessive contributions
            heat_contribution = heat_contribution if heat_contribution < 150 else 150 * (efficiency ** 0.5)
            
            cumulative_heat += heat_contribution
            
            # Irrelevant tracking - distractor
            temp_buffer.append(energy_input * adjustment)
        
        elif stage['type'] == 'cooling':
            reduction = stage['duration'] * 0.77
            cumulative_heat = max(0, cumulative_heat - reduction)

        # Simulate intermediate monitoring (distractor logic)
        monitor_flag = 'critical' if cumulative_heat > 100 else 'stable'
        status_log = f"Stage {i}: {monitor_flag} at {cumulative_heat:.2f}"

    # Set peak moment (not used in final result)
    if temp_buffer:
        peak_moment = max(temp_buffer) * decay_rate

    # Actual calculation with list comprehension and set operation
    valid_stages = [s for s in stages if s['intensity'] > 1]
    unique_durations = list(set([s['duration'] for s in valid_stages]))
    duration_score = sum([round(d * base_factor) for d in unique_durations])

    # Final output influenced by both cumulative heat and structural score
    final_adjustment = duration_score * 0.3
    return int(cumulative_heat + final_adjustment)

# Simulation data
process_stages = [
    {'type': 'heating', 'duration': 12, 'intensity': 2.1, 'efficiency': 0.88},
    {'type': 'heating', 'duration': 8, 'intensity': 1.5, 'efficiency': 0.82},
    {'type': 'cooling', 'duration': 5, 'intensity': 0},
    {'type': 'heating', 'duration': 15, 'intensity': 2.3, 'efficiency': 0.91},
    {'type': 'cooling', 'duration': 3, 'intensity': 0}
]

initial_volume = 450  # irrelevant parameter
baseline_offset = 12  # unused constant
reference_modes = {'static': 1, 'dynamic': 2, 'hybrid': 3}  # dead data structure

thermal_capacity = 0
thermal_capacity = calculate_thermal_output(process_stages)
print(f"Result: {thermal_capacity}")