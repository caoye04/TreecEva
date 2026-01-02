def analyze_temperature_trend(readings):
    filtered_readings = [temp for temp in readings if temp > 0]
    sorted_readings = sorted(filtered_readings)
    min_temp = sorted_readings[0]
    max_temp = sorted_readings[-1]
    temperature_stats = (min_temp, max_temp)
    result = temperature_stats[1] - temperature_stats[0]
    return result

# Simulated sensor data with some invalid (non-positive) values
sensor_data = [3, -1, 15, 8, 0, 22, 11, 5]
final_result = analyze_temperature_trend(sensor_data)
print(f"Result: {final_result}")