def process_efficiency(filter_func, data):
    filtered = [x for x in data if filter_func(x)]
    total = sum(filtered)
    count = len(filtered)
    return round(total / count, 3) if count > 0 else 0

# Simulated IoT sensor readings (mg/m³ particulate matter)
sensor_data = [23.4, 19.1, 45.6, 30.2, 12.8, 50.0, 37.3, 8.9]

deviation_flags = [x < 10 or x > 40 for x in sensor_data]  # Irrelevant distractor list
status_labels = list(map(str.upper, ['ok', 'alert', 'critical']))  # Unused string operation

threshold = 25.0
smoothness_factor = 1.05  # Unused parameter (distractor)

filtration_score = process_efficiency(lambda x: x > threshold, sensor_data)
print(f"Result: {filtration_score}")