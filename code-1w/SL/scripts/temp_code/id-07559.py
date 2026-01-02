def filter_readings(data):
    return [x for x in data if x > 50]

compute_score = lambda vals: sum(v ** 0.5 for v in vals)

def calculate_efficiency(readings):
    base = compute_score(readings)
    adjustment = 1.2 if len(readings) > 3 else 0.8
    return base * adjustment

# Sensor readings from thermal array (in megajoules)
sensor_data = [45, 67, 89, 52, 76, 30]

# Irrelevant auxiliary variable (minimal distraction)
baseline_calibration = 55

# Key computation chain
energy_threshold = calculate_efficiency(filter_readings(sensor_data))

print(f"Result: {energy_threshold}")