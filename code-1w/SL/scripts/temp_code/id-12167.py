def calculate_performance(data):
    total = 0
    adjustments = (0.5, -0.3, 0.8)
    for i, (name, value) in enumerate(zip(data, adjustments)):
        if 'sensor' in name.lower():
            total += value * 10
        else:
            total -= value * 2
    return int(total)

# Irrelevant auxiliary data (minimal distraction)
calibration_keys = ['A1', 'B2', 'C3']
temp_readings = [23.5, 24.1, 22.7]

benchmark_data = ['SensorAlpha', 'ActuatorBeta', 'sensorGamma']
initial_offset = 5
final_score = calculate_performance(benchmark_data)
print(f"Target result: {final_score}")