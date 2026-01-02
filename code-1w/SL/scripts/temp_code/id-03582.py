from itertools import cycle

# Simulate thermal dynamics in a multi-phase industrial heater
def calculate_thermal_output(energy_input, efficiency):
    total_phases = len(energy_input)
    phase_results = [0] * total_phases
    temp_buffer = []
    
    for idx, (power, eff) in enumerate(zip(energy_input, efficiency)):
        raw_heat = power * eff
        adjusted_heat = raw_heat * 0.95  # heat loss factor
        
        # Simulate fluctuating ambient absorption
        ambient_offset = 0
        for j in range(3):
            ambient_offset += (idx + j) % 4
        ambient_absorption = ambient_offset / 10.0
        
        final_heat = adjusted_heat + ambient_absorption
        
        # Track intermediate states (not all used)
        temp_buffer.append(final_heat * 0.1)
        
        if idx > 0 and final_heat < phase_results[idx-1]:
            phase_results[idx] = phase_results[idx-1] * 0.9
        else:
            phase_results[idx] = final_heat
    
    # Misleading secondary calculation (distractor)
    avg_temp = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0
    stability_score = avg_temp * 0.25
    
    # Final aggregation
    return int(sum(phase_results))

# Input data
energy_levels = [120, 135, 110, 145, 130]
efficiency_rates = [0.88, 0.91, 0.85, 0.93, 0.89]

# Red herring variables
baseline_reference = 0
calibration_factor = None
status_log = []

for step in range(len(energy_levels)):
    baseline_reference += (step * 2) % 7
    calibration_factor = baseline_reference * 0.01
    status_log.append(f'Step {step}: Ref={baseline_reference}')

# Core computation
thermal_capacity = calculate_thermal_output(energy_levels, efficiency_rates)

# Print result as required
print(f"Result: {thermal_capacity}")