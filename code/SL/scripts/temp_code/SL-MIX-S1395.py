temperatures = [22.5, None, 24.0, 23.5, None, 25.0]
valid_readings = [t for t in temperatures if t is not None]
is_sufficient_data = len(valid_readings) >= 3
avg_temperature = sum(valid_readings)/len(valid_readings) if is_sufficient_data and valid_readings else 0
print(f'Result: {avg_temperature}')