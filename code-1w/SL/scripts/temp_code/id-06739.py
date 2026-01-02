def calculate_reservoir_capacity(rainfall_data, threshold):
    adjusted_levels = []
    temp_offset = 0.0
    for i, level in enumerate(rainfall_data):
        if level > threshold:
            adjusted_level = level * (i + 1)
        else:
            adjusted_level = level / 2
        adjusted_levels.append(adjusted_level)
    
    total_capacity = sum(adjusted_levels)
    return total_capacity

rainfall_readings = [12, 8, 15, 5, 20]
threshold_limit = 10
result = calculate_reservoir_capacity(rainfall_readings, threshold_limit)
total_capacity = result
print(f"Result: {total_capacity}")