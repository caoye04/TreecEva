def calculate_energy_allocation():
    base_load = 1200
    peak_multiplier = 1.6
    is_peak_hour = True
    temperature = 32  # degrees Celsius
    humidity_factor = 0.9  # unrelated to main logic

    adjusted_load = base_load * peak_multiplier
    load_level = adjusted_load + 100 if temperature > 30 else adjusted_load

    energy_threshold = load_level if is_peak_hour else base_load * 0.8

    # Irrelevant environmental metric (distractor)
    comfort_index = temperature * humidity_factor

    return energy_threshold

result = calculate_energy_allocation()
print(f"Target result: {result}")