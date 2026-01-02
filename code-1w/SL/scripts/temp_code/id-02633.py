def analyze_system_equilibrium():
    # Simulate multi-phase system with feedback loops
    phase_inputs = [18, 24, 36, 42, 54]
    adjustment_factors = [0.8, 1.2, 0.9, 1.1, 1.0]
    
    cumulative_weight = 0
    transient_buffer = 0
    cycle_count = 0
    decay_rate = 0.95
    
    # Irrelevant tracking variables (distractors)
    peak_magnitude = 0
    oscillation_count = 0
    damping_ratio = 0.0
    
    for i in range(len(phase_inputs)):
        raw_signal = phase_inputs[i]
        adjusted_signal = raw_signal * adjustment_factors[i % len(adjustment_factors)]
        
        # Simulate signal filtering
        filtered_output = int(adjusted_signal * (decay_rate ** i))
        
        # Update relevant state
        if filtered_output > 20:
            cumulative_weight += filtered_output // 3
            cycle_count += 1
        else:
            transient_buffer += filtered_output
        
        # Distractor logic: tracks peaks but unused in final result
        if filtered_output > peak_magnitude:
            peak_magnitude = filtered_output
            oscillation_count += 1
        
        # More irrelevant computation
        if i % 2 == 0:
            damping_ratio += 0.05 * (filtered_output / (raw_signal + 1))
    
    # Secondary processing with list comprehension
    residuals = [abs(x - 30) for x in phase_inputs]
    correction_term = sum([r**2 for r in residuals if r > 5]) // 100
    
    # Logic to compute final tally using conditional expression
    base_tally = cumulative_weight + (transient_buffer if transient_buffer < 50 else 25)
    final_tally = base_tally + (correction_term if cycle_count > 3 else 0)
    
    # Key statement
    equilibrium_score = final_tally // (cycle_count + 1)
    
    # Print result as required
    print(f"Result: {equilibrium_score}")

analyze_system_equilibrium()