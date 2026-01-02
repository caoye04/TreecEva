def analyze_system_stability(readings, threshold=15):
    base_equilibrium = 10
    adjustment = 5
    transient_peak = 0
    cumulative_drift = 0
    equilibrium_score = 0
    
    for reading in readings:
        # Irrelevant drift accumulation (distractor)
        cumulative_drift += reading * 0.1
        
        if reading > 20:
            transient_peak += 1
        
        # Core logic begins here
        raw_signal = reading - 5
        normalized = abs(raw_signal) ** 0.5
        
        # Conditional expression (required Python feature)
        signal_weight = 1.5 if normalized > threshold * 0.3 else 1.0
        
        filtered = normalized * signal_weight
        
        # List comprehension (required Python feature) - partially irrelevant
        harmonics = [filtered / (i + 1) for i in range(3)]
        energy_sum = sum(harmonics)
        
        net_flow = energy_sum - base_equilibrium
        
        # Key statement: decision point with conditional assignment
        equilibrium_score = net_flow if net_flow > threshold else base_equilibrium + adjustment
        
        # Dead code path (distractor)
        if False:
            equilibrium_score *= 0.9
    
    # Additional misleading computation (does not affect final result)
    final_diagnostic = transient_peak * 100 + cumulative_drift
    
    print(f"Result: {equilibrium_score}")

# Input data
sensor_data = [25, 18, 22]
analyze_system_stability(sensor_data)