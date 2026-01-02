def process_sensor_data():
    base_temperatures = [23.5, 18.2, 19.8, 17.3, 20.1]
    calibration_sequence = [1.1, 1.2, 1.0, 0.9, 1.3]
    scaling_factor = 2
    offset = -5
    active_zone = slice(1, 4)
    temperature_data = [round(base * cal, 2) for base, cal in zip(base_temperatures, calibration_sequence)]
    processed_slice = temperature_data[active_zone]
    reversed_slice = processed_slice[::-1]
    result = reversed_slice[0] * scaling_factor + offset
    print(f"Target result: {result}")

process_sensor_data()