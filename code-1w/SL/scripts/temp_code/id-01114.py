def convert_and_scale(temps, func):
    converted = {}
    for unit, temp in temps.items():
        if unit == 'fahrenheit':
            celsius = (temp - 32) * 5 / 9
            converted[unit] = func(celsius)
        elif unit == 'kelvin':
            celsius = temp - 273.15
            converted[unit] = func(celsius)
        else:
            converted[unit] = func(temp)
    return sum(converted.values())

# Temperature readings from different sensors
temp_map = {
    'sensor_a': 25,         # Celsius
    'fahrenheit': 98.6,     # Human body temp
    'kelvin': 373.15,       # Boiling point of water
    'sensor_b': -40         # Extreme cold
}

# Apply cubic scaling above threshold via lambda
transform_func = lambda x: x ** 2 / 10 if x > 50 else x + 10

# Irrelevant auxiliary variable (minor distraction)
baseline_offset = 0.5

final_temperature = convert_and_scale(temp_map, transform_func)
print(f"Result: {final_temperature}")