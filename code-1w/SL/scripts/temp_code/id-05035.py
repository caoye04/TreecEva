temperatures_celsius = [22.3, 25.1, 19.8, 30.0, 27.4]
max_temperature = max(temperatures_celsius)

# Define safety thresholds for different components (in Celsius)
safety_thresholds = {
    'cpu': 85,
    'gpu': 90,
    'ram': 75,
    'ssd': 70
}

# Calculate thermal safety margin based on most restrictive component
target_component = 'ssd' if max_temperature > 65 else 'ram'
baseline = 20
adjustment_factor = 1.2 if target_component == 'ssd' else 0.8
reference_point = baseline * adjustment_factor

temperature_risk = max_temperature - reference_point

# Key statement
termal_margin = min(safety_thresholds.values()) - max_temperature

Result: thermal_margin