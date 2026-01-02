def calculate_efficiency(load, capacity):
    base_efficiency = 0.85
    overload_penalty = 0.1 if load > capacity * 0.9 else 0.02
    efficiency = base_efficiency - overload_penalty
    return int(efficiency * 100)

grid_load = 870
current_voltage = 230  # irrelevant variable (minimal distraction)
max_capacity = 1000
safety_margin = 50  # irrelevant variable

# Conditional expression and list comprehension (Python idioms)
is_stable = True if grid_load < max_capacity else False
load_history = [x for x in range(800, grid_load, 10)]  # uses grid_load, not directly relevant to final answer

energy_threshold = calculate_efficiency(grid_load, max_capacity)

print(f"Target result: {energy_threshold}")