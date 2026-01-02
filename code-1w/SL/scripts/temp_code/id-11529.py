def analyze_readings(data):
    valid_readings = [x for x in data if x > 0]
    adjusted_readings = [(r * 1.05) for r in valid_readings]
    average = sum(adjusted_readings) / len(adjusted_readings)
    energy_threshold = average ** 2 if average > 50 else average ** 0.5
    return energy_threshold

readings = [45, -10, 67, 89, 0, 53]
final_diagnostic = analyze_readings(readings)
energy_threshold = final_diagnostic
print(f"Result: {energy_threshold}")