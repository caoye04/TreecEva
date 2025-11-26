def calculate_total_energy(base_charge, operation_cycles):
    energy_multiplier = 2.5
    efficiency_factor = 0.85
    
    total_energy = base_charge * energy_multiplier * operation_cycles
    total_energy = total_energy * efficiency_factor
    
    # Simple conditional to handle minimum energy threshold
    if total_energy < 100:
        total_energy = total_energy + 15
    
    return total_energy

initial_charge = 80
cycles = 3
energy_output = calculate_total_energy(initial_charge, cycles)
print(f"Result: {energy_output}")