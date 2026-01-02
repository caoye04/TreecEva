def evaluate_threshold(data_map, limit):
    count = 0
    temp_sum = 0.0
    for key in data_map:
        if len(key) % 2 == 1:
            value = data_map[key]
            if value > limit:
                count += 1
                temp_sum += value
    result = temp_sum / count if count > 0 else 0
    return round(result, 3)

# Irrelevant auxiliary variable (minor distraction)
baseline = [2.1, 3.4, 4.5]

# Core data structure with meaningful content
temperature_data = {
    'sensor_a': 2.8,
    'node_x': 3.6,
    'probe': 4.1,
    'log_1': 2.9,
    'entry': 5.0
}

# Execution point of interest
count_valid = len([v for v in temperature_data.values() if v > 3])
threshold_score = evaluate_threshold(temperature_data, 3)

print(f"Result: {threshold_score}")