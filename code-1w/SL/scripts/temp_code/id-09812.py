def analyze_system_performance(input_energy, ambient_temp):
    base_load = 127
    peak_threshold = 950
    efficiency_ratio = 0.88
    degradation_factor = 0.03

    # Simulate fluctuating load conditions
    fluctuating_loads = [input_energy * (0.9 + i * 0.05) for i in range(5)]
    valid_loads = [load for load in fluctuating_loads if load < peak_threshold]

    # Compute average effective load
    total_effective_load = sum(valid_loads)
    load_count = len(valid_loads)
    average_load = total_effective_load / load_count if load_count > 0 else 0

    # Secondary calculation: heat dissipation rate (not directly used)
    temp_gradient = ambient_temp - 22
    dissipation_rate = temp_gradient * 1.6
    corrected_dissipation = dissipation_rate * (1 + degradation_factor)

    # Efficiency loss computation chain
    raw_loss = (input_energy - average_load)
    conditional_penalty = 1.15 if average_load < base_load else 1.0
    efficiency_losses = (raw_loss * efficiency_ratio) * conditional_penalty

    # Dummy state tracking (distractor)
    system_states = ['idle', 'active', 'overload']
    current_state = system_states[1] if average_load > peak_threshold * 0.7 else system_states[0]
    state_code = hash(current_state) % 100

    # Final thermal model
    def calculate_thermal_output(losses):
        base_heat = losses * 0.42
        surge_buffer = 17.3
        # Apply environmental correction
        adjusted_heat = base_heat * (1 + (ambient_temp - 20) * 0.015)
        final_heat = adjusted_heat + surge_buffer
        return int(final_heat)  # Discrete capacity units

    thermal_capacity = calculate_thermal_output(efficiency_losses)
    
    # Dead code path (red herring)
    if state_code < 50:
        backup_correction = ambient_temp // 2
        thermal_capacity += backup_correction  # Not triggered due to logic

    # Unrelated logging
    debug_snapshot = {
        'timestamp': 1678886400,
        'voltage_peaks': [231, 234, 229],
        'crc_checksum': 0xDEADBEEF
    }
    
    print(f"Result: {thermal_capacity}")

analyze_system_performance(867, 25)