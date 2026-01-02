def calculate_energy_profile():
    base_load = 120
    peak_multiplier = 1.8
    efficiency_factor = 0.75
    current_demand = 95
    temperature = 32

    is_peak_time = current_demand > 100 or temperature > 30
    load_level = base_load * peak_multiplier if is_peak_time else base_load

    energy_threshold = load_level if is_peak_time else base_load * efficiency_factor

    # Irrelevant monitoring variables (minor interference)
    status_code = 200
    last_updated = "14:30"
    
    return energy_threshold

result = calculate_energy_profile()
print(f"Result: {result}")