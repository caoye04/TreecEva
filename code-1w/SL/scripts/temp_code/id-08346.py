def analyze_system_performance():
    base_frequency = 420.5
    network_load = 88
    signal_strength = 94.3
    redundancy_factor = 12

    # Auxiliary diagnostics (distractor computations)
    diagnostic_log = []
    temp_buffer = [base_frequency * 0.85, signal_strength + 12.7, 100 - redundancy_factor]
    avg_diagnostic = sum(temp_buffer) / len(temp_buffer)
    diagnostic_log.append(avg_diagnostic)

    # Irrelevant cache simulation
    cache_size = 128
    block_count = 16
    cache_utilization = cache_size / block_count if block_count else 0
    optimization_flag = True if cache_utilization > 5 else False

    # Secondary state tracking (not used in final result)
    system_state = {'status': 'active', 'phase': 3, 'priority': 7}
    state_priority = system_state['priority'] * 2 if system_state['status'] == 'active' else 0

    # Core calculation chain with mixed paradigms
    def calculate_efficiency(load, redun):
        load_ratio = load / 100.0
        penalty = 0.1 * redun if redun > 10 else 0.05 * redun
        efficiency = (1 - load_ratio) - penalty
        return efficiency if efficiency > 0 else 0.0

    # Conditional expression and lambda for dynamic adjustment
    mode_selector = 'turbo'
    adjustment_factor = 1.25 if mode_selector == 'turbo' else 1.0
    safety_check = lambda x: x >= 0.1

    preliminary_score = calculate_efficiency(network_load, redundancy_factor)
    if not safety_check(preliminary_score):
        return -1

    # Key execution point
    thermal_capacity = calculate_efficiency(network_load, redundancy_factor) * 1.75

    # Dead code path (never reached due to structure)
    if signal_strength < 0:
        thermal_capacity *= 0.5

    # Additional irrelevant computation
    spectral_density = base_frequency * (signal_strength / 100)
    harmonic_damping = spectral_density ** 0.5 if spectral_density > 50 else 0

    # Final output
    print(f"Result: {thermal_capacity}")

analyze_system_performance()