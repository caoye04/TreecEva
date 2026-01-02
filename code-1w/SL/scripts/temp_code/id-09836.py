def calculate_system_capacity():
    base_levels = [12, 15, 18, 20, 22]
    thresholds = [10, 16, 17, 21, 25]
    adjustment_factor = 1.5
    temp_offset = 3  # Irrelevant offset not used in main logic

    adjusted_levels = []
    for i, (level, threshold) in enumerate(zip(base_levels, thresholds)):
        if level < threshold:
            adjusted_value = level * adjustment_factor
        else:
            adjusted_value = level + adjustment_factor
        adjusted_levels.append(adjusted_value)

    total_capacity = sum(adjusted_levels)
    return total_capacity

result = calculate_system_capacity()
print(f"Result: {result}")