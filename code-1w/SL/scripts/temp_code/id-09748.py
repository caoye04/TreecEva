def calculate_efficiency(readings):
    avg = sum(readings) / len(readings)
    squared_devs = list(map(lambda x: (x - avg) ** 2, readings))
    variance = sum(squared_devs) / len(squared_devs)
    return round(100 * (1 - variance / (avg + 1)), 2)

sensor_data = [12.5, 14.0, 13.7, 15.2, 13.0, 14.8, 16.1, 13.9]
filtered_readings = sensor_data[1:7:1]
baseline_check = [x for x in filtered_readings if x > 13.5]
energy_output = calculate_efficiency(filtered_readings)
print(f"Result: {energy_output}")