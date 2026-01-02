def calculate_safety_margin(base, peak):
    normalizer = 1 if peak == 0 else peak
    adjusted_base = base * 1.25
    load_ratio = (peak - base) / normalizer if normalizer != 0 else 0
    safety_factor = 1.5 if load_ratio > 0.3 else 1.1
    return int(adjusted_base * safety_factor)

# System baseline parameters
temperature_zone = 3
base_level = 80
peak_load = 120

# Irrelevant diagnostic flag (minimal distraction)
diagnostic_mode = False

# Key computation
energy_threshold = calculate_safety_margin(base_level, peak_load)

# Output result as required
print(f"Result: {energy_threshold}")