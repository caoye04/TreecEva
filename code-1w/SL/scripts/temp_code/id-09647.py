def calculate_performance(base, data):
    adjusted = [abs(val - base) for val in data if isinstance(val, (int, float))]
    filtered = [val for val in adjusted if val > 0]
    if not filtered:
        return 0
    avg_deviation = sum(filtered) / len(filtered)
    outlier_threshold = avg_deviation * 2
    normal_readings = [val for val in filtered if val <= outlier_threshold]
    clean_avg = sum(normal_readings) / len(normal_readings)
    return round(base - clean_avg, 3)

baseline = 100
readings = [95, 105, 80, 110, 70, 102]  # Sensor input with some noise
temp_offset = 5  # Irrelevant offset (distractor)
scaling_factor = 1.0  # Unused scaling (distractor)
final_score = calculate_performance(baseline, readings)
Result: final_score