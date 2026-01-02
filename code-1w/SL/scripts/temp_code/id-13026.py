def calculate_safety_margin(level, peak):
    normal_op = level > 50
    surge_protected = peak < 120
    return (level * 1.2) if normal_op and surge_protected else (level * 0.8)

base_level = 75
peak_load = 110
temperature_factor = 1.05  # Irrelevant to final result
voltage_stable = True      # Distractor variable

energy_threshold = calculate_safety_margin(base_level, peak_load)

Result: {energy_threshold}