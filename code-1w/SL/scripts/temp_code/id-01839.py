def calculate_efficiency(load, limits):
    peak = max(limits)
    base = min(limits)
    if load > peak:
        return round((base / load) * 100, 3)
    elif load < base:
        return round((load / base) * 50, 3)
    else:
        normal_range = [x for x in range(base, peak + 1) if x <= load]
        utilization = len(normal_range) / (peak - base + 1)
        return round(utilization * 100, 3)

grid_load = 75
thresholds = [30, 60, 90]
dummy_flag = True
temp_buffer = [0] * 10
energy_output = calculate_efficiency(grid_load, thresholds)
print(f"Target result: {energy_output}")