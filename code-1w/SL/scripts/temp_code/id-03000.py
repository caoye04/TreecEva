def analyze_reactor_state(temperature, pressure, cycles):
    base_stability = 97.3
    fluctuation = temperature * 0.07
    energy_level = base_stability - fluctuation + (pressure // 10)
    cycle_count = cycles + 1
    
    # Preliminary diagnostics
    initial_safe = energy_level > 90
    peak_load = pressure > 150
    
    # Conditional expression for adaptive threshold
    energy_threshold = 85 if not peak_load else 90
    
    # Final system diagnostic
    final_diagnostic = (energy_level > 85) and (cycle_count < 10)
    
    # Output result
    print(f"Result: {energy_threshold}")
    return energy_threshold

# Simulate reactor with specific parameters
result = analyze_reactor_state(temperature=120, pressure=140, cycles=6)