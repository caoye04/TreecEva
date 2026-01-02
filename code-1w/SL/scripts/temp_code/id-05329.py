def calculate_adjustment(readings):
    baseline = sum(readings) / len(readings)
    deviation = readings[-1] - baseline
    adjustment_factor = 1.5 if deviation > 10 else 0.8
    pressure_adjustment = deviation * adjustment_factor
    return pressure_adjustment

sensor_readings = [98, 102, 99, 101, 115]
pressure_adjustment = calculate_adjustment(sensor_readings)
print(f"Result: {pressure_adjustment}")