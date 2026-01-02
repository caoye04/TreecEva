def calculate_thermal_output(buffer, shift):
    base = sum([b % 7 for b in buffer if b > 0])
    offset = len(buffer) // 2
    shifted_vals = [buffer[(i + shift) % len(buffer)] for i in range(len(buffer))]
    
    # Irrelevant signal processing (distractor)
    signal_peak = max(shifted_vals) * 0.85
    normalized = [val / (signal_peak + 1e-5) for val in shifted_vals]
    entropy_score = 0
    for v in normalized:
        if v > 0.5:
            entropy_score += 1
    
    # Semi-relevant transformation
    adjusted = [x * 1.1 for x in buffer][::-1]
    mirror_sum = sum(adjusted[:len(adjusted)//2])
    
    # Core logic masked by noise
    threshold_filter = [v for v in buffer if v % 3 == 0]
    if len(threshold_filter) < 3:
        fallback = (base * 2) + 5
    else:
        fallback = base + len(threshold_filter)
    
    # Actual computation path
    modulation_index = (shift ** 2) % 9
    core_energy = sum(buffer[i] for i in range(0, len(buffer), 2))
    efficiency_factor = 1.0 + (modulation_index / 10.0)
    thermal_capacity = int((core_energy * efficiency_factor) + fallback)
    
    # Dead code branch (never executed due to data)
    if False and len(buffer) > 100:
        backup = [0] * len(buffer)
        for k in range(len(backup)):
            backup[k] = backup[k-1] + k
    
    return thermal_capacity

# Initialization block
energy_buffer = [12, 7, 18, 5, 9, 21, 3, 14]
phase_shift = 3
auxiliary_weights = [0.1, 0.3, 0.5, 0.7, 0.9]  # Unused in final calculation

# Simulated preprocessing (some has side effects)
filtered_data = [x for x in energy_buffer if x >= 5]
scaling_factor = sum(auxiliary_weights) * 10  # Unused
intermediate_stats = {
    'mean': sum(filtered_data) / len(filtered_data),
    'peak': max(filtered_data),
    'lag': filtered_data[-1] - filtered_data[0]
}

# Key assignment with embedded function call
temp_offset = intermediate_stats['lag'] * 2
target_mode = 'THERMAL' if temp_offset > 0 else 'PASSIVE'
thermal_capacity = calculate_thermal_output(energy_buffer, phase_shift)

# Output result as required
print(f"Result: {thermal_capacity}")