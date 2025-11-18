temperature_readings = {'day1': 0.5, 'day2': -2.3, 'day3': 1.2, 'day4': -0.8, 'day5': 3.1, 'day6': -1.5, 'day7': 0.9}
extreme_filter = lambda temp: abs(temp) > 1.0
extreme_temperatures = {day: temp for day, temp in temperature_readings.items() if extreme_filter(temp)}
sorted_extreme_temps = sorted(extreme_temperatures.values())
print(f'Result: {sorted_extreme_temps}')