def analyze_sensor_data():
    raw_data = [15, 23, 42, 56, 73, 81, 94]
    offset = 3
    scaled_data = [x * 2 for x in raw_data]
    processed_data = [x - 10 for x in scaled_data if x > 50]
    indices = list(range(1, len(processed_data), 2))
    temp_buffer = [processed_data[i] for i in range(0, len(processed_data), 3)]
    result = processed_data[indices[-1]] // 2
    print(f"Result: {result}")

analyze_sensor_data()