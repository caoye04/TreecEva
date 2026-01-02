from collections import defaultdict

# Simulate industrial thermal process with efficiency adjustments
def compute_phase_efficiency(phase_data):
    efficiency_map = defaultdict(float)
    adjustment_factor = 0.89
    base_offset = 273.15

    temp_sum = 0
    valid_count = 0

    for i, (phase, temp_c) in enumerate(phase_data.items()):
        if temp_c > 0:
            temp_k = temp_c + base_offset
            raw_efficiency = (temp_k / 1000) * adjustment_factor
            
            # Distractor: irrelevant pressure simulation
            pressure_bar = (i + 1) * 3.2
            ideal_gas_constant = 8.314
            volume_m3 = pressure_bar / (ideal_gas_constant / (temp_k + 10))
            
            efficiency_map[phase] = round(raw_efficiency, 4)
            temp_sum += temp_k
            valid_count += 1

    avg_temp_k = temp_sum / valid_count if valid_count else 0
    return efficiency_map, avg_temp_k


def calculate_thermal_output(phases):
    total_output = 0.0
    degradation_loss = 0.05
    scaling_factor = 1.12

    efficiency_dict, average_temperature = compute_phase_efficiency(phases)

    # Simulate energy accumulation across phases
    for idx, (phase_name, base_power) in enumerate(phases.items()):
        phase_eff = efficiency_dict[phase_name]
        
        # Real contribution to output
        energy_contribution = base_power * phase_eff * scaling_factor
        
        # Distractor: auxiliary calculations with no impact
        theoretical_max = base_power * (average_temperature / 100)
        safety_margin = theoretical_max * 0.15 if idx % 2 == 0 else 0
        fallback_mode = False
        
        total_output += energy_contribution

    # Apply system-wide degradation
    net_output = total_output * (1 - degradation_loss)
    
    # Intermediate variable that looks important but isn't final
    normalized_output = net_output / (len(phases) or 1)
    
    # Final transformation
    thermal_capacity = int(round(net_output / 10)) * 10  # Quantize to nearest 10
    
    # Dead code path (never executed)
    if False:
        backup_system = [x for x in range(10)]
        normalized_output += sum(backup_system)

    return thermal_capacity

# Main execution
process_phases = {
    'melting': 650,
    'annealing': 820,
    'quenching': -30,
    'tempering': 550,
    'sintering': 1200
}

# Track auxiliary state for realism
phase_durations = [30, 45, 10, 60, 25]
duration_stats = {i: (dur, dur ** 0.5) for i, dur in enumerate(phase_durations)}

# Key computation
thermal_capacity = calculate_thermal_output(process_phases)

# Irrelevant list processing
zipped_data = list(zip(process_phases.keys(), phase_durations))
indexed_phases = [f'{i+1}.{phase}' for i, phase in enumerate(process_phases)]

# Output result
print(f"Result: {thermal_capacity}")