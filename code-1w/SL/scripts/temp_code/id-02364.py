def calculate_thermal_capacity(stages):
    base_multiplier = 1.5
    adjustment_factor = 0.85
    thermal_capacity = 0
    peak_flux = 0
    transient_loss = 0.0

    for i, (temp, duration, phase) in enumerate(stages):
        if temp > 400:
            saturation_point = temp * 0.1
            transient_loss += saturation_point * 0.05

        # Irrelevant computation - distractor
        dummy_calc = (i + 1) * duration ** 0.5
        efficiency_modifier = 1.0

        if phase == 'cooling':
            efficiency_modifier = 0.9
        elif phase == 'heating':
            efficiency_modifier = 1.1

        # Main contribution to thermal capacity
        stage_contribution = temp * duration * base_multiplier * efficiency_modifier
        thermal_capacity += stage_contribution

        # Tracking peak flux (not used in final answer)
        if stage_contribution > peak_flux:
            peak_flux = stage_contribution

        # Early termination if excessive heat
        if temp > 600 and duration > 50:
            break

    # Final adjustment with no effect on logic
    safety_margin = 1.02
    return int(thermal_capacity // 100 * safety_margin)


# Simulated industrial thermal process stages
process_stages = [
    (300, 20, 'initial'),
    (450, 35, 'heating'),
    (520, 40, 'transition'),
    (480, 50, 'cooling'),
    (550, 30, 'heating')
]

# Auxiliary variables - irrelevant
system_voltage = 220
coolant_level = 78.5
maintenance_interval = 150

thermal_capacity = 0

# Key execution point
thermal_capacity = calculate_thermal_capacity(process_stages)

# Output result
print(f"Result: {thermal_capacity}")