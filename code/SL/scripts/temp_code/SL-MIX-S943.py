temperatures = [23, None, 25, 22, None, 24, 26, None, 21, 27]
valid_readings = list(filter(lambda x: x is not None, temperatures))
valid_count = len(valid_readings)
total_days = len(temperatures)
min_valid = total_days / 2
avg_temperature = sum(valid_readings) / valid_count if valid_count >= min_valid else 0
print(f'Result: {avg_temperature}')