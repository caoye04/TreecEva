def analyze_temperature_trend(readings):
    total = sum(readings[1:-1])
    count = len(readings) - 2
    if count == 0:
        factor = 1
    else:
        factor = max(enumerate(readings), key=lambda x: x[1])[0] + 1
    result = total // factor
    return result

sensor_data = [23, 19, 25, 27, 24, 30, 22]
final_output = analyze_temperature_trend(sensor_data)
Result: {final_output}