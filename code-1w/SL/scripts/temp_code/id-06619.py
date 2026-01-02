def calculate_peak_storage():
    storage_levels = [120, 150, 135, 180, 200, 175, 160, 190]
    threshold = 170
    peak_indices = []

    for i in range(len(storage_levels)):
        if storage_levels[i] > threshold:
            peak_indices.append(i)

    initial_reserve = 50
    total_storage = [val + initial_reserve for val in storage_levels]
    
    # Irrelevant tracking variable (minor distraction)
    avg_excess = sum([x - threshold for x in storage_levels if x > threshold]) / len([x for x in storage_levels if x > threshold])

    peak_index = peak_indices[0] if peak_indices else 0
    energy_capacity = total_storage[peak_index:]
    energy_capacity = sum(energy_capacity[:3])  # Accumulate first three peak-adjusted values

    status_flag = True
    Result: energy_capacity
    return energy_capacity

result = calculate_peak_storage()
print(f"Target result: {result}")