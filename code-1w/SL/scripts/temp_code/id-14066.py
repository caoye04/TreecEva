def calculate_peak_load():
    base_loads = [12, 15, 10, 20, 25, 18, 22, 30, 28, 24]
    growth_factor = 1.2
    adjusted_loads = [int(x * growth_factor) for x in base_loads]
    
    # Simulate maintenance period: ignore first 2 and last 3 days
    load_profile_sliced = adjusted_loads[2:-3]
    
    # Irrelevant distraction: calculate average (not used in final answer)
    total = sum(adjusted_loads)
    average_load = total / len(adjusted_loads)
    
    peak_capacity = max(load_profile_sliced)
    return peak_capacity

result = calculate_peak_load()
print(f"Result: {result}")