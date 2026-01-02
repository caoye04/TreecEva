def calculate_safety_margin(data):
    base_level = sum(data) / len(data)
    peak = max(data)
    safety_factor = 1.2 if peak > 2 * base_level else 1.0
    return base_level * safety_factor

# Sensor readings from thermal array
temperature_readings = [23.5, 24.1, 22.7, 25.3, 48.9, 23.0]

critical_ratio = 1.5  # Threshold for alert system (unused in final computation)
energy_threshold = calculate_safety_margin(temperature_readings)

# Output result
print(f"Target result: {energy_threshold}")