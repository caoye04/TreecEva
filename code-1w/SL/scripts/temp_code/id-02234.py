def calculate_pressure_adjustment(altitude, temperature_readings):
    base_pressure = 1013.25
    pressure_adjustment = 0.0
    altitude_factor = 0.0981
    temp_sum = 0
    valid_count = 0

    for i, temp in enumerate(temperature_readings):
        if temp < -50 or temp > 60:
            continue
        temp_sum += temp
        valid_count += 1

        adjusted_temp = temp * (1 - altitude_factor * altitude / 1000)
        if abs(adjusted_temp - temp) > 15:
            pressure_adjustment += base_pressure * 0.02
            break
        else:
            pressure_adjustment += base_pressure * 0.01

    return pressure_adjustment


temperature_readings = [25, 30, -60, 45, 10]
altitude = 2500
result = calculate_pressure_adjustment(altitude, temperature_readings)
print(f"Result: {result}")