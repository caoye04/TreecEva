from collections import defaultdict

# Simulate sensor data with noise and redundancy
data = [
    {'temp': 23.5, 'humidity': 45, 'pressure': 1013.25},
    {'temp': 24.1, 'humidity': 47, 'pressure': 1012.8},
    {'temp': 22.9, 'humidity': 44, 'pressure': 1014.1},
    {'temp': 25.0, 'humidity': 50, 'pressure': 1011.9},
    {'temp': 23.8, 'humidity': 46, 'pressure': 1013.0}
]

# Redundant weight mappings for different conditions
weights = {
    'temp': 0.4,
    'humidity': 0.3,
    'pressure': 0.3
}

# Irrelevant transformation: normalize pressure to sea level (not used)
def adjust_pressure_reading(pressure, altitude=150):
    return pressure * (1 - altitude / 145000)  # Approximation

# Misleading auxiliary function that calculates average but isn't directly used
def compute_average_readings(sensor_data):
    avg = defaultdict(float)
    n = len(sensor_data)
    for reading in sensor_data:
        avg['temp'] += reading['temp'] / n
        avg['humidity'] += reading['humidity'] / n
        avg['pressure'] += reading['pressure'] / n
    return dict(avg)

# Helper: extract baseline reference (middle reading)
baseline = data[len(data)//2]
baseline_temp = baseline['temp']
baseline_humidity = baseline['humidity']

# Distractor: simulate calibration offset (unused in final logic)
calibration_offsets = {}
for key in weights.keys():
    calibration_offsets[key] = round(baseline[key] * 0.01, 3)  # 1% offset

# Core logic: calculate weighted deviation score
def calculate_final_score(readings, weight_map):
    total_score = 0.0
    base_ref = readings[0]  # Use first as reference

    for i, reading in enumerate(readings):
        temp_diff = abs(reading['temp'] - base_ref['temp'])
        humidity_diff = abs(reading['humidity'] - base_ref['humidity'])
        pressure_diff = abs(reading['pressure'] - base_ref['pressure'])

        # Weighted penalty score based on deviation
        step_score = 0
        step_score += temp_diff * weight_map['temp'] * 10
        step_score += humidity_diff * weight_map['humidity'] * 5
        step_score += pressure_diff * weight_map['pressure'] * 2

        # Accumulate only on even indices (arbitrary filtering)
        if i % 2 == 0:
            total_score += step_score

        # Early break for large deviations (rarely triggered here)
        if temp_diff > 5:
            total_score -= 5
            break

    # Final adjustment: scale by number of relevant samples
    valid_samples = len([i for i in range(len(readings)) if i % 2 == 0])
    normalized_score = total_score / valid_samples if valid_samples else 0

    # Unused intermediate: entropy-like measure of variation (distractor)
    import math
    entropy_proxy = 0
    for x in [temp_diff, humidity_diff, pressure_diff]:
        if x > 0:
            entropy_proxy += x * math.log(x)

    return round(normalized_score, 4)

# Execute main computation
final_score = calculate_final_score(data, weights)

# Print result as required
print(f"Target result: {final_score}")