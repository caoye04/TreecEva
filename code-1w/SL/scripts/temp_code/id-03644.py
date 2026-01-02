def simulate_reactor_performance():
    temperature = 273
    pressure = 101.3
    fuel_load = 42
    efficiency_factor = 0.87

    # Initial safety checks (irrelevant to final computation but part of workflow)
    system_status = 'nominal' if temperature < 300 and pressure < 110 else 'caution'
    
    # Primary calculation chain
    base_output = fuel_load * 23
    adjusted_output = base_output * (1 + (temperature - 273) * 0.002)
    
    # Conditional efficiency adjustment based on pressure
    efficiency_multiplier = 1.1 if pressure > 100 else 0.9
    
    # Final energy output with conditional efficiency
    energy_output = adjusted_output * (efficiency_factor if pressure > 100 else efficiency_factor * 0.95)
    energy_output *= efficiency_multiplier

    # Irrelevant telemetry logging (minor interference)
    log_entry = f'Reactor: T={temperature}, P={pressure}, E={energy_output:.1f}'
    
    return energy_output

result = simulate_reactor_performance()
print(f"Result: {result}")