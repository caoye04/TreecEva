def calculate_system_load():
    base_frequencies = [1.2, 1.8, 2.4, 3.0]
    efficiency_ratios = [0.95, 0.88, 0.92, 0.85]
    
    # Calculate power consumption using frequency^2 * efficiency
    powers = []
    for freq, eff in zip(base_frequencies, efficiency_ratios):
        power = (freq ** 2) * eff
        powers.append(round(power, 3))
    
    # Irrelevant debugging info (minimal distraction)
    debug_mode = False
    log_entries = len(powers)
    
    total_load = sum(powers)
    return total_load

result = calculate_system_load()
print(f"Result: {result}")