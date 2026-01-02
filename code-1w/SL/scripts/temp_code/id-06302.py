def filter_stable(data):
    return [x for x in data if x > 70]

analyze_readings = lambda vals: sum(map(lambda x: x ** 0.5, vals)) // len(vals)

readings = [68, 75, 88, 91, 62, 77, 85]
temperature_baseline = 70
energy_threshold = 0
diagnostic_log = []

stable_readings = filter_stable(readings)
final_diagnostic = analyze_readings(stable_readings)
energy_threshold = int(final_diagnostic * 1.5)

print(f"Result: {energy_threshold}")