def calculate_efficiency(load, redundancy):
    base_efficiency = 98.5
    adjustment = sum([0.2 * (1.5 ** i) for i in range(len(load)) if load[i] > 75])
    final_reduction = redundancy * 0.75 if len(load) > 3 else 0
    return round(base_efficiency + adjustment - final_reduction, 3)

# System load readings in megawatts over 4-hour window
grid_load = [68, 82, 95, 77]
redundancy_factor = 2

# Irrelevant auxiliary metric (distractor)
system_uptime_hours = 1247
maintenance_cycle = False

# Key computation
energy_threshold = calculate_efficiency(grid_load, redundancy_factor)

Result: energy_threshold