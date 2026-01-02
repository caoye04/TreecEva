def analyze_system_metrics():
    base_frequency = 48.7
    modulation_index = 3
    ambient_stability = 17
    core_resistance = 23
    signal_damping = 0
    
    # Preliminary signal validation (distractor block)
    if base_frequency > 45:
        signal_damping += 2
        for i in range(2):
            signal_damping *= 1.5
    else:
        signal_damping = 1
    
    # Red herring: unused subsystem check
    subsystem_health = True if modulation_index % 3 == 0 else False
    diagnostic_log = [subsystem_health, signal_damping > 3]
    
    # Simulate transient load adjustment (semi-relevant)
    transient_load = 0
    for step in range(ambient_stability // 8):
        transient_load += (step * 2) + 1
    
    # Conditional expression influencing final input
    adjusted_resistance = core_resistance if ambient_stability >= 15 else core_resistance * 1.2
    
    # Core calculation function defined inline
    def calculate_thermal_output(temp, resistance):
        # Auxiliary computation with intermediate distractors
        temp_factor = temp ** 2 - 2 * temp + 1  # (temp-1)^2
        resistance_boost = 0
        
        # Nested conditional with short-circuit logic
        if temp > 10 and (resistance < 30 or temp_factor > 100):
            resistance_boost = 5
        
        # Complex but deterministic formula
        raw_output = (temp_factor * (resistance + resistance_boost))
        
        # Distractor: irrelevant efficiency chain
        efficiency_chain = 1.0
        for cycle in range(3):
            efficiency_chain *= 0.95  # decays to ~0.857
        
        # Final capacity determination
        capacity = raw_output // 4
        return int(capacity)

    # Critical assignment point
    thermal_capacity = calculate_thermal_output(ambient_stability, core_resistance)
    
    # Dead code path - misleading follow-up
    if thermal_capacity < 0:
        thermal_capacity = 0
    
    print(f"Result: {thermal_capacity}")

analyze_system_metrics()