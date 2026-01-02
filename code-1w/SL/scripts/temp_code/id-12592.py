def analyze_sensor_data(readings):
    threshold = 50
    smoothed_readings = [round((r + readings[i-1]) / 2) for i, r in enumerate(readings) if i > 0]
    smoothed_readings.append(readings[-1])

    valid_range = {x for x in range(20, 100)}
    filtered_readings = [val for val in smoothed_readings if val in valid_range]

    temp = [x for x in smoothed_readings if x < 20]
    extra_metric = len(temp) * 2

    filtration_score = sum(filtered_readings) // len(filtered_readings)
    
    debug_mode = False
    if debug_mode:
        print(f"Discarded: {extra_metric} low values")

    return filtration_score

sensor_input = [65, 70, 45, 80, 90, 30, 40]
result = analyze_sensor_data(sensor_input)
print(f"Target result: {result}")