def calculate_efficiency(load, thresh):
    adjusted_load = [val * 0.9 for val in load if val > thresh]
    total_input = sum(load)
    total_adjusted = sum(adjusted_load)
    efficiency_ratio = total_adjusted / total_input
    return int(total_adjusted * efficiency_ratio)

grid_load = [120, 150, 90, 200, 180]
thresh_limit = 100
energy_output = calculate_efficiency(grid_load, thresh_limit)
print(f"Result: {energy_output}")