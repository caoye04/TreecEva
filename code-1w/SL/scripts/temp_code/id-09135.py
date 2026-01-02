def calculate_energy_status(load_level, efficiency_mode):
    baseline_energy = 78
    reduction = 22
    boost = 14
    peak_load = 95
    min_load = 10
    temp_buffer = (peak_load + min_load) // 2  # Irrelevant computation

    active = load_level > 50
    energy_threshold = max(0, baseline_energy - reduction) if active else baseline_energy + boost
    
    diagnostic_log = f"Load: {load_level}, Mode: {efficiency_mode}"  # Logging, no impact
    return energy_threshold

result = calculate_energy_status(57, "high_efficiency")
print(f"Result: {result}")