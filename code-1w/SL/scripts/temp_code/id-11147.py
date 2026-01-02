def calculate_harvest_efficiency(yield_data, threshold):
    daily_efficiency = []
    for i, yield_val in enumerate(yield_data):
        efficiency = round(yield_val / (i + 1), 2) if i != 0 else round(yield_val, 2)
        daily_efficiency.append(efficiency)

    labeled_data = list(zip(daily_efficiency, yield_data))
    filtered_yields = [y for e, y in labeled_data if e > threshold]
    
    temp_sum = sum(daily_efficiency)  # Irrelevant computation (minimal distraction)
    total_harvest = sum(filtered_yields)
    return total_harvest

# Simulation data
crop_yields = [23, 45, 67, 39, 58, 72, 51]
min_threshold = 20.0
total_harvest = calculate_harvest_efficiency(crop_yields, min_threshold)
print(f"Result: {total_harvest}")