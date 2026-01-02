def calculate_efficiency(data_slice):
    base = sum(data_slice)
    adjustment = data_slice[0] if data_slice[0] > 0 else 1
    return round(base * 0.85 / adjustment, 3)

sensor_readings = [12, -5, 23, 8, 15]
processed = [x ** 2 for x in sensor_readings if x > 0]
transformed_data = processed[1:4]

# Key computation step
dummy_flag = len(processed) > 5
backup_value = 999
energy_output = calculate_efficiency(transformed_data)
print(f"Result: {energy_output}")