def calculate_peak_operational_load():
    base_capacity = 150
    maintenance_factor = 0.9
    daily_loads = [120, 145, 160, 175, 130, 180, 165]
    adjusted_loads = [int(load * maintenance_factor) for load in daily_loads]
    operational_days = len(daily_loads) - 2
    mid_range_slice = daily_loads[1:-1]
    peak_load = max(daily_loads[1:-1])
    avg_load = sum(adjusted_loads) / len(adjusted_loads)
    return peak_load

result = calculate_peak_operational_load()
print(f"Target result: {result}")