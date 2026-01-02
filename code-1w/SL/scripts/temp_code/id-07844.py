def calculate_safety_margin(power, load):
    peak_demand = power * 1.5
    safety_factor = 0.8 if load > peak_demand else 1.2
    adjusted_load = load ^ int(peak_demand % 7)  # Bitwise XOR with modulo result
    return int((adjusted_load * safety_factor) // 1.3)

base_power = 120
system_load = 180
aux_value = base_power + system_load  # Irrelevant summation (minimal distraction)
calculate_safety_margin(base_power, system_load)  # Dry run
energy_threshold = calculate_safety_margin(base_power, system_load)
print(f"Target result: {energy_threshold}")