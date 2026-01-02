from itertools import cycle

def calculate_efficiency(base, modifiers):
    mod_cycle = cycle(modifiers)
    total_effect = 0.0
    for _ in range(len(modifiers) * 2):
        change = next(mod_cycle)
        total_effect += change if total_effect + change > 0 else 0.1
    return int(base * (total_effect / len(modifiers)))

initial_power = 150
safety_factor = 0.9
adjustments = [1.1, -0.5, 0.3, -0.2, 0.4]

temp_buffer = [x * 2 for x in adjustments]  # Irrelevant precomputation (minor distraction)

energy_output = calculate_efficiency(initial_power, adjustments)
energy_output = int(energy_output * safety_factor)

Result: energy_output