def calculate_efficiency(data):
    filtered = [x for x in data if x > 0]
    normalized = [val / sum(filtered) for val in filtered]
    return sum(i * val for i, val in enumerate(normalized))

# Sensor metrics from turbine array (irrelevant negative values represent faulty readings)
sensor_metrics = [3.5, -1.2, 4.8, -0.3, 2.1, 5.6]
baseline_adjustment = 0.05  # unused calibration offset (distractor)
energy_output = calculate_efficiency(sensor_metrics)
print(f"Result: {energy_output}")