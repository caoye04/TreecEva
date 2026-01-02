def calculate_thermal_output(sequence):
    base_yield = 23.5
    modifier = 1.75
    transient_loss = 0.05
    thermal_capacity = 0
    
    # Simulate multi-stage industrial process
    for stage in sequence:
        if stage['type'] == 'heating':
            base_yield += stage['duration'] * modifier
        elif stage['type'] == 'cooling' and stage['efficiency'] > 0.7:
            base_yield -= transient_loss * stage['duration']
    
    # Distractor: Chemical stability check (unused)
    stability_ratio = 0
    for stage in sequence:
        if 'catalyst' in stage:
            stability_ratio += len(stage['catalyst'])
    adjustment_factor = stability_ratio / max(len(sequence), 1)
    dummy_metric = base_yield * adjustment_factor if adjustment_factor > 0.1 else 0
    
    # Real computation path
    efficiency_flags = [s.get('monitor', False) for s in sequence]
    active_monitoring = sum(efficiency_flags)
    
    # Conditional expression with string method distraction
    mode_label = ('high' if active_monitoring > 2 else 'low').upper()
    mode_penalty = 2.0 if 'HIGH' in mode_label else 0.5
    
    # Final capacity calculation
    thermal_capacity = int(base_yield - mode_penalty)
    
    # Dead code path - misleading post-processing
    if thermal_capacity < 0:
        status = "FAILED"
        error_log = f"Error: Negative capacity {thermal_capacity}"
    else:
        status = "OK"
        temp_buffer = [thermal_capacity * 0.1 for _ in range(3)]  # unused
    
    return thermal_capacity

# Process configuration data
process_stages = [
    {'type': 'heating', 'duration': 4, 'monitor': True},
    {'type': 'heating', 'duration': 3, 'monitor': True, 'catalyst': 'Z7'},
    {'type': 'cooling', 'duration': 2, 'efficiency': 0.85, 'monitor': False},
    {'type': 'heating', 'duration': 5, 'monitor': True, 'catalyst': 'X9'},
    {'type': 'cooling', 'duration': 1, 'efficiency': 0.92}
]

# Key execution point
thermal_capacity = calculate_thermal_output(process_stages)
print(f"Result: {thermal_capacity}")