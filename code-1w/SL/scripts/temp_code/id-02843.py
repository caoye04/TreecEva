def simulate_production_cycle():
    phases = ['initiation', 'acceleration', 'stabilization', 'decline']
    base_output = 1200
    degradation_rate = 0.92
    stress_factor = 0.0
    threshold = 5.7
    efficiency_map = {phase: (0.35 + i * 0.21) for i, phase in enumerate(phases)}
    temp_log = []
    debug_flags = [False, False, True]
    aggregate_stress = 0.0
    cycle_yield = 0
    final_yield = 0

    for cycle in range(1, 9):
        phase_index = (cycle - 1) % 4
        current_phase = phases[phase_index]
        
        # Core calculation branch
        raw_contribution = base_output * (degradation_rate ** (cycle // 4))
        efficiency = efficiency_map[current_phase]
        adjusted_output = raw_contribution * efficiency
        
        # Distractor block: logging irrelevant metrics
        diagnostic_score = (adjusted_output / 100) * (phase_index + 1)
        temp_log.append(diagnostic_score * 0.76)
        if len(temp_log) > 3:
            moving_avg = sum(temp_log[-3:]) / 3
            aggregate_stress += moving_avg * 0.15

        # Real logic affecting result
        stress_factor = (cycle * 0.8) + (aggregate_stress * 0.3)
        
        if stress_factor > threshold and efficiency_map[current_phase] < 0.4:
            break
        
        cycle_yield += int(adjusted_output)
    
    # Final adjustment independent of loop break
    safety_margin = 0.95
    final_yield = int(cycle_yield * safety_margin)
    
    # Dead code path - never executed due to structure
    if debug_flags[2] and False:
        final_yield -= 500
        final_yield = max(final_yield, 0)

    print(f"Result: {final_yield}")

simulate_production_cycle()