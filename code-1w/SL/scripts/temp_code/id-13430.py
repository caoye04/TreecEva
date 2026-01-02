def monitor_system(diagnostic_fn, data_sequence):
    return sum(1 for reading in data_sequence if diagnostic_fn(reading))

baseline = 23.7
offset = 7.3
energy_threshold = round(baseline + offset, 1)
readings = [18.2, 25.6, 30.1, 22.8, 27.4, 20.0, 31.5]
system_flag = False
placeholder_value = [x * 2 for x in readings if x < 20]  # Irrelevant list comp (distractor)
final_diagnostic = monitor_system(lambda x: x > energy_threshold, readings)
print(f"Result: {energy_threshold}")