def calculate_grid_load(base_demand, fluctuations):
    adjusted_loads = [base_demand * (1 + f) for f in fluctuations]
    filtered_loads = [load for load in adjusted_loads if load > 100]
    grid_loads = [max(load, 120) for load in filtered_loads]
    safety_margin = 1.1  # Irrelevant distractor
    peak_load = max(grid_loads)
    return peak_load

base_demand = 95
fluctuations = [0.1, 0.3, 0.05, 0.8]
result = calculate_grid_load(base_demand, fluctuations)
peak_load = result
print(f"Target result: {peak_load}")