def calculate_system_load():
    base_load = 37
    fluctuations = [2, -5, 8, -3, 10, -1, 6]
    capacity_levels = []

    for i, delta in enumerate(fluctuations):
        adjusted_load = base_load + delta * (i % 3 + 1)
        if adjusted_load > 50:
            adjusted_load = 50
        capacity_levels.append(round(adjusted_load, 2))

    total_sum = sum(capacity_levels)
    peak_capacity = max(capacity_levels)
    
    # Redundant variable (minor interference)
    average_load = total_sum / len(capacity_levels) if capacity_levels else 0
    
    return peak_capacity

result = calculate_system_load()
print(f"Result: {result}")