def simulate_chemical_equilibrium(steps, initial_concentration):
    concentrations = [initial_concentration]
    reaction_rates = []
    temperature_history = []
    pressure_buffer = []

    for i in range(1, steps + 1):
        current = concentrations[-1]
        
        # Irrelevant temperature fluctuation tracking (distractor)
        temp_effect = (i % 7) * 0.3 if i % 3 == 0 else (i % 5) * 0.1
        temperature_history.append(temp_effect)
        
        # Real computation path
        forward_rate = (current * 0.8) / (1 + current)
        backward_rate = 0.2 * current ** 0.5
        net_change = forward_rate - backward_rate
        
        new_concentration = current + net_change
        concentrations.append(new_concentration)
        
        # Logging pressure as side effect (partially relevant)
        raw_pressure = abs(new_concentration * 2.3 - i * 0.1)
        pressure_buffer.append(raw_pressure)

        # Dead code: never used again (distractor)
        if i % 10 == 0:
            _ = [x * 0.95 for x in pressure_buffer if x > 1.0]

    # Slice recent history for stability check
    recent_concs = concentrations[-5:]
    smoothed = sum(recent_concs) / len(recent_concs)
    
    # Simulate log recording (semi-relevant)
    state_log = [f'STATE_{j}' for j in range(steps//2)]
    state_log.append(f'STABLE_{smoothed:.3f}')

    def calculate_equilibrium(state_str):
        # Extract numeric part from state string
        eq_val = float(state_str.split('_')[-1])
        base_pressure = eq_val * 12.5
        
        # Additional irrelevant transformation
        dummy_shift = sum([i**2 for i in range(len(state_log))]) * 0.001
        adjusted = base_pressure + dummy_shift  # Slight distraction
        
        # Final computation uses slicing of pressure buffer
        recent_pressures = pressure_buffer[-3:] if len(pressure_buffer) >= 3 else [0]
        correction = max(recent_pressures) * 0.1 if recent_pressures else 0
        return adjusted + correction

    # Key statement
    final_pressure = calculate_equilibrium(state_log[-1])
    
    # Print result for evaluation
    print(f"Result: {final_pressure}")
    
    # Irrelevant post-calculation (dead code path)
    if final_pressure < 0:
        for k in range(5):
            final_pressure += k * 0.1

    return final_pressure

# Execute simulation
result = simulate_chemical_equilibrium(steps=12, initial_concentration=3.2)