def calculate_efficiency(data):
    base_score = sum([x * 0.8 for x in data if x > 5])
    penalty = len([x for x in data if x < 3]) * 1.5
    return round(base_score - penalty, 2)

# Sensor readings from thermal array (simulated)
sensor_readings = [7, 6, 2, 8, 9, 1, 4, 7]

# Auxiliary variable (irrelevant to final computation)
baseline_average = sum(sensor_readings) / len(sensor_readings)

# Determine energy threshold based on efficiency calculation
energy_threshold = calculate_efficiency(sensor_readings)

# Print result for evaluation
print(f"Result: {energy_threshold}")