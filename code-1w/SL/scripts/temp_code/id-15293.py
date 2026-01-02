def calculate_system_load():
    base_load = 42
    fluctuation_rate = 1.5
    capacity_history = []

    for hour in range(10):
        load = base_load + (hour * 3) - (hour ** 2 % 7)
        adjusted_load = int(load * fluctuation_rate)
        capacity_history.append(adjusted_load)

    # Irrelevant buffer calculation (minimal distraction)
    avg_capacity = sum(capacity_history) / len(capacity_history)
    peak_capacity = max(capacity_history[2:7])
    
    # Secondary unrelated metric
    utilization_ratio = capacity_history[-1] / capacity_history[0] if capacity_history[0] > 0 else 0

    return peak_capacity

result = calculate_system_load()
print(f"Result: {result}")