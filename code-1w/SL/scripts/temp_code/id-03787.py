def analyze_signal_transforms(frequency_data, phase_offsets):
    cumulative_power = 0
    temp_amplitude = 0
    total_cycles = 0
    rotation_sum = 0
    correction_factor = 1.5
    baseline_adjustment = 0
    intermediate_results = []
    
    for idx, (freq, phase) in enumerate(zip(frequency_data, phase_offsets)):
        if freq <= 0:
            continue
            unused_path = freq * 2  # Dead code path (unreachable)

        cycle_count = int(freq * 0.1)
        total_cycles += cycle_count
        
        # Irrelevant amplitude calculation (distractor)
        temp_amplitude = (freq ** 0.5) * correction_factor
        cumulative_power += temp_amplitude ** 2
        
        # Relevant phase logic
        shifted_phase = (phase + 90) % 360
        if shifted_phase > 180:
            shifted_phase -= 360
        
        # Accumulate weighted rotation
        rotation_contribution = shifted_phase * cycle_count
        rotation_sum += rotation_contribution
        
        # Store intermediate (not used later)
        intermediate_results.append((idx, shifted_phase))

    # Extra distraction: unused normalization
    if total_cycles > 0:
        average_power = cumulative_power / total_cycles
        normalized_power = round(average_power, 2)
    else:
        average_power = 0

    # Additional red herring variable
    baseline_adjustment = sum(p for p in phase_offsets if p < 0)

    # Core computation chain
    base_rotation = rotation_sum
    adjustment_offset = len(frequency_data) * 15
    final_rotation = base_rotation + adjustment_offset
    
    # Key execution point
    net_phase_shift = final_rotation % 360
    
    print(f"Result: {net_phase_shift}")
    return net_phase_shift

# Input data
freq_input = [50, 60, 0, 120, 25]
phase_input = [45, -30, 90, 180, -90]

result = analyze_signal_transforms(freq_input, phase_input)