def calculate_thermal_output(stages):
    base_factor = 1.5
    adjustment = 0.8
    cumulative_heat = 0
    peak_flux = 0
    thermal_capacity = 0

    # Irrelevant initialization (distractor)
    safety_margin = 1.2
    redundancy_check = [0] * len(stages)
    temp_log = []

    for i, stage in enumerate(stages):
        stage_id = i + 1
        heat_input = stage['input'] * base_factor
        loss_factor = stage.get('loss', 0.1)
        net_heat = heat_input * (1 - loss_factor)

        # Conditional branching with string-based mode check
        if stage['mode'] == 'boost':
            net_heat *= 1.4
        elif stage['mode'] == 'eco':
            net_heat *= 0.7

        # Tracking peak flux (semi-relevant but not used in final answer)
        if net_heat > peak_flux:
            peak_flux = net_heat
            active_stage = stage_id  # Distractor variable

        # Update cumulative heat with adjustment
        cumulative_heat += net_heat * adjustment

        # Dead code path (never accessed due to logic)
        if stage_id < 0:
            cumulative_heat -= 10  # Unreachable

        # Logging for debugging (no impact on result)
        temp_log.append(f'Stage {stage_id}: {net_heat:.2f}')

    # Secondary loop using zip (python idiom) - processes auxiliary data
    aux_data = [1.1, 0.9, 1.05]
    correction_sum = 0
    for a, b in zip(stages[:-1], aux_data):
        correction_sum += b * 0.1  # Minor side computation

    # Final calculation - only cumulative_heat matters
    thermal_capacity = int(cumulative_heat + correction_sum)  # Rounded to integer

    # Additional red herring: unused transformation
    final_profile = [x['input'] * 2 for x in stages if x['mode'] != 'eco']

    return thermal_capacity

# Main execution
process_stages = [
    {'input': 50, 'loss': 0.05, 'mode': 'normal'},
    {'input': 70, 'loss': 0.15, 'mode': 'boost'},
    {'input': 60, 'loss': 0.10, 'mode': 'eco'},
    {'input': 80, 'mode': 'normal'}
]

# Key assignment point
thermal_capacity = calculate_thermal_output(process_stages)

print(f"Target result: {thermal_capacity}")