fahrenheit_readings = [68, 77, 86, 95, 104]
total_temperature = sum([(temp - 32) * 5/9 for temp in fahrenheit_readings])
print(f"Total temperature: {total_temperature}")