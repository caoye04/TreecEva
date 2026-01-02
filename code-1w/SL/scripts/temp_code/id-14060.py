def calculate_threshold(data):
    filtered = [x for x in data if x > 50]
    average = sum(filtered) / len(filtered) if filtered else 0
    return int(average * 0.9)

readings = [45, 60, 70, 55, 80, 30, 90, 65]
sensor_count = len(readings)
baseline = sum(readings) / len(readings)
threshold_score = calculate_threshold(readings)
print(f"Result: {threshold_score}")