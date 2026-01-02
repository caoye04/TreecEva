temperatures = set(range(-40, 61))
thresholds = {t for t in range(45, 101)}
event_temperatures = {x * 2 for x in range(20, 41)}
filtered_temps = temperatures.difference({t for t in temperatures if t < 0})
warning_levels = thresholds.union(event_temperatures)
result_set = filtered_temps.intersection(warning_levels)
irrelevant_counter = 0
for val in result_set:
    if val % 3 == 0:
        irrelevant_counter += 1
result_set_size = len(result_set)
print(f"Target result: {result_set_size}")