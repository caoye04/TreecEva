def get_correction_factor(sensor_type):
    match sensor_type:
        case 'A':
            return 0.5
        case 'B':
            return -0.3
        case _:
            return 0.0

sensor_reading_celsius = 20.0
sensor_type = 'A'
correction = get_correction_factor(sensor_type)
corrected_celsius = sensor_reading_celsius + correction
final_temperature_fahrenheit = (corrected_celsius * 9/5) + 32

print(f"Result: {final_temperature_fahrenheit}")