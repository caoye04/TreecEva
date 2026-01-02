def calculate_efficiency(data):
    filtered = [x for x in data if x > 0]
    adjusted = [val * 1.5 if val < 10 else val * 0.8 for val in filtered]
    average = sum(adjusted) / len(adjusted) if adjusted else 0
    return round(average, 3)

# Sensor metrics (some values may be invalid or zero)
sensor_metrics = [0, 5, 12, -3, 8, 0, 15, 7]
temperature_factor = 2.1  # Irrelevant variable for distraction
dummy_list = [i**2 for i in range(5)]  # Minor distractor operation

energy_output = calculate_efficiency(sensor_metrics)
print(f"Result: {energy_output}")