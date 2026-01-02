def calculate_thermal_output(stages):
    base_multiplier = 1.75
    adjustment_factor = 0.89
    thermal_capacity = 0
    stage_weights = {key: (idx + 1) * 0.5 for idx, key in enumerate(stages)}
    
    # Irrelevant signal processing simulation
    signal_buffer = [0] * len(stages)
    for i in range(len(stages)):
        if i % 2 == 0:
            signal_buffer[i] = (i + 1) * 1.3
        else:
            signal_buffer[i] = (i + 1) * 0.7
    
    # Real computation path
    temp_offset = sum([len(key) for key in stages.keys()])
    efficiency_log = []
    for idx, (key, value) in enumerate(stages.items()):
        raw_score = value * (idx + 1)
        adjusted_score = raw_score * stage_weights[key]
        if adjusted_score > 10:
            adjusted_score *= adjustment_factor
        efficiency_log.append(adjusted_score)
    
    # Secondary distraction: network latency mockup
    latency_map = dict(zip(stages.keys(), [0.12 * v for v in stages.values()]))
    total_latency = sum(latency_map.values())
    penalty_rate = total_latency * 0.05 if total_latency > 0.5 else 0
    
    # Final calculation chain
    base_energy = sum(efficiency_log) * base_multiplier
    fluctuation_correction = abs(base_energy * 0.03 * (-1)**len(efficiency_log))
    thermal_capacity = int(base_energy - fluctuation_correction - penalty_rate * 100)
    
    return thermal_capacity

# Main execution context
process_stages = {
    'initiation': 6,
    'propagation': 8,
    'saturation': 5,
    'termination': 9
}

# Dead code branch - misleading state tracking
status_registry = {}
for phase in process_stages:
    status_registry[phase] = 'completed'

aux_data = [[i*j for j in range(3)] for i in range(4)]  # Unused list comprehension

thermal_capacity = 0
previous_mode = "standby"

if len(process_stages) > 3:
    mode = "turbo"
    calibration_sequence = list(enumerate(['a','b','c']))  # Unused
    thermal_capacity = calculate_thermal_output(process_stages)
    recovery_state = [x for x, _ in calibration_sequence]  # Unused

print(f"Result: {thermal_capacity}")