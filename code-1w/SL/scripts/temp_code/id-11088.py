from itertools import cycle

def simulate_reaction_stage(energy_input, stage_config):
    activation_threshold = stage_config['threshold']
    efficiency_ratio = stage_config['efficiency']
    intermediate_signal = (energy_input * 0.87) + 1.5
    noise_floor = 0.02 * energy_input
    adjusted_input = max(intermediate_signal - noise_floor, activation_threshold)
    return (adjusted_input * efficiency_ratio) % 97

def evaluate_stability_metric(state_log):
    cumulative_drift = 0
    for i in range(len(state_log) - 1):
        cumulative_drift += abs(state_log[i+1] - state_log[i])
    penalty_factor = 0.1 if cumulative_drift > 50 else 0.05
    return cumulative_drift * penalty_factor

def calculate_thermal_output(sequence):
    base_temperatures = [320, 345, 370, 335, 355]
    modulation_sequence = cycle([1.05, 0.98, 1.12])
    processed_phases = []
    temp_offset_tracker = []
    
    for idx, op_code in enumerate(sequence):
        config = {
            'threshold': 65 + (idx % 4) * 5,
            'efficiency': 0.78 + (idx * 0.01) % 0.2
        }
        
        raw_energy = base_temperatures[idx % len(base_temperatures)]
        modulated_energy = raw_energy * next(modulation_sequence)
        
        # Irrelevant signal processing branch (dead-end computation)
        if idx % 4 == 0:
            dummy_signal = sum([modulated_energy / (i+1) for i in range(1, 4)])
            smoothing_factor = dummy_signal * 0.01
            adjusted_dummy = smoothing_factor ** 2
        
        stage_output = simulate_reaction_stage(modulated_energy, config)
        processed_phases.append(stage_output)
        
        # Tracking variable not used in final result
        temp_offset_tracker.append(abs(modulated_energy - raw_energy))
    
    # Secondary analysis with partial relevance
    stability_score = evaluate_stability_metric(processed_phases)
    
    # Core accumulation logic (key path)
    total_accum = 0
    for val in processed_phases:
        if val > 70:
            total_accum += val * 0.6
        elif val > 50:
            total_accum += val * 0.4
        else:
            total_accum += val * 0.2
    
    # Final transformation
    thermal_capacity = int((total_accum - stability_score) // 1.8)
    
    # Red herring: unused complex calculation
    final_diagnostic = sum([x**2 for x in temp_offset_tracker]) / (len(temp_offset_tracker) or 1)
    
    return thermal_capacity

# Execution sequence
process_sequence = [1, 0, 1, 1, 0, 1, 0, 0]
thermal_capacity = calculate_thermal_output(process_sequence)
print(f"Result: {thermal_capacity}")