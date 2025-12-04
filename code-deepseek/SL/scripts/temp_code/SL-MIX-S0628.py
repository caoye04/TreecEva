def energy_transform(func, base):
    # Calculate base energy transformation
    primary = func(base)
    secondary = func(base + 2)
    
    # Distraction calculations that don't affect final result
    temp_shift = (base << 1) & 0xFF
    redundant_metric = primary * 0.5 + secondary * 0.3
    
    # Core logic with lambda function
    energy_adjust = lambda x: x // 2 if x > 10 else x * 2
    adjusted_primary = energy_adjust(primary)
    
    # Final energy calculation
    final_energy = adjusted_primary + (secondary % 5)
    
    print(f"Result: {final_energy}")
    return final_energy

base_level = 4
final_energy = energy_transform(lambda x: x**2 + 3*x - 7, base_level)