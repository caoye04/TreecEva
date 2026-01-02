def calculate_efficiency(data):
    # Irrelevant transformation (distractor)
    normalized = list(map(lambda x: (x - min(data)) / (max(data) - min(data) + 1e-9), data))
    
    # Key processing steps
    filtered = [x for x in data if x > sum(data) / len(data)]  # Only values above mean
    squared_devs = [(x - sum(data)/len(data))**2 for x in filtered]
    variance = sum(squared_devs) / len(squared_devs) if squared_devs else 0
    efficiency_factor = max(data) / (variance + 1)  # Critical metric
    
    # Dead computation path (misleading)
    redundant_sum = 0
    for i in range(len(normalized)):
        if normalized[i] > 0.5:
            redundant_sum += i * 1.5  # Not used later

    # Secondary distractor: complex but unused lambda
    transform = lambda lst: [lst[i] * lst[i-1] for i in range(1, len(lst))]
    ignored_series = transform([int(x) for x in normalized])

    # Final calculation (depends only on efficiency_factor and length)
    base_yield = len(filtered) * efficiency_factor
    thermal_output = int(base_yield + variance * 0.5)  # Final result
    
    return thermal_output

# Input data (real signal embedded in noise)
data_sequence = [12, 15, 10, 23, 8, 19, 14, 16]
offset_correction = [x * 0.1 for x in data_sequence]  # Unused side data
process_data = [x + 2 for x in data_sequence]  # Actual input

# Execution point of interest
temperature_baseline = 273
thermal_output = calculate_efficiency(process_data)
print(f"Result: {thermal_output}")